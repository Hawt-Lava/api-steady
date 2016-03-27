from api.steady.serializers.scoresheet_serializer import ScoreSheetSerializer
from api.steady.tests.base_test import BaseTest


class ScoreSheetSerializerTest(BaseTest):
    def test_serialization(self):

        data_dict = {
            "label": self.faker.sentence(),
            "entries": [{
                "score": 5,
                "prompt": {
                    "text": self.faker.sentence()
                }
            }, {
                "score": 2,
                "prompt": {
                    "text": self.faker.sentence()
                }
            }, {
                "score": 8,
                "prompt": {
                    "text": self.faker.sentence()
                }
            }]
        }
        scoresheet_serializer = ScoreSheetSerializer(data=data_dict)
        self.assertTrue(scoresheet_serializer.is_valid())
