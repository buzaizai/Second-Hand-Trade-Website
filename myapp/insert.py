from models import CartItem, Product


def add_to_cart(request):
    # 创建购物车项对象
    cart_item = CartItem(product=product)

    # 保存购物车项对象到数据库
    cart_item.save()

# 调用示例
product = Product.objects.get(id=1)  # 假设已经获取到了产品
add_to_cart(product)