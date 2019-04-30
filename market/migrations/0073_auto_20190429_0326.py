# Generated by Django 2.2 on 2019-04-29 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0072_auto_20190426_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbidder',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Farmproduce'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('General', 'General'), ('Painting', 'Painting'), ('Sculpture', 'Sculpture'), ('Book', 'Book'), ('Instrument', 'Instrument'), ('Agriculture', 'Agriculture')], default='Gen', max_length=100, verbose_name='Choose product category'),
        ),
    ]