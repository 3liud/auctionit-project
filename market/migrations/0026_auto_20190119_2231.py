# Generated by Django 2.1.4 on 2019-01-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0025_auto_20190119_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_time',
            field=models.TimeField(choices=[('5', '5'), ('10', '10'), ('20', '20'), ('30', '30')], max_length=20),
        ),
    ]
