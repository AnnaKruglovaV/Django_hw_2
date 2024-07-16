from django.core.management import BaseCommand
import json
from django.conf import settings

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def read_json():
        with open(f'{settings.BASE_DIR}\\db.json', encoding='utf-8') as file:
            return json.load(file)

    def get_categories(self):
        data = self.read_json()
        return list(filter(lambda x: x.get('model') == 'catalog.category', data))

    def get_products(self):
        data = self.read_json()
        return list(filter(lambda x: x.get('model') == 'catalog.product', data))

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.get_categories(self):
            category_for_create.append(
                Category(
                    pk = category.get('pk'),
                    **category.get('fields'),
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.get_products(self):
            print(product['fields']['category'])
            if product['fields']['category'] is not None:
                product['fields']['category'] = Category.objects.get(pk=int(product['fields']['category']))

            product_for_create.append(
                Product(
                    pk=product.get('pk'),
                    **product.get('fields')
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
