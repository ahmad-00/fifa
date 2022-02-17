from django.apps import AppConfig
import csv

from core.utils import CurrencyToInt
from django.db import connection


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        convertor = CurrencyToInt()
        prepared_list = ''
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader, None)
            for line in reader:
                line[0] = int(line[0]) + 1
                line[11] = convertor(value=line[11])
                line[12] = convertor(value=line[12])
                line[88] = convertor(value=line[88])
                line[26] = line[26].replace("'", ".")
                line[2] = line[2].replace("'", "")
                line[9] = line[9].replace("'", "")
                line[24] = line[24].replace("'", "")

                prepared_list += str(tuple(line)) + ','
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO player VALUES {}'''.format(prepared_list[:-1]))
        connection.commit()
