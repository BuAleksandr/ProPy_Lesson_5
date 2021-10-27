import datetime
import os
import json
from pprint import pprint
import hashlib

file_txt = os.path.join(os.getcwd(), "notepad.txt")


def parametrized_decor(random_file):
    def logger(foo):
        def func(*args, **kwargs):
            with open("notepad.txt", "r", encoding="utf-8") as f:
                result_func = foo(*args, **kwargs)
                with open("notepad.txt", "w", encoding="utf-8") as f:
                    now = datetime.datetime.now()
                    f.write(f'Путь к файлу с логами {random_file}\n')
                    f.write(f'{str(now)}\n')
                    f.write(f"Вызвана функция {foo.__name__}\n")
                    f.write(f"с аргументами {args} {kwargs}\n")
                return result_func

        return func

    return logger


@parametrized_decor
def old_func():
    pass


class Country_Iterator:
    def __init__(self, json_file):
        with open(file_json, 'r') as file:
            self.my_json = json.load(file)
        self.start = -1
        self.end = len(self.my_json)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.my_json[self.start]['name']['common']


if __name__ == '__main__':
    def generate(path):
        with open(path) as file:
            for line in file:
                yield line.upper()


    url = "https://en.wikipedia.org/wiki/"
    file_json = os.path.join(os.getcwd(), "countries.json")
    for name_country in Country_Iterator(file_json):
        name_fix = url + name_country.replace(" ", "_")
        pprint(f'Город {name_country} - {name_fix}')
        hash_object = hashlib.md5(b'{name_fix}')
        print(hash_object.hexdigest())

