from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from api.steady.models.scoresheet import ScoreSheet
from api.steady.tests.base_test import BaseTest
from api.steady.tests.stubs.scoresheet_stub import ScoreSheetStub
from api.steady.tests.stubs.entry_stub import EntryStub
from api.steady.models.entry import Entry
from api.steady.models.prompt import Prompt

class ScoreSheetSerializerTest(BaseTest):

    def test_serialization(self):

        data_dict = ScoreSheetStub().generate()
        scoresheet_serializer = ScoreSheetSerializer(data=data_dict)
        self.assertTrue(scoresheet_serializer.is_valid())
        self.assertFalse(scoresheet_serializer.errors)

    def test_creation_serialization(self):
        data_dict = ScoreSheetStub().generate()
        prompt_id = data_dict['entries'][0]['prompt']
        prompt = Prompt.objects.get(id=prompt_id)
        data_dict['entries'][0]['prompt'] = prompt

        prompt_id_2 = data_dict['entries'][1]['prompt']
        prompt2 = Prompt.objects.get(id=prompt_id_2)
        data_dict['entries'][1]['prompt'] = prompt2
        scoresheet_serializer = ScoreSheetSerializer()
        scoresheet = scoresheet_serializer.create(data_dict)
        self.assertEquals(len(ScoreSheet.objects.all()), 1)
        self.assertEquals(len(scoresheet.entries.all()), 2)
