# Generated by Django 2.2 on 2019-04-26 06:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0070_auto_20190406_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='live_time',
            field=models.CharField(choices=[('1', '1 minutes'), ('5', '5 minutes'), ('10', '10 minutes'), ('20', '20 minutes'), ('30', '30 minutes'), ('60', '1 Hour')], default='5', max_length=20, verbose_name='How long should your item stay in the auction table?'),
        ),
        migrations.CreateModel(
            name='Farmproduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Input the title of the Item you are selling')),
                ('description', models.TextField(default='', verbose_name='describe the produce, breed of cattle/ variety of the crop')),
                ('image', models.ImageField(default='', upload_to='commodity_pics', verbose_name='Let the buyer see what you are selling, upload a current picture of the produce or the crop')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('Tea', 'Tea'), ('Maize', 'Maize'), ('Milk', 'Milk')], max_length=100, verbose_name='Choose Farm produce type ')),
                ('price', models.IntegerField(verbose_name='What is the least unit price you are selling for?')),
                ('sell_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('live_time', models.CharField(choices=[('1', '1 month'), ('2', '5 months'), ('5', '5 months')], default='5', max_length=20, verbose_name='How long should your item stay in the auction table?')),
                ('seller', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
