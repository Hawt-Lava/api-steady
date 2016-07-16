from api.steady.tests.stubs.base_stub import BaseStub
from api.steady.models.user import User


class UserStub(BaseStub):
    def generate(self):
        return {"device_id": self.faker.sentence()}

    def generate_existing(self):
        data = self.generate()
        data['id'] = self.random_number()
        return data

    def generate_object(self):
        user = User(**self.generate())
        user.save()
        return user
