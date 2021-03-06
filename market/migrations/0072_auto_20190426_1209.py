# Generated by Django 2.2 on 2019-04-26 09:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0071_auto_20190426_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='FBidder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bid_amount', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')])),
                ('bid_status', models.CharField(choices=[('PENDING', '0'), ('WINNER', '1')], default='PENDING', max_length=20)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Product')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
