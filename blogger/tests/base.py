from django.test import TestCase 
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
        user = User.objects.create(
            username="muhammad", is_staff=True, 
            first_name="Muhammad",last_name="Jalloh"
            )
        user.set_password("S3CReT123")
        user.save()
        self.user = user 

    def create_mock_blogger(self, blogger_info):
        """
        Create a mock blogger.Blogger() instance
        """
        self.create_mock_user()
        if self.user:
            blogger = Blogger.objects.create(user=self.user, **blogger_info)
        else:
            self.create_user()
            blogger = Blogger.objects.create(user=self.user, **blogger_info)
        blogger.save()
        self.blogger = blogger

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

