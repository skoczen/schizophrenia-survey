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
        self.assertEquals(self.ele("h1").text, "Welcome.")
        self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "Basic Information")
        self.ele("#id_age").fill(Factory.rand_int())
        self.ele("#id_education").select("Some high school")
        self.ele("#id_household_income").select("20,000-40,000")
        self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "Introduction")
        self.ele(".next_button").click()

        for i in range(1, 9):
            self.assertEquals(self.ele("h1").text, "Health State #%s" % i)
            self.assertEquals(self.ele("h2").text, "Introduction")
            selector = ".hs_%s" % getattr(self.survey_path_1, "state_%s" % i)
            assert self.browser.is_element_present_by_css(selector)
            self.ele(".next_button").click()
            self.assertEquals(self.ele("h1").text, "Health State #%s" % i)
            self.assertEquals(self.ele("h2").text, "Video")
            self.ele(".next_button").click()
            self.assertEquals(self.ele("h1").text, "Health State #%s" % i)
            self.assertEquals(self.ele("h2").text, "Vertical Scale")
            self.ele(".next_button").click()
            self.assertEquals(self.ele("h1").text, "Health State #%s" % i)
            self.assertEquals(self.ele("h2").text, "Time Trade-off")
            self.ele(".next_button").click()
            self.assertEquals(self.ele("h1").text, "Health State #%s" % i)
            self.assertEquals(self.ele("h2").text, "Transition")
            self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "All done!")

    def test_sequences_go_through_correctly(self):
        self.visit("%s?survey_id=1234&exit_url=foo.com" % reverse("survey:entrance"))
        self.ele(".next_button").click()

        self.ele("#id_age").fill(Factory.rand_int())
        self.ele("#id_education").select("Some high school")
        self.ele("#id_household_income").select("20,000-40,000")
        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Introduction")
        self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "Health State #1")
        assert self.browser.is_element_present_by_css(".hs_%s" % self.survey_path_1.state_1)

        self.browser.cookies.delete()
        self.visit("survey:temp_logout")
        self.ele(".next_button").click()

        self.ele("#id_age").fill(Factory.rand_int())
        self.ele("#id_education").select("Some high school")
        self.ele("#id_household_income").select("20,000-40,000")
        self.ele(".next_button").click()
        self.assertEquals(self.ele("h1").text, "Introduction")
        self.ele(".next_button").click()

        self.assertEquals(self.ele("h1").text, "Health State #1")
        assert self.browser.is_element_present_by_css(".hs_%s" % self.survey_path_2.state_1)
