# Generated by Django 4.1.7 on 2023-07-19 08:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_product_category_alter_product_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
