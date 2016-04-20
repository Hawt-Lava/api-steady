from api.steady.serializers.user_serializer import UserSerializer 
from api.steady.tests.base_test import BaseTest 

class UserSerializerTest(BaseTest):
    def test_serialization(self):
        data_dict = {"device_id": self.random_number()}
        user_serializer = UserSerializer(data=data_dict)
        self.assertTrue(user_serializer.is_valid())
