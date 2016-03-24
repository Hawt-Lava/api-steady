from faker import Factory
from unittest import TestCase

class ScoresheetTest(TestCase):
    def setUp(self):
        self.faker = Factory.create()
