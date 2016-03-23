from api.steady.models.prompt import Prompt

from faker import Factory
from unittest import TestCase


class PromptTest(TestCase):
    def setUp(self):
        self.fake = Factory.create()
    def testProperties(self):
        prompt = Prompt()
        text = self.fake.sentence()
        prompt.text = text
        self.assertEquals(prompt.text, text)
