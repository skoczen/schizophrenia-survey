from django.test import TransactionTestCase
from utils.factory import Factory
from utils.test_helpers import skip


class SurveyPathTest(TransactionTestCase):

    def setUp(self):
        self.survey_response = Factory.survey_response()

    @skip
    def test_claim_path(self):
        self.assertTrue("Written")