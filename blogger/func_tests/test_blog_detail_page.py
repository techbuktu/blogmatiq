from selenium import webdriver 
from functional_tests.base import BaseFunctionalTest 
from selenium.webdriver.common.keys import Keys 


class BlogOwnerTest(BaseFunctionalTest):
    """
    Tests a User's interaction with the blog detail page.
    """

    def test_blog_has_link_to_owner(self):
        self.fail("Implement me! ")

class BlogDetailTest(BaseFunctionalTest):
    """
    Test that a Blog has all the right attributes/components 
    """
    def test_blog_has_all_its_attributes(self):
        pass 

    def test_blog_detail_page_has_list_of_categories(self):
        pass 

    def test_blog_has_list_of_recent_blog_posts(self):
        pass 

