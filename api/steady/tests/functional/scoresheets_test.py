from api.steady.tests.base_test import BaseTest
from api.steady.tests.stubs.scoresheet_stub import ScoreSheetStub


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

    def test_scoresheets_post(self):
        data = ScoreSheetStub().generate()

        import pprint
        pprint.pprint(data)

        response = self.client.post('/scoresheets', data, format='json')
        print ("MADE IT HERE")
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['label'], data['label'])
