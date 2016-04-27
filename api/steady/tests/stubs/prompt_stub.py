from api.steady.tests.stubs.base_stub import BaseStub
from api.steady.models.prompt import Prompt


class PromptStub(BaseStub):
    def generate(self):
        return {"text": self.faker.sentence()}

    def generate_existing(self):
        data = self.generate()
        data['id'] = self.random_number()
        return data

    def generate_object(self):
        prompt = Prompt(**self.generate())
        prompt.save()
        return prompt
