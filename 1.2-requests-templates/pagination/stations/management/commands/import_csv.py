import csv
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    print(f"Входим в класс")
    file_name = 'data-398-2018-08-30.csv'
    file_found = False

    def handle(self, *args, **options):
        # Получите корневой каталог проекта Django.
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(f"Входим в функцию")

        for root, dirs, files in os.walk(project_root):
            if self.file_name in files:
                file_path = os.path.join(root, self.file_name)
                print(f"Found file at: {file_path}")
                self.file_found = True
                break
            if not self.file_found:
                print(f"File {self.file_name} not found.")

# python manage.py import_csv data-398-2018-08-30.csv