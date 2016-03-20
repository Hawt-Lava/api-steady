from unittest import TestCase
from api.steady.models.prompts import Prompt
from faker import Factory

class PromptTest(TestCase):

    def setUp(self):
        self.faker = Factory()

    def testProperties(self):
        prompt = Prompt()
        text = self.faker.text
        prompt.text = text
        self.assertEquals(prompt.text, text)
