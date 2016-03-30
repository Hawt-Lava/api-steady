from api.steady.serializers.prompt_serializer import PromptSerializer
from api.steady.tests.base_test import BaseTest


class PromptSerializerTest(BaseTest):
    def test_serialization(self):
        data_dict = {"text": self.faker.sentence()}
        prompt_serializer = PromptSerializer(data=data_dict)
        self.assertTrue(prompt_serializer.is_valid())
