from selenium import webdriver 
from functional_tests.base import BaseFunctionalTest 
from selenium.webdriver.common.keys import Keys 


class BlogPostTest(BaseFunctionalTest):
    """
    Test that a User's interaction with a BlogPost's detail page
    provides the desired effects.
    """
    def get_a_blogpost_page(self):
        """
        A non-test method to retrieve a sample BlogPost detail page.
        """
        pass 

    def post_a_comment(blogpost_page, comment_data, user):
        pass 
        

    def test_blogpost_has_all_its_attributes(self):
        pass 


    def test_blog_post_has_a_category(self):
        # Belongs to a BlogCategory and links to it.
        # Category name is displayed and linked to
        pass

    def test_blogpost_page_has_list_of_comments(self):
        pass 

class BlogPostCommentsTest(BaseFunctionalTest):
    def test_blogpost_page_has_comments_form(self):
        pass 

    def test_only_authenticated_user_can_post_comments(self):
        pass 
    
    def test_non_staff_user_cannot_delete_comments(self):
        pass 

    def test_most_recent_comments_displayed_first(self):
        pass 

    def test_inactive_user_cannot_post_comments_on_a_blogpost(self):
        pass 

