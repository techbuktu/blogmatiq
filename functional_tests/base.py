from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 

class BaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def go_to_page(self, page):
        return self.browser.get(self.live_server_url + page)

    def 