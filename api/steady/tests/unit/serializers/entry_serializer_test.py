from api.steady.serializers.entry_serializer import EntrySerializer
from api.steady.tests.base_test import BaseTest


class EntrySerializerTest(BaseTest):
    def test_serialization(self):

        data_dict = {"score": 5, "prompt": {"text": self.faker.sentence()}}
        entry_serializer = EntrySerializer(data=data_dict)
        self.assertTrue(entry_serializer.is_valid())
