# Generated by Django 2.1.4 on 2019-01-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0023_auto_20190117_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_time',
            field=models.TimeField(choices=[('5 minutes', '5'), ('10 minutes', '10'), ('20 minutes', '20'), ('30 minutes', '30')], max_length=2),
        ),
    ]
