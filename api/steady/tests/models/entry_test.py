from api.steady.models.prompt import Prompt
from api.steady.models.entry import Entry
from api.steady.tests.base_test import BaseTest


class EntryTest(BaseTest):
    def test_properties(self):
        score = 1
        prompt = Prompt()
        entry = Entry()
        entry.prompt = prompt
        prompt_text = self.faker.sentence()
        prompt.text = prompt_text
        entry.score = score
        self.assertEquals(entry.prompt, prompt)
        self.assertEquals(entry.prompt.text, prompt_text)
        self.assertEquals(entry.score, score)
