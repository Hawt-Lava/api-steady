from api.steady.tests.stubs.base_stub import BaseStub
from api.steady.tests.stubs.entry_stub import EntryStub
from api.steady.models.scoresheet import ScoreSheet
from api.steady.models.entry import Entry


class ScoreSheetStub(BaseStub):
    def generate(self):
        device_id = self.faker.sentence()
        entry1 = EntryStub().generate()
        entry2 = EntryStub().generate()
        return {"device_id": device_id, "entries": [entry1, entry2]}

    def generate_existing(self):
        data = self.generate()
        data['id'] = self.random_number()
        data['entries'] = [EntryStub().generate_existing(),
                           EntryStub().generate_existing()]
        return data

    def generate_object(self):
        data = self.generate()
        data.pop("entries")

        entry = EntryStub().generate_object()
        entry2 = EntryStub().generate_object()
        entry.save()
        entry2.save()

        scoresheet = ScoreSheet(**data)
        scoresheet.save()

        scoresheet.entries.add(entry, entry2)

        return scoresheet
