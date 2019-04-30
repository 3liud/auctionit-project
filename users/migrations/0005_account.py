# Generated by Django 2.1.7 on 2019-04-06 19:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20190330_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default=100000, max_length=20, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric are allowed.')])),
                ('country', models.CharField(default='Kenya', max_length=200)),
                ('cardNumber', models.CharField(default='AUCT-010', max_length=30)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]