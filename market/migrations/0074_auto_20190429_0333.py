# Generated by Django 2.2 on 2019-04-29 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0073_auto_20190429_0326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fbidder',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='fbidder',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='Farmproduce',
        ),
        migrations.DeleteModel(
            name='FBidder',
        ),
    ]