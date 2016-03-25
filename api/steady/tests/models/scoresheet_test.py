from api.steady.tests.base_test import BaseTest
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry


class ScoresheetTest(BaseTest):
    def test_properties(self):
        scoresheet = ScoreSheet()
        label = self.faker.sentence()
        scoresheet.label = label
        entry1 = Entry()
        entry2 = Entry()
        scoresheet.entries = [entry1, entry2]
        self.assertEquals(scoresheet.label, label)
