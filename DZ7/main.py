from os.path import exists
from CSV_creating import creating
from file_operation import writing_csv
from file_operation import writing_txt
from file_operation import open_csv


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt()
open_csv()