from utils.test_helpers import skip, wip, ClearedTransactionTestCase
from utils.factory import Factory


class CurrentPageContextTest(ClearedTransactionTestCase):

    def setUp(self):
        super(CurrentPageContextTest, self).setUp()
        self.survey_response = Factory.survey_response()

    def test_context_returns_a_dict(self):
        self.assertEquals(type({}), type(self.survey_response.current_page_context))
