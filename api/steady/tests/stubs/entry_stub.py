from api.steady.tests.stubs.base_stub import BaseStub
from api.steady.tests.stubs.prompt_stub import PromptStub
from api.steady.models.entry import Entry


class EntryStub(BaseStub):
    def generate(self):
        score = self.random_number()
        prompt = PromptStub().generate()
        return {"score": score, "prompt": prompt}

    def generate_existing(self):
        data = self.generate()
        data['id'] = self.random_number()
        data['prompt'] = PromptStub().generate_existing()
        return data

    def generate_object(self):
        data = self.generate()
        prompt = PromptStub().generate_object()
        prompt.save()
        data['prompt'] = prompt
        return Entry(**data)
