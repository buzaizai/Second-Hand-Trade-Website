import json
import time

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

import myapp.models
from myapp.models import Product, CartItem
from .models import User


# Create your views here.
# Create your views here.
# 以下是二手交易平台函数

class RegisterView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        email = request.data.get('email')
        email_code = request.data.get('emailCode')

        # 检查必要参数是否缺失
        if not all([phone, password, email, email_code]):
            return Response({'error': '参数缺失'}, status=status.HTTP_400_BAD_REQUEST)

        # 检查邮箱验证码是否正确
        # 这里省略了具体的邮箱验证码检查逻辑，请根据实际情况自行判断

        # 从缓存中获取之前发送给用户的验证码
        verification_code = cache.get(f'email_verification_code_{email}')

        if email_code != verification_code:
            # 验证码不匹配，验证失败
            return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

        # 检查邮箱是否已被注册
        if User.objects.filter(email=email).exists():
            return Response({'error': '邮箱已被注册'}, status=status.HTTP_409_CONFLICT)

        # 创建用户
        user = User(phone=phone, password=password, email=email)
        auth_token = generate_auth_token()
        user.auth_token = auth_token
        user.save()

        return Response({'success': True}, status=status.HTTP_201_CREATED)

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random

def generate_verification_code():
    """生成随机的 6 位验证码"""
    return str(random.randint(100000, 999999))

def send_verification_code(receiver):
    """发送验证码邮件"""
    smtp_server = 'smtp.qq.com'
    port = 465
    sender = '2164820351@qq.com'  # 发件人邮箱
    password = 'gnxrzlnwettddhgfx'  # 发件人邮箱的授权码或密码

    subject = '验证码'  # 邮件标题
    verification_code = generate_verification_code()  # 生成验证码
    content = '您的验证码是：{}'.format(verification_code)  # 邮件内容

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(sender)
    message['To'] = Header(receiver)
    message['Subject'] = Header(subject)

    try:
        smtp_obj = smtplib.SMTP_SSL(smtp_server, port)
        smtp_obj.login(sender, password)
        smtp_obj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
        return verification_code
    except smtplib.SMTPException as e:
        print("邮件发送失败：" + str(e))
        return None
from django.conf import settings
MAX_SEND_LIMIT = getattr(settings, 'MAX_SEND_LIMIT', 3)
MIN_SEND_INTERVAL = getattr(settings, 'MIN_SEND_INTERVAL', 60)

@api_view(['POST'])
def send_email_code(request):
    email = request.data.get('email')  # 使用 request.data 获取 POST 请求的数据
    last_send_time = cache.get(f'email_send_time_{email}')
    send_count = cache.get(f'email_send_count_{email}', 0)
    now = time.time()
    if last_send_time and (now - last_send_time) < MIN_SEND_INTERVAL:
        return Response({'message': '发送邮件过于频繁，请稍后再试'}, status=status.HTTP_429_TOO_MANY_REQUESTS)

    if send_count >= MAX_SEND_LIMIT:
        return Response({'message': '发送次数已达上限，请稍后再试'}, status=status.HTTP_429_TOO_MANY_REQUESTS)
    verification_code = send_verification_code(email)
    if verification_code:
        send_count += 1
        cache.set(f'email_send_count_{email}', send_count)
        cache.set(f'email_send_time_{email}', now)
        cache.set(f'email_verification_code_{email}',verification_code)
        return Response({'message': 'success'})
    else:
        print("邮件发送失败")
    return Response({'message': 'error'})

@api_view(['POST'])
def verify_email_code(request):
    email = request.data.get('email')
    user_input_code = request.data.get('code')

    # 从缓存中获取之前发送给用户的验证码
    verification_code = cache.get(f'email_verification_code_{email}')

    if user_input_code == verification_code:
        # 验证码匹配，验证成功
        # 执行后续逻辑，比如允许用户进行下一步操作
        return Response({'message': '验证成功'})
    else:
        # 验证码不匹配，验证失败
        return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse, HttpResponse

import uuid

def generate_auth_token():
    return str(uuid.uuid4())  # 使用UUID算法生成唯一令牌

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        # 查询用户对象
        user = User.objects.get(email=email)
        # 验证密码
        if password ==user.password:
            auth_token = generate_auth_token()
            user.auth_token = auth_token
            user.save()
            # 登录成功
            response = {
                'success': True,
                'message': '登录成功'
            }
            http_response = HttpResponse(json.dumps(response), content_type='application/json')
            http_response.set_cookie('authToken', auth_token)
            return http_response
        else:
            # 登录失败，密码不匹配
            response = {
                'success': False,
                'message': '邮箱或密码错误'
            }
            return JsonResponse(response, status=401)
    except User.DoesNotExist:
        # 登录失败，用户不存在
        response = {
            'success': False,
            'message': '邮箱或密码错误'
        }
        return JsonResponse(response, status=401)

@api_view(['POST'])
def forgetView(request):
    password = request.data.get('newPassword')
    email = request.data.get('email')
    email_code = request.data.get('code')

    # 检查必要参数是否缺失
    if not all([password, email, email_code]):
        return Response({'error': '参数缺失'}, status=status.HTTP_400_BAD_REQUEST)

    # 检查邮箱验证码是否正确
    # 这里省略了具体的邮箱验证码检查逻辑，请根据实际情况自行判断

    # 从缓存中获取之前发送给用户的验证码
    verification_code = cache.get(f'email_verification_code_{email}')
    if email_code != verification_code:
        # 验证码不匹配，验证失败
        return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(email=email)
        user.password = password
        user.save()
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        return Response({'success': True}, status=status.HTTP_404_NOT_FOUND)


def get_products(request):
    page = request.GET.get('page', 1)
    category = request.GET.get('category', None)
    per_page = 8  # 每页显示的商品数量
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, per_page)
    paginated_products = paginator.get_page(page)

    serialized_products = [
        {
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
            'image': product.image_url,
            'category': product.category
        }
        for product in paginated_products
    ]

    return JsonResponse({'products': serialized_products})

def get_products_count(request):
    category = request.GET.get('category')
    if category == '':
        product_count = Product.objects.count()
    else:
        product_count = Product.objects.filter(category=category).count()
    return JsonResponse({'page_count': product_count})

def get_mysell_count(request):
    mysell_count = mysell.objects.count()
    return JsonResponse({'page_count': mysell_count})

def get_product(request):
    id = request.GET.get('id')
    try:
        product = Product.objects.get(id=id)
        data = {
            'image_url': product.image_url,
            'name': product.name,
            'quantity': product.quantity,
            'price': str(product.price),
            'details': product.details,
            'category': product.category,
            'condition': product.condition,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def get_user(request):
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(' ')[1]  # 提取令牌字符串
    user = User.objects.get(auth_token=auth_token)
    user_info = {
        'email': user.email,
        'username': user.username,
        'phone': user.phone
    }
    return JsonResponse(user_info)

def get_cart_items(request):
    cart_items = CartItem.objects.all()
    data = []
    for item in cart_items:
        product = item.product_id
        product_data = Product.objects.get(id=product)
        data.append({
            'product_id': product_data.id,
            'image_url': product_data.image_url,
            'name': product_data.name,
            'price': product_data.price,
        })
    return JsonResponse(data, safe=False)



def add_to_cart(product):
    # 创建购物车对象
    cart = CartItem(product=product)

    # 保存购物车对象到数据库
    cart.save()
def add_to_cart_api(request):
    id = request.GET.get('id')
    product = Product.objects.get(id=id)
    cart = CartItem(product=product)
    cart.save()
    response_data = {
        'message': 'Product added to cart successfully.'
    }
    return JsonResponse(response_data)


def remove_from_cart_api(request):
    id = request.GET.get('id')

    try:
        cart_item = CartItem.objects.get(product_id=id)
        cart_item.delete()
        response_data = {
            'message': 'Product removed from cart successfully.'
        }
    except CartItem.DoesNotExist:
        response_data = {
            'error': 'Item not found in cart.'
        }

    return JsonResponse(response_data)

@api_view(['POST'])
def add_to_product(request):
    data = json.loads(request.body)
    name = data.get('name')
    quantity = data.get('quantity')
    price = data.get('price')
    details = data.get('details')
    category = data.get('category')
    condition = data.get('condition')
    image_url = data.get('image_url')

    # 创建Product对象，并保存到数据库
    product = Product(
        name=name,
        quantity=quantity,
        price=price,
        details=details,
        category=category,
        condition=condition,
        image_url=image_url
    )
    product.save()
    product_id=product.id
    response_data = {
        'message': 'Product added to cart successfully.',
        'product_id': product_id
    }
    return JsonResponse(response_data)
from myapp.models import mysell
@api_view(['POST'])
def add_to_mysell(request):
    data = json.loads(request.body)
    product_id = data.get('id')
    # 创建Product对象，并保存到数据库
    mysell = myapp.models.mysell(
        product_id=product_id
    )
    mysell.save()
    response_data = {
        'message': 'mysell added successfully.',
    }
    return JsonResponse(response_data)

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']

        # 验证图片大小和类型
        if validate_image(image):
            # 保存图片到指定目录
            save_path = save_image(image)

            response_data = {
                'message': 'Image uploaded successfully.',
                'path': save_path  # 返回保存的图片路径
            }
            return JsonResponse(response_data)
        else:
            response_data = {
                'message': 'Invalid image format or size.'
            }
            return JsonResponse(response_data, status=400)
    else:
        response_data = {
            'message': 'No image file provided.'
        }
        return JsonResponse(response_data, status=400)


import os
from PIL import Image

@csrf_exempt
def validate_image(image):
    # 验证图片类型
    allowed_formats = ['JPEG', 'PNG']
    image_format = image.content_type.split('/')[1].upper()
    if image_format not in allowed_formats:
        return False

    # 验证图片大小
    # max_size = 5 * 1024 * 1024  # 限制图片大小为 5MB
    # if image.size > max_size:
    #     return False

    return True

@csrf_exempt
def save_image(image):
    # 将图片保存到指定目录的逻辑

    # 创建保存目录（如果不存在）
    save_dir = 'media/'
    os.makedirs(save_dir, exist_ok=True)

    # 生成保存路径
    save_path = os.path.join(save_dir, image.name)

    # 保存图片
    with open(save_path, 'wb') as f:
        for chunk in image.chunks():
            f.write(chunk)

    return save_path

def root_view(request):
    if request.method == 'POST':
        # 处理 POST 请求的逻辑
        return HttpResponse('POST 请求成功')
    else:
        return HttpResponse('其他请求方法')


def get_mysell_products(request):
    mysell_products = mysell.objects.values("product_id")
    product_ids = [item["product_id"] for item in mysell_products]
    products = Product.objects.filter(id__in=product_ids)

    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    response_data = []
    for product in page_obj:
        product_data = {
            "product_id": product.id,
            "name": product.name,
            "image_url": product.image_url,
            "quantity": product.quantity,
            "price": str(product.price),
            "details": product.details,
            "category": product.category,
            "condition": product.condition
        }
        response_data.append(product_data)

    return JsonResponse({
        "products": response_data,
    })

@api_view(['POST'])
def update_username(request):
    try:
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(' ')[1]  # 提取令牌字符串
        user = User.objects.get(auth_token=auth_token)
        new_username = request.data.get('username')
        user.username = new_username
        user.save()
        return JsonResponse({'message': 'Username updated successfully.'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=404)

@api_view(['DELETE'])
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class MySellDetailView(APIView):
    def get(self, request, product_id):
        mysell_instance = get_object_or_404(mysell, product__id=product_id)
        product = mysell_instance.product
        data = {
            'productList': [
                {
                    'image_url': product.image_url,
                    'name': product.name,
                    'quantity': product.quantity,
                    'price': product.price,
                    'details': product.details,
                    'category': product.category,
                    'condition': product.condition
                }
            ]
        }
        return Response(data)


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # 获取前端传递的数据
        image_url = request.POST.get('image_url')
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        details = request.POST.get('details')
        category = request.POST.get('category')
        condition = request.POST.get('condition')

        # 更新商品信息
        product.image_url = image_url
        product.name = name
        product.quantity = quantity
        product.price = price
        product.details = details
        product.category = category
        product.condition = condition

        # 保存更新后的商品信息
        product.save()

        return JsonResponse({'success': True, 'message': '商品信息更新成功'})

    return JsonResponse({'success': False, 'message': '仅支持POST请求'})