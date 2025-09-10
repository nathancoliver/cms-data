import os
from pathlib import Path

from pandas import read_csv
from requests import get  # type: ignore


def unpack_zip(path: str | Path):
    pass


def request_file(url: str):
    response = get(url)
    print()
