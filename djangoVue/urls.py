"""djangoVue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from myapp.views import get_products, MySellDetailView, update_product
from myapp.views import get_product
from myapp.views import RegisterView
from myapp.views import send_email_code
from myapp.views import login
from myapp.views import forgetView
from myapp.views import get_products_count
from myapp.views import get_mysell_count
from myapp.views import get_user
from myapp.views import get_cart_items
from myapp.views import add_to_cart_api
from myapp.views import remove_from_cart_api
from myapp.views import add_to_product
from myapp.views import add_to_mysell
from myapp.views import upload_image
from myapp.views import get_mysell_products
from myapp.views import update_username
from myapp.views import delete_product
from django.conf import settings
from django.conf.urls.static import static

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        # 处理 GET 请求的逻辑
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        # 处理 POST 请求的逻辑
        # 这里可以根据需要进行自定义处理
        return self.render_to_response(self.get_context_data())

urlpatterns = [
    path('admin', admin.site.urls),
    path('', IndexView.as_view(), name='index.html'),
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/send_email_code', send_email_code, name='email_code'),
    path('api/login', login, name='login'),
    path('api/change-password', forgetView, name='forget'),
    path('api/products', get_products, name='get_products'),
    path('api/products/count', get_products_count, name='get_products_count'),
    path('api/mysell/count', get_mysell_count, name='get_mysell_count'),
    path('api/mysell', get_mysell_products, name='get_mysell'),
    path('api/product', get_product, name='get_product'),
    path('api/get_user', get_user, name='get_user'),
    path('api/cart',get_cart_items , name='get_cart'),
    path('api/add_cart',add_to_cart_api , name='add_cart'),
    path('api/remove_cart',remove_from_cart_api , name='remove_cart'),
    path('api/add_product',add_to_product , name='add_product'),
    path('api/add_mysell',add_to_mysell , name='add_to_mysell'),
    path('api/upload_image/', upload_image, name='upload_image'),
    path('api/update_username', update_username, name='update_username'),
    path('api/delete_mysell/<int:product_id>/', delete_product),
    path('api/mysell/<int:product_id>/', MySellDetailView.as_view(), name='mysell-detail'),
    path('api/update_product/<int:product_id>/', update_product, name='update_product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)