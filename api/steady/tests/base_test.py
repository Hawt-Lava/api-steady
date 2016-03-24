from faker import Factory
from unittest import TestCase

class BaseTest(TestCase):
    def setUp(self):
        self.faker = Factory.create()
