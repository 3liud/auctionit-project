# Generated by Django 2.1.7 on 2019-04-06 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190406_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(default='0000', max_length=19),
        ),
        migrations.AlterField(
            model_name='account',
            name='county',
            field=models.CharField(default='Nairobi', max_length=19),
        ),
        migrations.AlterField(
            model_name='account',
            name='postal_code',
            field=models.CharField(default='0000', max_length=19),
        ),
    ]