# Generated by Django 2.1.4 on 2018-12-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catecory_id',
            new_name='category_id',
        ),
    ]
