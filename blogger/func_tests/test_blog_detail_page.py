from selenium import webdriver 
from functional_tests.test_blog import BloggerAppFunctionalTest
from selenium.webdriver.common.keys import Keys 


class BlogOwnerTest(BloggerAppFunctionalTest):
    """
    Tests a User's interaction with the blog detail page.
    """

    def test_blog_has_link_to_owner(self):
        pass 

class BlogDetailPageTest(BloggerAppFunctionalTest):
    """
    Test that a Blog Page has all the right components 
    that a site visitor would expect it to have and be
    able to interact with it.
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.create_user()
        blogger_dict = {
            "bio": "I am (what you would call) an accomplished 'Bloglite.'"
        }
        self.user = self.create_user()
        self.blogger = self.create_blogger(blogger_dict)
        blog_dict = {
            'name': 'Travelogue', 
            'desc': 'Wherein I explore global cultures and cuisine.', 
        }
        self.blog = self.create_a_blog(blog_dict)

    def test_blog_has_all_its_attributes(self):
        self.go_to_page('/travelogue')
        self.assertIn('travelogue', self.browser.current_url)

    def test_blog_detail_page_has_list_of_categories(self):
        pass 

    def test_blog_has_list_of_recent_blog_posts(self):
        pass 

