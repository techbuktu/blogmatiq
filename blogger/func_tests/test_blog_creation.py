from selenium import webdriver 
from functional_tests.base import BaseFunctionalTest
from selenium.webdriver.common.keys import Keys 


class HomePageTest(BaseFunctionalTest):

    def test_home_page_has_site_title(self):
        # Maryam found out that her company has set up a mult-user blogging site for the team
        # She goes to check it to check out the home page.
        self.browser.get(self.live_server_url)

        # The home page title mentions 'Blogmatiq', the name of the blogging platform
        self.assertIn('Blogmatiq', self.browser.title)

        # She sees that there is a list of the current blogs on the site created by her colleagues
        blog_list_header = self.browser.find_element_by_id('list_of_blogs')
        self.assertIn('List of Blogs', blog_list_header.text)

        