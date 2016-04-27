from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from api.steady.models.scoresheet import ScoreSheet
from api.steady.tests.base_test import BaseTest
from api.steady.tests.stubs.scoresheet_stub import ScoreSheetStub
from api.steady.tests.stubs.entry_stub import EntryStub
from api.steady.models.entry import Entry
from unittest import skip

class ScoreSheetSerializerTest(BaseTest):
    @skip
    def test_serialization(self):

        data_dict = ScoreSheetStub().generate()
        scoresheet_serializer = ScoreSheetSerializer(data=data_dict)
        #self.assertTrue(scoresheet_serializer.is_valid())
        scoresheet_serializer.is_valid()
        self.assertFalse(scoresheet_serializer.errors)
    @skip
    def test_creation_serialization(self):
        data_dict = ScoreSheetStub().generate()
        scoresheet_serializer = ScoreSheetSerializer()
        scoresheet = scoresheet_serializer.create(data_dict)
        self.assertEquals(len(ScoreSheet.objects.all()), 1)
        self.assertEquals(len(scoresheet.entries.all()), 2)
