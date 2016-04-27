from api.steady.serializers.entry_serializer import EntrySerializer
from api.steady.tests.base_test import BaseTest
from api.steady.models.prompt import Prompt


class EntrySerializerTest(BaseTest):
    def test_serialization(self):
        prompt = Prompt(text=self.faker.sentence)
        prompt.save()
        data_dict = {"score": 5, "prompt": prompt.id}
        entry_serializer = EntrySerializer(data=data_dict)
        entry_serializer.is_valid()
        self.assertFalse(entry_serializer.errors)
        self.assertTrue(entry_serializer.is_valid())
