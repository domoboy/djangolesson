# Generated by Django 2.1.4 on 2018-12-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181223_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10, verbose_name='цена'),
        ),
    ]
