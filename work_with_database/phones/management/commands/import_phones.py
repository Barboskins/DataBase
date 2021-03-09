import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.DictReader(csvfile, delimiter=';')

            # phone_reader = csv.reader(csvfile, delimiter=';')
            # # пропускаем заголовок
            # next(phone_reader)

            for line in phone_reader:
                Phone.objects.create(
                    id=line.get('id'),
                    name=line.get('name'),
                    price=line.get('price'),
                    image=line.get('image'),
                    release_date=line.get('release_date'),
                    lte_exists=line.get('lte_exists'),
                    slug=line.get('name')
                )
                # # TODO: Добавьте сохранение модели
                # pass
