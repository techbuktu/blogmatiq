from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 

class BaseFunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def go_to_page(self, page):
        """
        Shortcut utility method to fetch any page with the self.live_server_url 
        """
        return self.browser.get(self.live_server_url + page)

    def logout_user(self):
        """
        Utitlity FT method to logout a user no matter which page he/she is on.
        """
        logout_button = self.browser.find_element_by_id('logout')
        logout_button.click()
        self.browser.refresh()

    def wait_for(self, seconds):
        """
        Concise method for how long to wait for browser to load ... in seconds.
        """
        if seconds < 0:
            return self.browser.implicitly_wait(5)
        return self.browser.implicitly_wait(seconds)

    def login_user(self, auth_creds):
        username = auth_creds['username']
        password = auth_creds['password']
        username_input_box = self.browser.find_element_by_id('username')
        password_input_box = self.browser.find_element_by_id('password')
        login_button = self.browser.find_element_by_id('login')
        username_input_box.send_keys(username)
        password_input_box.send_keys(password)
        login_button.click()

    
    

    

    