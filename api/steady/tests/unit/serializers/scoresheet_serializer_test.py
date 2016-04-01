from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from api.steady.models.scoresheet import ScoreSheet
from api.steady.tests.base_test import BaseTest
from api.steady.tests.stubs.scoresheet_stub import ScoreSheetStub


class ScoreSheetSerializerTest(BaseTest):
    def test_serialization(self):

        data_dict = ScoreSheetStub().generate()
        scoresheet_serializer = ScoreSheetSerializer(data=data_dict)
        self.assertTrue(scoresheet_serializer.is_valid())

    def test_creation_serialization(self):
        data_dict = ScoreSheetStub().generate()
        scoresheet_serializer = ScoreSheetSerializer()
        scoresheet = scoresheet_serializer.create(data_dict)
        self.assertEquals(len(ScoreSheet.objects.all()), 1)
        self.assertEquals(len(scoresheet.entries.all()), 2)
