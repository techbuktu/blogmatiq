from selenium import webdriver 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from django.contrib.auth.models import User 

class BaseFunctionalTest(StaticLiveServerTestCase):
    def create_user(self):
        user = User.objects.create(username="muhammad", is_staff=True, first_name="Muhammad",
        last_name="Jalloh")
        user.set_password("S3CReT123")
        user.save()
        return user 

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

    def get_object_owner(self, owner_element_id):
        return self.browser.find_element_by_id(owner_element_id)

    def get_list_container(self, list_class_name):
        list_of_elements = self.browser.find_elements_by_class_name(list_class_name)
        return list_of_elements

    def item_in_list_container(list_class_name, item_position):
        """
        Shortcut method for retrieving an item of <item_position>
        from a list of similar items in the <list_class_name> container.
        """
        list_of_elements = self.browser.find_elements_by_class_name(list_class_name)
        return list_of_elements[item_position]

    def get_comment_form(self):
        """
        A utilty/shortcut method to fetch the #comment_form 
        container on a page.
        """
        comment_form = self.browser.fin_element_by_id('comment_form')
        return comment_form 

    

