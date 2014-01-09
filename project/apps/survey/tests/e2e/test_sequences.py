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
            self.assertIn("Health State #%s" % i, self.ele("h1").text)
            self.assertEquals(self.ele("h2").text, "Introduction")
            selector = ".hs_%s" % getattr(self.survey_path_1, "state_%s" % i)
            assert self.browser.is_element_present_by_css(selector)
            self.ele(".next_button").click()
            self.assertIn("Health State #%s" % i, self.ele("h1").text)
            self.assertEquals(self.ele("h2").text, "Video")
            self.sleep(7)  # Wait for super slow video to finish.
            self.ele(".next_button").click()
            self.assertIn("Health State #%s" % i, self.ele("h1").text)
            self.assertEquals(self.ele("h2").text, "Vertical Scale")
            self.ele("#id_vas_rating").fill(Factory.rand_int())
            self.ele(".next_button").click()
            self.assertIn("Health State #%s" % i, self.ele("h1").text)
            self.assertEquals(self.ele("h2").text, "Timeline")
            self.ele("#id_tto_rating").fill(Factory.rand_int())
            self.ele(".timeline.top").click()
            self.ele(".next_button").click()
            self.assertIn("Health State #%s" % i, self.ele("h1").text)
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

        self.assertIn("Health State #1", self.ele("h1").text)
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

        self.assertIn("Health State #1", self.ele("h1").text)
        assert self.browser.is_element_present_by_css(".hs_%s" % self.survey_path_2.state_1)
