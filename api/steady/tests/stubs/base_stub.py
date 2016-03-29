from api.steady.mixins.random_number import RandomNumber

from faker import Factory


class BaseStub(RandomNumber):
    def __init__(self):
        self.faker = Factory.create()
