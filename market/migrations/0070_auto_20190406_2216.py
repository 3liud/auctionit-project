# Generated by Django 2.1.7 on 2019-04-06 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0069_auto_20190406_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]