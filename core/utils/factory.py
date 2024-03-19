from abc import ABC

from faker import Faker


class BaseFaker(ABC):

    def __init__(self):
        self.faker = Faker()
