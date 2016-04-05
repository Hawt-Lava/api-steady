from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from api.steady.models.scoresheet import ScoreSheet
from api.steady.tests.base_test import BaseTest
from api.steady.tests.stubs.scoresheet_stub import ScoreSheetStub
from api.steady.tests.stubs.entry_stub import EntryStub
from api.steady.models.entry import Entry


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

    def test_can_reference_existing_entries(self):
        # Initialize 2 Entries

        entry1 = Entry.objects.create()
        entry2 = Entry.objects.create()

        scoresheet_stub = ScoreSheetStub().generate()
        scoresheet_stub.pop('entries')

        scoresheet_stub.entries = [
            {
                'id': entry1.id
            },
            {
                'id': entry2.id
            }

        ]
        scoresheet_serializer = ScoreSheetSerializer()
        print scoresheet_stub
        scoresheet = scoresheet_serializer.create(**scoresheet_stub)

        self.assertEquals(len(scoresheet.entries), 2)

