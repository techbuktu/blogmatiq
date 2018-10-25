from functional_tests.base import BaseFunctionalTest
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost, Comment)

class BloggerAppFunctionalTest(BaseFunctionalTest):
    """
    Parent/base Functional Test class to house reusable methods, etc.
    across blogger app's functional tests.
    """
    def create_a_blog(self, blog_obj):
        """
        utitlity method to generate a blogger.Blog model instance for use in
        testing.
        """
        blogger_dict = {
            "bio": "I am (what you would call) an accomplished 'Bloglite.'"
        }
        blog_owner = self.create_blogger(blogger_dict)
        blog = Blog.objects.create(owner=blog_owner, **blog_obj)
        blog.save()
        return blog

    def create_blogcategory(self, category_data):
        """
        Utitlity method to create and return a blogger.BlogCategory model
        instance for use in testing.
        """
        category = BlogCategory.objects.create(**category_data)
        category.save()
        return category

    def create_blogpost(self, blogpost_data):
        """
        Reusable method to create a blogger.BlogPost model object
        and return it for (re)use during testing.
        """
        blog_post = BlogPost.objects.create(**blogpost_data)
        blog_post.save()
        return blog_post

    def create_blogger(self, blogger_data):
        """
        FT utility method to create and return a blogger.Blogger model instance
        for use during testing.
        """
        if self.user:
            blogger = Blogger.objects.create(user=self.user, **blogger_data)
        else:
            self.create_user()
            blogger = Blogger.objects.create(user=self.user, **blogger_data)
        blogger.save()
        return blogger 