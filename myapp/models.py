# Create your models here.
import uuid

from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'myapp'
def __unicode__(self):
    return self.book_name


class User(models.Model):
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=20,default='新用户')
    password = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    auth_token = models.UUIDField(default=uuid.uuid4, editable=False)
class Product(models.Model):
    image_url = models.URLField(null=True)
    name = models.CharField(max_length=100,null=True)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True)
    details = models.TextField(null=True)
    category = models.CharField(max_length=50,null=True)
    condition = models.CharField(max_length=50,default='九成',null=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)

class mysell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, unique=True)
