from django.test import TestCase
from utils.test_helpers import E2ETestCase, wip, skip
from utils.factory import Factory


class CurrentPageContextTest(TestCase):

    def setUp(self):
        self.survey_response = Factory.survey_response()

    def test_context_returns_a_dict(self):
        self.assertEquals(type({}), type(self.survey_response.current_page_context))
