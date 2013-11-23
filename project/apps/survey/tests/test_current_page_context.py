from django.test import TestCase
from utils.factory import Factory


class CurrentPageContextTest(TestCase):

    def setUp(self):
        self.survey_response = factory.survey_response()

    def test_context_returns_a_dict(self):
        self.assertEquals(type({}), type)