import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify

class Command(BaseCommand):
    print('заливаем мобилки.')
    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str, help='D:\IT\Проекты\dj-homeworks\2.1-databases\work_with_database\phones.csv')

    def handle(self, *args, **options):
        csv_file_path = options['csvfile']
        with open(csv_file_path, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                new_phone = Phone.objects.create(
                id=int(phone['id']),
                name=phone['name'],
                price=int(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slugify(phone['name'])
                )

        self.stdout.write(self.style.SUCCESS(f'Успешно импортировано {len(phones)} phones'))

# Вызвать функцию
# python manage.py import_phones phones.csv