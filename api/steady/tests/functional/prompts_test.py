from api.steady.tests.base_test import BaseTest
from api.steady.models.prompt import Prompt
from api.steady.tests.stubs.prompt_stub import PromptStub


class PromptsEndpointTest(BaseTest):
    def test_prompts_exists(self):
        response = self.client.get('/prompts')
        self.assertEquals(response.status_code, 200)

    def test_prompts_returns_list(self):
        number_of_prompts = 3
        i = 0
        while i < number_of_prompts:
            PromptStub().generate_object().save()
            i += 1
        response = self.client.get('/prompts')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['count'], number_of_prompts)

    def test_post_success(self):
        data = PromptStub().generate()
        response = self.client.post('/prompts', data)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.data['text'], data['text'])
