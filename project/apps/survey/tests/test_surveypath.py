from utils.factory import Factory
from utils.test_helpers import skip, wip, ClearedTransactionTestCase


class SurveyPathTest(ClearedTransactionTestCase):

    def setUp(self):
        super(SurveyPathTest, self).setUp()
        self.survey_response = Factory.survey_response()

    @skip
    def test_claim_path(self):
        self.assertTrue("Written")