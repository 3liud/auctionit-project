# Generated by Django 2.1.4 on 2019-03-18 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0060_auto_20190318_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sell_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
