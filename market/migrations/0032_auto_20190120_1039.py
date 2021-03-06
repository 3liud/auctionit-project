# Generated by Django 2.1.4 on 2019-01-20 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0031_auto_20190120_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postsell',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=10, verbose_name='What is the least price you are selling your item for?'),
        ),
        migrations.AlterField(
            model_name='postsell',
            name='sell_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='When do you want your item to go live for Auction?'),
        ),
    ]
