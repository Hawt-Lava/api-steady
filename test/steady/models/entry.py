class EntryTest(TestCase):

    def setUp(self):
        self.faker = Factory()

    def test_properties(self):
        score = self.faker.int
        prompt = Prompt()
        entry = Entry()
        entry.prompt = prompt
        entry.score = score
        self.assertEquals(entry.prompt, prompt)
        self.assertEquals(entry.score, score)

