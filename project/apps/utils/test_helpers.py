from django.core.urlresolvers import reverse
from django.test import LiveServerTestCase

from nose.plugins.attrib import attr
from splinter.browser import Browser


@attr('e2e')
class E2ETestCase(LiveServerTestCase):
    def setUp(self, *args, **kwargs):
        super(E2ETestCase, self).setUp(*args, **kwargs)
        self.browser = Browser('phantomjs')

    def tearDown(self, *args, **kwargs):
        self.browser.quit()
        super(E2ETestCase, self).tearDown(*args, **kwargs)

    def visit(self, url):
        try:
            url = reverse(url)
        except:
            pass
        self.browser.visit("%s%s" % (self.live_server_url, url))


wip = attr("wip")
