from api.steady.tests.base_test import BaseTest
from api.steady.models.entry import Entry
from api.steady.tests.stubs.entry_stub import EntryStub
from rest_framework.test import APIClient


class EntriesEndpointTest(BaseTest):
    def test_entries_enpoint_exists(self):
        response = self.client.get('/entries')
        self.assertEquals(response.status_code, 200)

    def test_entries_returns_list(self):
        number_of_entries = 4
        i = 0
        while i < number_of_entries:
            EntryStub().generate_object().save()
            i += 1
        response = self.client.get('/entries')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['count'], number_of_entries)

    def test_entries_success(self):
        data = EntryStub().generate()
        response = self.client.post('/entries', data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['score'], data['score'])
