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
        blog = Blog.objects.create(**blog_data)
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
        comment = Comment.objects.create(**comment_data)
        comment.save()
        return comment 

class HelperMethodsTest(BaseBloggerAppUnitTestCase):
    """
    TestCase class to test that the helper methods of the BaseBloggerAppUnitTestCase
    return the correct object instance types.
    """
    def test_create_mock_user_returns_auth_User_instance(self):
        user = self.create_mock_user()
        self.assertIsInstance(user, User)

    def test_create_mock_blogger_returns_Blogger_model_instance(self):

        blogger_info = {
            'bio': 'I am a mock Blogger'
        }
        blogger = self.create_mock_blogger(blogger_info)
        self.assertIsInstance(blogger, Blogger)

    def test_create_mock_blog_creates_AND_returns_Blog_model_instance(self):
        blogger_details = {
            'bio': 'I am a mock Blogger'
        }
        blogger = self.create_mock_blogger(blogger_details)
        blog_info = {
            'name': 'Blog One',
            'desc': "This blog is #1 in the technosphere.",
            'owner': blogger
            }
        blog = self.create_mock_blog(blog_info)
        self.assertIsInstance(blog, Blog)
    
    def test_create_mock_blog_category_returns_BlogCategory_model_instance(self):
        blogger_details = {
            'bio': 'I am a mock Blogger'
        }
        blogger = self.create_mock_blogger(blogger_details)
        blog_info = {
            'name': 'Primero Blog',
            'desc': "This blog is #1 in the technosphere.",
            'owner': blogger
            }
        blog = self.create_mock_blog(blog_info)
        blog_category_info = {
            'name': 'The Life of Technocrats',
            'desc' : 'How do technocrats live, breathe, make a living and go through life, one codebase at a time?',
            'blog': blog
        }
        new_blog_category = self.create_mock_blog_category(blog_category_info)
        self.assertIsInstance(new_blog_category, BlogCategory)

    def test_create_mock_blogpost_returns_valid_BlogPost_object_instance(self):
        blogger_details = {
            'bio': 'I am a creative Entrepreneurial Blogger.'
        }
        blogger = self.create_mock_blogger(blogger_details)
        blog_info = {
            'name': 'Blogzilla',
            'desc': 'This is the Wordzilla of blogs.',
            'owner': blogger
        }
        blog = self.create_mock_blog(blog_info)
        blog_category_info = {
            'name': 'Technocopia',
            'desc' : 'The dream of technocrats; the envy of tehchnophobes.',
            'blog': blog
        }
        category = self.create_mock_blog_category(blog_category_info)
        blogpost_info = {
            'title': 'Once upon a villagezilla.',
            'category':  category
        }
        blogpost_info = {
            'title': 'Once Upon a Coded Time',
            'body': 'There still lives a techpreneur who wanders the wilderness of TechVille.',
            'category': category
        }
        blogpost = self.create_mock_blogpost(blogpost_info)
        self.assertIsInstance(blogpost, BlogPost)
    
    def test_create_mock_comment_returns_valid_Comment_object(self):
        blogger_details = {
            'bio': 'I am a creative Entrepreneurial Blogger.'
        }
        blogger = self.create_mock_blogger(blogger_details)
        blog_info = {
            'name': 'Blogzilla',
            'desc': 'This is the Wordzilla of blogs.',
            'owner': blogger
        }
        blog = self.create_mock_blog(blog_info)
        blog_category_info = {
            'name': 'Technocopia',
            'desc' : 'The dream of technocrats; the envy of tehchnophobes.',
            'blog': blog
        }
        category = self.create_mock_blog_category(blog_category_info)
        blogpost_info = {
            'title': 'Once upon a villagezilla.',
            'category':  category
        }
        blogpost_info = {
            'title': 'Once Upon a Coded Time',
            'body': 'There still lives a techpreneur who wanders the wilderness of TechVille.',
            'category': category
        }
        blogpost = self.create_mock_blogpost(blogpost_info)
        commenter = User.objects.first()
        comment_data = {
            'commenter': commenter,
            'subject': "C'est la vie!",
            'blog_post': blogpost,
            'body': "I agree with 70% and disagree with 30%. Here's where I tell you more about that"
        }
        comment_on_blogpost = self.create_mock_comment(comment_data)
        self.assertIsInstance(comment_on_blogpost, Comment)