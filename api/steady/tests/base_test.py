from faker import Factory
from rest_framework.test import APIClient, APITestCase
from api.steady.mixins.random_number import RandomNumber


class BaseTest(APITestCase, RandomNumber):
    def setUp(self):
        self.faker = Factory.create()
