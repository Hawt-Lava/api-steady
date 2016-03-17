from unittest import TestCase
from steady.models.prompt import Prompt
import faker import Factory

class PromptTest(TestCase):

    def setUp(self):
        self.faker = Faker()

    def testProperties(self):
        prompt = Prompt()
        text = self.faker.text
        prompt.text = text
        self.assertEquals(prompt.text, text)


