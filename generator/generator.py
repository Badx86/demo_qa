import random

from data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(18, 55),
        department=faker_ru.job(),
        salary=random.randint(10, 350000),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_file():
    path = rf"C:\Users\мвидео\PycharmProjects\DemoQA\filetest{random.randint(0,999)}.txt"
    file = open(path, "w+")
    file.write(f"Hello World!{random.randint(0,999)}")
    file.close()
    return file.name, path
