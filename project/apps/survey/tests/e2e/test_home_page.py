from utils.test_helpers import E2ETestCase, wip
from django.core.urlresolvers import reverse


class HomePageTest(E2ETestCase):

    def test_home_page_gives_invalid_code_with_no_code(self):
        self.visit(reverse("survey:entrance"))
        self.browser.is_text_present("Sorry!")

    def test_home_page_says_welcome_with_code(self):
        self.visit("%s?survey_id=1234&exit_url=foo.com" % reverse("survey:entrance"))
        self.browser.is_text_present("Welcome")

    def test_home_page_remembers_code_after_reload(self):
        self.visit("%s?survey_id=1234&exit_url=foo.com" % reverse("survey:entrance"))
        self.browser.is_text_present("Welcome")

        self.browser.reload()
        self.browser.is_text_present("Welcome")

        self.visit("survey:entrance")
        self.browser.is_text_present("Welcome")
