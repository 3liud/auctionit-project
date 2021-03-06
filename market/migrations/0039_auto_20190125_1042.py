# Generated by Django 2.1.4 on 2019-01-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
	atomic = False
	dependencies = [
		('market', '0038_auto_20190125_1034'),
	]
	
	operations = [
		migrations.AlterField(
			model_name='product',
			name='category',
			field=models.CharField(
				choices=[('General', 'Gen'), ('Painting', 'Paint'), ('Sculpture', 'Sculpture'), ('Book', 'Book'),
				         ('Instrument', 'Inst')], default='Gen', max_length=100,
				verbose_name='Choose product category'),
		),
	]

