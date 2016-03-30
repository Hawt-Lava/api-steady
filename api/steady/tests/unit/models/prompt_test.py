from api.steady.models.prompt import Prompt

from api.steady.tests.base_test import BaseTest


class PromptTest(BaseTest):
    def test_properties(self):
        prompt = Prompt()
        text = self.faker.sentence()
        prompt.text = text
        self.assertEquals(prompt.text, text)

    def test_unicode(self):
        prompt = Prompt()
        text = self.faker.sentence()
        prompt.text = text
        self.assertEquals(str(prompt), text)
