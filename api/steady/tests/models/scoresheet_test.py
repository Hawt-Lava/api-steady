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
        
        prompt1 = Prompt(text=self.faker.sentence())
        prompt2 = Prompt(text=self.faker.sentence())
        
        scoresheet.entries.add(entry1, entry2)

        entry1.prompt = prompt1
        entry2.prompt = prompt2
        
        scoresheet.save()

        self.assertEquals(scoresheet.label, label)
        self.assertEquals(len(scoresheet.entries.all()), 2)
        // Assert Prompt and Entries are correct
        self.assertEquals(scoresheet.entries.get(id))
