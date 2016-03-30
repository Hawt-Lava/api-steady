import random


class RandomNumberMixin:
    @staticmethod
    def random_number(lower=0, upper=10):
        return random.randrange(lower, upper)
