from functional_tests.base import BaseFunctionalTest

from blogger.models import (Blogger, Blog, BlogCategory, BlogPost, Comment)

class BloggerAppFunctionalTest(BaseFunctionalTest):
    """
    Parent/base Functional Test class to house reusable methods, etc.
    across blogger app's functional tests.
    """
    def get_blogger(self):
        """
        Returns a sample blogger.Blogger model instance for use in tests.
        """
        blogger = Blogger.objects.get(user__username="muhammad")
        return blogger
    
    def create_a_blog(self, blog_obj):
        """
        utitlity method to generate a blogger.Blog model instance for use in
        testing.
        """
        blogger = self.get_blogger()
        blog = Blog.objects.create(blogger=blogger, **blog_obj)
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

