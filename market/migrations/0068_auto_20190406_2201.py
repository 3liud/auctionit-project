# Generated by Django 2.1.7 on 2019-04-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0067_auto_20190406_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(default='Kenya', max_length=200),
        ),
    ]
