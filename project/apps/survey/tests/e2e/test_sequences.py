from utils.test_helpers import E2ETestCase, wip, skip
from django.core.urlresolvers import reverse
from django.core.cache import cache
from utils.factory import Factory
from survey.models import NEXT_SURVEY_PATH_KEY


class HomePageTest(E2ETestCase):

    def setUp(self, *args, **kwargs):
        super(HomePageTest, self).setUp(*args, **kwargs)
        cache.delete(NEXT_SURVEY_PATH_KEY)
        self.survey_path_1 = Factory.survey_path(order=1)
        self.survey_path_2 = Factory.survey_path(order=2)

    def test_first_sequence_is_picked_and_advances_in_order(self):
        self.visit("%s?survey_id=1234&exit_url=foo.com" % reverse("survey:entrance"))
        # This never happens because the test browser reloads the page. Ridiculous.
        # self.assertEquals(self.ele("h1").text, "Welcome.")
        # self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_1)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_2)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_3)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_4)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_5)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_6)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_7)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_8)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "All done!")

    def test_sequences_go_through_correctly(self):
        self.visit("%s?survey_id=1234&exit_url=foo.com" % reverse("survey:entrance"))
        # self.browser.is_text_present("Welcome!")
        # self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_1)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_2)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_1.state_3)

        self.browser.cookies.delete()
        self.visit("survey:temp_logout")
        self.visit("%s?survey_id=1235&exit_url=foo.com" % reverse("survey:entrance"))
        # self.browser.is_text_present("Welcome!")
        # self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_2.state_1)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_2.state_2)

        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Health State #%s" % self.survey_path_2.state_3)
