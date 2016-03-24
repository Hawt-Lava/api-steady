from api.steady.models.prompt import Prompt

from faker import Factory
from unittest import TestCase


class PromptTest(TestCase):
    def setUp(self):
        self.fake = Factory.create()

    def test_properties(self):
        prompt = Prompt()
        text = self.fake.sentence()
        prompt.text = text
        self.assertEquals(prompt.text, text)

    def test_unicode(self):
        prompt = Prompt()
        text = self.fake.sentence()
        prompt.text = text
        self.assertEquals(str(prompt), text)
