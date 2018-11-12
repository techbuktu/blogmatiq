from django.test import TestCase 
from unittest import skip
from django.http import HttpRequest 
from django.utils.html import escape 
from django.core.urlresolvers import resolve, reverse

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
    def setUp(self):
        """
        Needed to maintain DRY and house creation of instances of blogger app's models 
        (Blogger, Blog, BlogCategory, BlogPost and Comment) for use in the view unit tests.
        """
        blogger_data = {
            "bio": "I am a Blogger with 'views'. ;) "
        }
        self.blogger = self.create_mock_blogger(blogger_data)
        self.user = self.blogger.user 
        blog_info = {
            'name': 'Nomad',
            'desc': "This blog is all about traveling the world solo and in teams.",
            'owner': self.blogger
        }
        self.blog = self.create_mock_blog(blog_info)
        blog_category_info = {
            'name': 'Shepherds',
            'desc' : 'How do Shepherds live, breathe, make a living and go through life, one day at a time? Discover The Curious Life of Shepherds',
            'blog': self.blog
        }
        self.category = self.create_mock_blog_category(blog_category_info)
        blogpost_info = {
            'title': 'Life in the Hills of Fouta Djallon',
            'body': 'In the mountains and valleys of Fouta Djallon, ',
            'category': self.category
        }
        self.blog_post = self.create_mock_blogpost(blogpost_info)

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
    def test_blog_detail_page_resolves_to_blog_detail_view(self):
        res = resolve('/travelogue/')
        self.assertEqual(res.func, blog_detail)
    
    def test_view_renders_correct_html_template(self):
        response = self.client.get(self.blog.get_absolute_url())
        self.assertTemplateUsed(response, 'blogger/blog_detail.html')
    
    def test_template_is_passed_all_context_data_items(self):
        # Test for presence of each in .context dict
        response = self.client.get('/nomad/')
        self.assertIn('blog', response.context)
        self.assertIn('blog_categories', response.context)
        self.assertIn('blog_posts', response.context)
        self.assertIn('page_url', response.context)

    def test_that_view_redirects_to_comment_on_post_after_successful_POST_request(self):
        pass 

class BlogCategoryViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.blogcategory_detail() view
    """
    def test_view_resolves_to_correct_blog_category_url(self):
        res = resolve('/travelogue/tourism/')
        self.assertEqual(res.func, blog_category_detail)

    def test_views_uses_correct_html_template(self):
        blogger_data = {
            "bio": "I am a Blogger with 'views'. ;) "
        }
        blogger = self.create_mock_blogger(blogger_data)
        blog_info = {
            'name': 'Nomad',
            'desc': "This blog is all about traveling the world solo and in teams.",
            'owner': blogger
        }
        blog = self.create_mock_blog(blog_info)
        blog_category_info = {
            'name': 'Shepherds',
            'desc' : 'How do Shepherds live, breathe, make a living and go through life, one day at a time? Discover The Curious Life of Shepherds',
            'blog': blog
        }
        self.create_mock_blog_category(blog_category_info)
        response = self.client.get('/nomad/shepherds/')
        self.assertTemplateUsed(response, 'blogger/blog_category_detail.html')

    def test_view_passes_valid_context_data_to_template(self):
        blogger_data = {
            "bio": "I am a Blogger with 'views'. ;) "
        }
        blogger = self.create_mock_blogger(blogger_data)
        blog_info = {
            'name': 'Nomad',
            'desc': "This blog is all about traveling the world solo and in teams.",
            'owner': blogger
        }
        blog = self.create_mock_blog(blog_info)
        blog_category_info = {
            'name': 'Shepherds',
            'desc' : 'How do Shepherds live, breathe, make a living and go through life, one day at a time?',
            'blog': blog
        }
        self.create_mock_blog_category(blog_category_info)
        response = self.client.get('/nomad/shepherds/')
        self.assertIn('category', response.context)
        self.assertIn('category_posts', response.context)
    
    def test_template_renders_list_of_blog_posts_of_this_category(self):
        pass 

class BlogPostDetailViewTest(BaseViewTestCase):
    """
    Tests all aspects of the blogger.views.blogpost_detail() view.
    """
    def test_blogpost_detail_url_resolves_to_blogpost_detail_view(self):
        response = resolve('/travelogue/tourism/the-art-of-volunteerism/')
        self.assertEqual(response.func, blog_post_detail)

    def test_view_renders_correct_template(self):
        response = self.client.get(self.blog_post.get_absolute_url())
        self.assertTemplateUsed(response, 'blogger/blog_post_detail.html')

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
