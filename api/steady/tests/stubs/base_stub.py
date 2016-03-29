from api.steady.mixins.random_number import RandomNumberMixin

from faker import Factory


class BaseStub(RandomNumberMixin):
    def __init__(self):
        self.faker = Factory.create()
