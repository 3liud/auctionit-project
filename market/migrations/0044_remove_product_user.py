# Generated by Django 2.1.4 on 2019-01-25 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0043_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
