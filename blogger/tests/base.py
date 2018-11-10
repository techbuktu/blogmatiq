from django.test import TestCase 
from unittest import skip
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
from django.utils import timezone 
from blogger.models import (
    Blogger, Blog, BlogCategory, BlogPost, Comment
)


class BaseBloggerAppUnitTestCase(TestCase):
    """
    The Base TestCase class for all model tests to house app-wide utility methods,
    etc.
    """
    def create_mock_user(self):
        """
        Create a mock django.contrib.auth.models.User() object.
        """
        try:
            user = User.objects.get(username='muhammad')
        except Exception:
            user = User.objects.create(
            username="muhammad", is_staff=True, 
            first_name="Muhammad",last_name="Jalloh"
            )
            user.set_password("S3CReT123")
            user.save()
        return user 

    def create_mock_blogger(self, blogger_info):
        """
        Create a mock blogger.Blogger() instance
        """
        user = self.create_mock_user()
        blogger = Blogger.objects.create(user = user, **blogger_info)
        return blogger 

    def create_mock_blog(self, blog_data):
        """
        Create and return a mock blogger.Blog() instance for use in
        Unit Testing the same model.
        """
        blog = Blog.objects.create(owner=self.blogger, **blog_data)
        blog.save()
        return blog

    def create_mock_blog_category(self, category_data):
        """
        Create and return a mock blogger.BlogCategory instance
        """
        category = BlogCategory.objects.create(**category_data)
        category.save()
        return category 

    def create_mock_blogpost(self, blogpost_data):
        """
        Create and return a blogger.BlogPost() instance for use during unit-testing
        this same model.
        """
        blog_post = BlogPost.objects.create(**blogpost_data)
        blog_post.save()
        return blog_post
    
    def create_mock_comment(self, comment_data):
        """
        Utility method to create a blogger.Comment instance
        """
        if self.user:
            comment = Comment.objects.create(commenter=self.user, **comment_data)
        else:
            self.create_mock_user()
            comment = Comment.objects.create(comment=self.user, **comment_data)
        comment.save()
        return comment 

class HelperMethodsTest(BaseBloggerAppUnitTestCase):
    """
    TestCase class to test that the helper methods of the BaseBloggerAppUnitTestCase
    return the correct object instance types.
    """
    def test_create_mock_user_returns_user_instance(self):
        user = self.create_mock_user()
        self.assertIsInstance(user, User)

    def test_create_mock_blogger_returns_blogger_model_instance(self):

        blogger_info = {
            'bio': 'I am a mock Blogger'
        }
        blogger = self.create_mock_blogger(blogger_info)
        self.assertIsInstance(blogger, Blogger)

    def test_create_mock_blog_creates_and_returns_blog_model_instance(self):
        pass 

    def test_create_mock_blog_category_returns_blogcategory_model_instance(self):
        pass 

    def test_create_mock_blogpost_returns_valid_blogpost_object_instance(self):
        pass 

    def test_create_mock_comment_returns_valid_comment_object(self):
        pass 