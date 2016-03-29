from api.steady.tests.stubs.base_stub import BaseStub
from api.steady.tests.stubs.prompt_stub import PromptStub


class EntryStub(BaseStub):
    @staticmethod
    def generate():
        score = self.random_number()
        prompt = PromptStub.generate()
        return {"score": score, "prompt": prompt}

    @staticmethod
    def generate_existing():
        data = self.generate()
        data['id'] = self.random_number()
        data['prompt'] = PromptStub.generate_existing()
        return data
