from faker import Factory
from rest_framework.test import APITestCase
from api.steady.mixins.random_number import RandomNumberMixin


class BaseTest(APITestCase, RandomNumberMixin):
    def setUp(self):
        self.faker = Factory.create()
