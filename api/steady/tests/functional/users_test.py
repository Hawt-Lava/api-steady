from api.steady.tests.base_test import BaseTest
from api.steady.models.user import User
from api.steady.tests.stubs.user_stub import UserStub


class UsersEndpointTest(BaseTest):
    def test_users_exists(self):
        response = self.client.get('/users')
        self.assertEquals(response.status_code, 200)

    def test_users_returns_list(self):
        number_of_users = 3
        i = 0
        while i < number_of_users:
            UserStub().generate_object().save()
            i += 1
        response = self.client.get('/users')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['count'], number_of_users)

    def test_post_success(self):
        data = UserStub().generate()
        response = self.client.post('/users', data)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['device_id'], data['device_id'])
