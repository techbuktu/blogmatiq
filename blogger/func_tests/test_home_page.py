from selenium import webdriver 
from functional_tests.base import BaseFunctionalTest
from selenium.webdriver.common.keys import Keys 


class HomePageVisitorTest(BaseFunctionalTest):

    def test_home_page_renders_correclty(self):
        # Maryam found out that her company has set up a mult-user blogging site for the team
        # She goes to check it to check out the home page.
        self.browser.get(self.live_server_url)

        # The home page title mentions 'Blogmatiq', the name of the blogging platform
        self.assertIn('Blogmatiq', self.browser.title)

        # She sees that there is a list of the current blogs on the site created by her colleagues
        blog_list_container = self.browser.find_element_by_id('list_of_blogs')
        self.assertContains(blog_list_container.text, 'List of Blogs')

        # Maryam notices that there is a list of blogs under this header
        blog_list = blog_list_container.find_elements_by_class_name('blog_item')
        #self.assertNotEqual(len(blog_list),0)


class StaticPagesTest(BaseFunctionalTest):
    def test_site_has_about_us_link(self):
        pass 

    def test_site_has_privacy_terms_link(self):
        pass 

    def test_has_contact_us_link(self):
        pass 

    def test_site_has_newsletter_page_link(self):
        pass 

class SiteNavHeaderTest(BaseFunctionalTest):
    def test_header_nav_has_blogs_link(self):
        pass

    def test_header_nav_has_registration_link(self):
        pass 

    def test_site_header_nav_has_login_logout_link(self):
        pass 


