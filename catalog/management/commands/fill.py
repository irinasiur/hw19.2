from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle_product(self, *args, **options):
        Product.objects.all().delete()
        product_list = [
            {'name': 'арбуз', 'description': 'однолетнее травянистое растение семейства тыквенные', 'category': 'фрукты', 'purchase_price': '100', 'date_of_creation': '',
             'last_modified_date': ''},
            {'name': 'морковь', 'description': 'корнеплод двухлетнего растения имеет вытянутую форму в виде конуса, иногда овальную, без выраженной кожуры', 'category': 'овощи', 'purchase_price': '20', 'date_of_creation': '',
             'last_modified_date': ''},
            {'name': 'рис', 'description': 'крупяная культура, которая произрастает в основном в тропических и субтропических регионах', 'category': 'крупы', 'purchase_price': '100', 'date_of_creation': '',
             'last_modified_date': ''},
            {'name': 'слива', 'description': 'съедобный сочный плод с упругой мякотью и крупной косточкой', 'category': 'фрукты', 'purchase_price': '150', 'date_of_creation': '',
             'last_modified_date': ''},
            {'name': 'батат', 'description': 'клубнеплодное растение семейства вьюнковых', 'category': 'овощи', 'purchase_price': '150', 'date_of_creation': '',
             'last_modified_date': ''},
            {'name': 'булгур',
             'description': 'зёрна пшеницы, которые пропаривают, а затем подсушивают и дробят',
             'category': 'крупы', 'purchase_price': '200', 'date_of_creation': '',
             'last_modified_date': ''}
        ]
        products_for_create = []
        for product_item in product_list:
            products_for_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_for_create)

    def handle_category(self, *args, **options):
        Product.objects.all().delete()
        category_list = [
            {'name': 'фрукты', 'description': 'сочные, как правило, сладкие плоды, которые растут на деревьях или кустарниках'},
            {'name': 'овощи', 'description': 'огородина, съедомая ботва и коренья'},
            {'name': 'крупы', 'description': 'целые, дробленые, прессованные'},
        ]
        categorys_for_create = []
        for category_item in category_list:
            categorys_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(categorys_for_create)



