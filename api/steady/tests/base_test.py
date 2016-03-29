from faker import Factory
from rest_framework.test import APIClient, APITestCase


class BaseTest(APITestCase):
    def setUp(self):
        self.faker = Factory.create()

