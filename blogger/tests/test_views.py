from django.test import TestCase 
from django.http import HttpRequest 
from django.utils.html import escape 
from django.core.urlresolvers import resolve 

from blogger.models import (
    Blogger, Blog, BlogCategory, BlogPost, Comment
)
from blogger.views import (
    home, about, contact, newsletter, blog_detail, legal_terms, comment_on_post,
    blog_category_detail, blog_post_detail
    )
from blogger.tests.base import BaseBloggerAppUnitTestCase


class BaseViewTestCase(BaseBloggerAppUnitTestCase):
    """
    Base View Unit TestCase for blogger.views and 
    holds all common methods across all view Unit TestCases
    """

def post_invalid_data(self, data, target_url):
    return self.client.post(target_url, data=data)

def force_login(self, user):
    """
    A shortcut method to simulate a user login but the details 
    of how a user is logged in are not important.
    """
    return self.client.force_login(user)

def login(self, auth_credentials):
    """
    Logs in a user with the provided username and password credentials.
    """
    return self.login(auth_credentials)


class HomeViewTest(BaseViewTestCase):
    """
    Tests that all aspects of the blogger.views.home() view are correct, proper and valid.
    """
    def test_uses_blogger_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blogger/index.html')

    def test_has_blog_list_in_context_data(self):
        response = self.client.get('/')
        self.assertIn('blog_list', response.context)

    def test_home_view_resolves_to_home_page_url(self):
        response = resolve('/')
        self.assertEqual(response.func, home)

class AboutViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.about() view.
    """
    def test_view_uses_correct_about_template(self):
        pass 

    def test_context_data_has_about_value(self):
        pass 

    def test_view_resolves_to_correct_about_us_url(self):
        pass 

class ContactViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.contact() view.
    """
    def test_contact_view_resolves_to_correct_url(self):
        pass 

    def test_contact_page_uses_correct_html_template(self):
        pass 

    def test_view_passes_correct_context_data(self):
        # Test for each in the .context dict
        pass 

    def test_template_is_passed_a_contact_form(self):
        pass 

    def test_can_save_a_valid_POST_request(self):
        pass 

    def test_view_redirects_to_thank_you_page_after_valid_POST_request(self):
        pass 

    
class NewsletterViewTest(BaseViewTestCase):
    """
    Tests all units of the blogger.views.newsletter() view 
    """
    def test_view_resolves_to_correct_newsletter_url(self):
        pass 

    def test_view_passes_correct_context_data_to_template(self):
        pass 

    def test_view_renders_correct_html_template(self):
        pass 

class BlogDetailViewTest(BaseViewTestCase):
    """
    Tests all units of the blogger.views.blog_detail() view.
    """
    def setUp(self):
        """
        Setup the blogger.views.blog_detail() view by setting up
        a sample Blog() to work with.
        """
        blogger_data = {
            "bio": "I am a Blogger with 'views'. ;) "
        }
        self.blogger = self.create_mock_blogger(blogger_data)

    def test_resolves_to_correct_blog_detail_url(self):
        pass 

    def test_view_renders_correct_html_template(self):
        pass 

    def test_template_renders_all_context_data_items(self):
        # Test for presence of each in .context dict
        pass 

    def test_that_view_redirects_to_comment_on_post_after_successful_POST_request(self):
        pass 

class BlogCategoryViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.blogcategory_detail() view
    """
    def test_view_resolves_to_correct_blog_category_url(self):
        pass 

    def test_views_uses_correct_html_template(self):
        pass 

    def test_view_passes_valid_context_data_to_template(self):
        pass

    def test_context_data_contains_list_of_categorys_blog_posts(self):
        pass 

    def test_template_renders_list_of_blog_posts_of_this_category(self):
        pass 

class BlogPostDetailViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.blogpost_detail() view.
    """
    def test_blogpost_detail_url_resolves_to_blogpost_detail_view(self):
        pass 

    def test_view_renders_correct_template(self):
        pass 

    def test_blogpost_detail_view_passes_valid_context_data_to_template(self):
        pass 
    
class LegalTermsViewTest(BaseViewTestCase):
    """
    Tests all granular units of the blogger.views.legal_terms() view.
    """
    def test_view_resolves_to_correct_url(self):
        pass 

    def test_view_uses_correct_html_template(self):
        pass 
    
    def test_template_renders_legal_terms_context_data(self):
        pass 

class CommentOnPostViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.comment_on_post() view.
    """
    def test_commenter_is_not_an_anonymous_user(self):
        pass 

    def test_comment_is_not_a_duplicate(self):
        pass 

    def test_commenter_is_automatically_derived_from_logged_user(self):
        pass 
