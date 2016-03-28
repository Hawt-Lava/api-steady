from api.steady.tests.base_test import BaseTest
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry
from api.steady.models.prompt import Prompt


class ScoresheetTest(BaseTest):
    def test_properties(self):
        scoresheet = ScoreSheet()

        label = self.faker.sentence()
        scoresheet.label = label

        scoresheet.save()
        entry1 = Entry()
        entry2 = Entry()

        entry1.score = 1
        entry2.score = 2

        entry1.save()
        entry2.save()

        scoresheet.entries.add(entry1, entry2)

        self.assertEquals(scoresheet.label, label)
        self.assertEquals(len(scoresheet.entries.all()), 2)

    def test_full_relationship_tree(self):

        # Create Prompts
        prompt1 = Prompt(text=self.faker.sentence())
        prompt2 = Prompt(text="foo")  # self.faker.sentence())

        prompt1.save()
        prompt2.save()

        # Create Entries
        entry1 = Entry(score=1, prompt=prompt1)
        entry2 = Entry(score=2, prompt=prompt2)

        entry1.save()
        entry2.save()

        # Create ScoreSheet
        label = self.faker.sentence()
        scoresheet = ScoreSheet(label=label)

        scoresheet.save()
        scoresheet.entries.add(entry1, entry2)

        # Make Assertions Throughout Relationship Tree
        self.assertEquals(scoresheet.label, label)
        self.assertEquals(len(scoresheet.entries.all()), 2)

        result_entry1 = scoresheet.entries.all()[0]  # type: Entry
        result_entry2 = scoresheet.entries.all()[1]  # type: Entry

        self.assertEquals(result_entry1, entry1)
        self.assertEquals(result_entry2, entry2)

        self.assertEquals(result_entry1.prompt, prompt1)

        self.assertEquals(result_entry2.prompt, prompt2)
