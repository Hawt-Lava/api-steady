import random


class RandomNumberMixin:
    @staticmethod
    def random_number(lower=0, upper=10):
        """Creates a random number between two bounds

        Args:
            lower(int): The lower bound
            upper(int): The upper bound

        Returns:
            A number randomly generated between the bounds
        """
        return random.randrange(lower, upper)
