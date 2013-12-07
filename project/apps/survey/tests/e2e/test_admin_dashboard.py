from utils.factory import Factory
from utils.test_helpers import E2ETestCase, wip
from django.core.urlresolvers import reverse


class AdminDashboardTest(E2ETestCase):

    def test_dashboard_loads(self):
        user, password = Factory.user(is_admin=True)
        self.visit(reverse("survey:admin_dashboard"))

        # Log in
        self.sleep(1)
        self.ele("#id_username").fill(user.username)
        self.ele("#id_password").fill(password)
        self.sleep(0.1)
        self.ele("input[type=submit]").click()

        assert self.browser.is_text_present("Admin Dashboard", wait_time=10)

    def test_dashboard_404s_for_non_admins(self):
        user, password = Factory.user()
        self.visit(reverse("survey:admin_dashboard"))

        # Log in
        self.sleep(1)
        self.ele("#id_username").fill(user.username)
        self.ele("#id_password").fill(password)
        self.sleep(0.1)
        self.ele("input[type=submit]").click()

        assert not self.browser.is_text_present("Admin Dashboard", wait_time=10)
        assert self.browser.is_element_present_by_css("#id_username")