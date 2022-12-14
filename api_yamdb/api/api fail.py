import csv
import os
import pathlib
# path = pathlib.Path( "static", "data", "category.csv")
# from api_yamdb.settings import STATICFILES_DIRS
#
# print(STATICFILES_DIRS)
unsorted_file_list = os.listdir()
print(unsorted_file_list)

try:
    with open("../static/data/category.csv", encoding='utf-8') as f:
        DictReader_obj = csv.DictReader(f)
        for item in DictReader_obj:
            print(dict(item))
except FileNotFoundError:
     print("Файл не найден")
