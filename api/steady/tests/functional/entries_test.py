from api.steady.tests.base_test import BaseTest
from api.steady.models.entry import Entry

from rest_framework.test import APIClient

class EntriesEndpointTest(BaseTest):
    def test_entries_enpoint_exists(self):
        response = self.client.get('/entries')
        self.assertEquals(response.status_code, 200)

    def test_entries_returns_list(self):
        number_of_entries = 4
        i = 0
        while i < number_of_entries:
            Entry(score=i, prompt=Prompt(text=self.faker.sentence())).save()
            i += 1
        response = self.client.get('/entries')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['count'], number_of_entries)

    def test_entries_success(self):
        data = {'text': self.faker.sentence()}
        response = self.client.post('/entries', data)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['text'], data['text'])

