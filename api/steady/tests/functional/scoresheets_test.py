from api.steady.tests.base_test import BaseTest
from api.steady.tests.stubs.scoresheet_stub import ScoreSheetStub
from api.steady.tests.stubs.entry_stub import EntryStub


class ScoreSheetEndpointTest(BaseTest):
    def test_scoresheet_enpoint_exists(self):
        response = self.client.get('/scoresheets')
        self.assertEquals(response.status_code, 200)

    def test_scoresheets_returns_list(self):
        number_of_scoresheets = 4
        i = 0
        while i < number_of_scoresheets:
            ScoreSheetStub().generate_object().save()
            i += 1
        response = self.client.get('/scoresheets')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['count'], number_of_scoresheets)

    def test_device_id_filter(self):
        number_of_scoresheets = 1
        i = 0
        current_scoresheet = ''
        while i < number_of_scoresheets:
            current_scoresheet = ScoreSheetStub().generate_object()
            current_scoresheet.save()
            i += 1
        response = self.client.get('/scoresheets?device_id={0}'.format(current_scoresheet.device_id))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['count'], 1)
        self.assertEquals(response.data['results'][0]['device_id'], current_scoresheet.device_id)

    def test_scoresheets_post(self):
        data = ScoreSheetStub().generate()
        response = self.client.post('/scoresheets', data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['device_id'], data['device_id'])
        self.assertEquals(response.data['entries'][0]['score'],
                          data['entries'][0]['score'])
