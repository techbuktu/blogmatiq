from selenium import webdriver 
from selenium import webdriver 
from functional_tests.base import BaseFunctionalTest
from functional_tests.test_blog import BloggerAppFunctionalTest
from selenium.webdriver.common.keys import Keys 


class HomePageVisitorTest(BloggerAppFunctionalTest):
    def setUp(self):
        self.browser = webdriver.Firefox()
        blog1 = {
            'name': 'Travelogue', 
            'desc': 'Wherein I explore global cultures and cuisine.', 
        }
        blog2 = {
            'name': 'Technocrat', 
            'desc':"Let's talk about code and this code life!"
        }
        blogger1 = {
            "bio": "I am (what you would call) an accomplished 'Bloglite.'"
        }
        self.create_user()
        self.create_blogger(blogger1)
        self.blog_one = self.create_a_blog(blog1)
        self.blog_two = self.create_a_blog(blog2)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_renders_correclty(self):
        # Maryam found out that her company has set up a mult-user blogging site for the team
        # She goes to check it to check out the home page.
        self.browser.get(self.live_server_url)

        # The home page title mentions 'Blogmatiq', the name of the blogging platform
        self.assertIn('Blogmatiq', self.browser.title)

        # She sees that there is a list of the current blogs on the site created by her colleagues
        blog_list_container = self.browser.find_element_by_id('list_of_blogs')
        self.assertIn('List of Blogs', blog_list_container.text)

        # Maryam notices that there is a list of blogs under this header
        self.wait_for(5)
        blog_list = self.browser.find_elements_by_class_name('blog_item')
        print(len(blog_list))
        self.assertNotEqual(len(blog_list),0)


class StaticPagesLinksTest(BaseFunctionalTest):
    def get_footer(self):
        self.browser.get(self.live_server_url)
        return self.browser.find_element_by_tag_name('footer')
    
    def test_site_has_about_us_link(self):
        footer = self.get_footer()
        about_us_link = footer.find_element_by_link_text('About Us')
        self.assertEqual('About Us', about_us_link.text)

    def test_site_has_privacy_terms_link(self):
        footer = self.get_footer()
        privacy_link = footer.find_element_by_partial_link_text('Privacy')
        self.assertIn('Terms', privacy_link.text)

    def test_has_contact_us_link(self):
        footer = self.get_footer()
        contact_link = footer.find_element_by_partial_link_text('Contact')
        self.assertEqual('Contact Us', contact_link.text)

    def test_site_has_newsletter_page_link(self):
        footer = self.get_footer()
        newsletter_link = footer.find_element_by_link_text('Newsletter')
        self.assertEqual('Newsletter', newsletter_link.text)

class SiteNavHeaderTest(BaseFunctionalTest):
    def test_header_nav_has_blogs_link(self):
        pass

    def test_header_nav_has_registration_link(self):
        pass 

    def test_site_header_nav_has_login_logout_link(self):
        pass 


