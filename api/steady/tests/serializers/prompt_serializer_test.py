from api.steady.models.prompt import Prompt
from api.steady.serializers.prompt_serializer import PromptSerializer
from api.steady.tests.base_test import BaseTest

import json


class PromptSerializerTest(BaseTest):

    def test_serialization(self):
        data_dict = {"text": "Fooo"}
        data = json.dumps(data_dict)
        prompt_serializer = PromptSerializer(data=data)
        self.assertTrue(prompt_serializer.is_valid())
