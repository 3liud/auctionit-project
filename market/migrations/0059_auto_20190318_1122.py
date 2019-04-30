# Generated by Django 2.1.4 on 2019-03-18 08:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0058_auto_20190317_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sell_on',
            field=models.DurationField(default=django.utils.timezone.now, verbose_name='When do you want your item to go live for Auction?'),
        ),
    ]