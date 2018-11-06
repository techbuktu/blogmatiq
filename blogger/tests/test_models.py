from django.test import TestCase 
from django.contrib.auth.models import User 
from blogger.models import (
    Blogger, Blog, BlogCategory, BlogPost, Comment
)

class BaseModelTestCase(TestCase):
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

    def create_mock_blogger(self):
        """
        Create a mock blogger.Blogger() instance
        """
        self.create_mock_user()
        blogger_info = {
            'bio': 'I am a Software Blogger.'
        }
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
        self.create_mock_blogger()
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
    
    def create_mock_comment(self):
        """
        """
        pass 


class BloggerModelTestCase(BaseModelTestCase):
    """
    Tests the blogger.Blogger model for proper validation, data integrity and state of 
    its fields.
    """
    def test_user_exists(self):
        """
        Check that a User() can be automatically-created using the base 
        self.create_mock_user() method.
        """
        self.create_mock_user()
        self.assertEqual('muhammad', self.user.username)

    def test_blogger_is_related_onetoone_to_a_user(self):
        pass 

    def test_blogger_has_a_valid_page_field_value(self):
        pass 
    
    def test_blogger_has_a_valid_date_joined_value(self):
        pass 

    def test_date_joined_is_older_than_last_updated_field(self):
        pass 

    def test_blogger_last_updated_field_can_be_null_by_default(self):
        pass 

    def test_last_updated_field_cannot_be_reverted_to_null(self):
        pass 

    def test_blogger_has_valid_string_representation(self):
        pass 

    def test_blogger_has_a_valid_page_URL(self):
        pass 

    def test_get_absolute_url_returns_valid_value(self):
        pass 


class BlogModelTest(TestCase):
    """
    Tests the blogger.Blog model's fields, validation, model relationships, etc.
    """
    def create_new_blog_model_instance(self):
        pass 

    def test_blog_has_a_blogger_who_owns_it(self):
        pass 

    def test_blog_cannot_have_null_name(self):
        pass 

    def test_blog_cannot_have_tampered_with_date_created_value(self):
        pass 

    def test_date_created_value_must_be_earlier_than_last_updated_value(self):
        pass 

    def test_last_updated_value_cannot_be_be_tampered_with(self):
        pass 

    def test_blog_must_have_a_valid_page_URL_generated_from_its_name_field_value(self):
        pass 

    def test_blog_must_have_valid_and_proper_string_representation(self):
        pass 

    def test_desc_field_cannot_be_blank_or_null(self):
        pass 

    def test_get_absolute_url_method_returns_valid_full_blog_page_url(self):
        pass 

    def test_blog_can_return_queryset_of_its_related_blog_categories(self):
        pass 

class BlogCategoryModelTest(TestCase):
    """
    Tests validity, integrity and attributes of blogger.BlogCategory model
    """

    def create_blog_category_instance(self, category_data):
        pass 

    def test_category_is_linked_to_a_valid_blog(self):
        pass 

    def test_category_must_have_a_blank_page_URL_value_during_instantiation(self):
        pass 

    def test_category_must_have_a_non_nullable_value(self):
        pass 

    def test_category_can_return_only_its_list_of_related_blogposts(self):
        pass 

    def test_category_must_have_valid_string_representation(self):
        pass 

    def test_get_absolute_url_method_must_return_full_url_to_categorys_page(self):
        pass 

class BlogPostModelTest(TestCase):
    """
    Tests the blogger.BlogPost model for field validity, data integrity and attributes
    """
    def ceate_blogpost_instance(self, blogpost_data):
        pass 
    
    def test_blogpost_has_a_parent_category(self):
        pass 

    def test_blogpost_title_cannot_be_blank_or_null(self):
        pass 

    def test_posted_date_value_must_be_blank_at_instantiation_but_not_null(self):
        pass 

    def test_updated_field_value_must_be_later_than_posted_date(self):
        pass 

    def test_updated_field_value_must_be_blank_at_instantiation(self):
        pass 

    def test_updated_field_value_cannot_revert_to_blank_after_its_get_value(self):
        pass 

    def test_blogpost_body_cannot_be_blank_or_null(self):
        pass 

    def test_blogpost_must_have_a_valid_page_URL_value(self):
        pass 

    def test_page_URL_value_must_be_derived_from_blogpost_title_value(self):
        pass 

class CommentModelTest(TestCase):
    """
    Covers Unit Tests for the blogger.Comment model
    """
    def create_a_comment(self, comment_data):
        pass 

    def test_comment_must_have_a_valid_auth_user(self):
        pass 

    def test_comment_must_have_a_subject_at_instantiation(self):
        pass 

    def test_comment_must_be_linked_to_a_valid_blogpost_instance(self):
        pass 

    def test_comment_body_cannot_be_blank(self):
        pass 

    def test_comment_body_cannot_be_null(self):
        pass 
    
    def test_comment_must_have_a_unique_page_URL_field_value(self):
        pass 
    
    def test_comment_must_have_a_nonnullable_comment_date_value(self):
        pass

    def test_comment_date_must_be_blank_at_instantiation(self):
        pass 

    def test_comment_date_cannot_be_reverted_to_blank_after_it_gets_value(self):
        pass 

    def test_page_URL_field_must_derive_from_comment_subject_value(self):
        pass 

    def test_page_field_must_be_blank_at_instantiation(self):
        pass 