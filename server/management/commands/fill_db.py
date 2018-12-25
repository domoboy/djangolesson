from django.core.management.base import BaseCommand
from products.models import CategoryProduct, Product, ShopUser
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'server/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        CategoryProduct.objects.all().delete()
        for category in categories:
            new_category = CategoryProduct(**category)
            new_category.save()

        products = loadFromJSON('products')

        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            # получаем категорию по имени
            _category = CategoryProduct.objects.get(name=category_name)
            # заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser(
            'django',
            'konoplya-ne@narod.ru',
            'geekbrains',
            age=36
        )
