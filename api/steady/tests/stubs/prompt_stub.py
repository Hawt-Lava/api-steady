from api.steady.tests/stubs.base_stub import BaseStub
class PromptStub(BaseStub):

    @staticmethod
    def generate():
        return {"text": self.faker.sentence()}

    @staticmethod
    def generate_existing():
        data = self.generate()
        data['id'] = self.faker.random_number()
        return data
