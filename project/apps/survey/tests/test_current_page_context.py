from utils.test_helpers import skip, wip, ClearedTransactionTestCase
from utils.factory import Factory


class CurrentPageContextTest(ClearedTransactionTestCase):

    def setUp(self):
        super(CurrentPageContextTest, self).setUp()
        self.survey_response = Factory.survey_response()
