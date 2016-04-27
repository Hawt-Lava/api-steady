from api.steady.models.user import User
from api.steady.tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_properties(self):
        user = User()
        device_id = self.faker.sentence()
        user.device_id = device_id
        self.assertEquals(user.device_id, device_id)
