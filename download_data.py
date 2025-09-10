from pathlib import Path

from pandas import read_csv

from cms_data import request_file, unpack_zip


df = read_csv("data/beneficiary_2025.csv", delimiter="|")
print()
