from abc import ABC

from faker import Faker


class BaseFaker(ABC):
    model = None

    def __init__(self):
        self.faker = Faker()
