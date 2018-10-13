from django.test import TestCase 
from django.http import HttpRequest 
from django.utils.html import escape 
from django.core.urlresolvers import resolve 

from blogger.models import (
    Blogger, Blog, BlogCategory, BlogPost, Comment
)
from blogger.views import (
    home, about, contact, newsletter, blog_detail, legal_terms, comment_on_post
    )

class HomeViewTest(TestCase):
    """
    Tests that all aspects of the blogger.views.home() view are correct, proper and valid.
    """
    def test_uses_blogger_index_template(self):
        pass 

    def test_has_blog_list_in_context_data(self):
        pass 

    def test_home_view_resolves_to_home_page_url(self):
        pass 

class AboutViewTest(TestCase):
    """
    Tests all aspects of the blogger.views.about() view.
    """
    def test_view_uses_correct_about_template(self):
        pass 

    def test_context_data_has_about_value(self):
        pass 

    def test_view_resolves_to_correct_about_us_url(self):
        pass 

class ContactViewTest(TestCase):
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

    
class NewsletterViewTest(TestCase):
    """
    Tests all units of the blogger.views.newsletter() view 
    """
    def test_view_resolves_to_correct_newsletter_url(self):
        pass 

    def test_view_passes_correct_context_data_to_template(self):
        pass 

    def test_view_renders_correct_html_template(self):
        pass 

class BlogDetailViewTest(TestCase):
    """
    Tests all units of the blogger.views.blog_detail() view.
    """
    def test_resolves_to_correct_blog_detail_url(self):
        pass 

    def test_view_renders_correct_html_template(self):
        pass 

    def test_template_renders_all_context_data_items(self):
        # Test for presence of each in .context dict
        pass 

    def test_that_view_redirects_to_comment_on_post_after_successful_POST_request(self):
        pass 

class BlogCategoryViewTest(TestCase):
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

class LegalTermsViewTest(TestCase):
    """
    Tests all granular units of the blogger.views.legal_terms() view.
    """
    def test_view_resolves_to_correct_url(self):
        pass 

    def test_view_uses_correct_html_template(self):
        pass 
    
    def test_template_renders_legal_terms_context_data(self):
        pass 

class CommentOnPostViewTest(TestCase):
    """
    Tests all aspects of the blogger.views.comment_on_post() view.
    """
    def test_commenter_is_authenticated(self):
        pass 

    def test_comment_is_not_a_duplicate(self):
        pass 