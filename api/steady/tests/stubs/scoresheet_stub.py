from api.steady.tests.stubs.base_stub import BaseStub
from api.steady.tests.stubs.prompt_stub import PromptStub
from api.steady.tests.stubs.entry_stub import EntryStub


class ScoreSheetStub(BaseStub):
    @staticmethod
    def generate():
        label = self.faker.sentence()
        entry1 = EntryStub.generate()
        entry2 = EntryStub.generate()
        return {"label": label, "entries": [entry1, entry2]}

    @staticmethod
    def generate_existing():
        data = self.generate()
        data['id'] = self.random_number()
        data['entries'] = [EntryStub.generate_existing(), EntryStub.generate_existing()]
        return data
