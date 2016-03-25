from api.steady.tests.base_test import BaseTest
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry


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
        scoresheet.entries.add(entry1)
        scoresheet.entries.add(entry2)

        self.assertEquals(scoresheet.label, label)
