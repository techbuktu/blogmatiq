from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.text import slugify 
from django.contrib.auth.models import User 


# Create your models here.
class Blogger(models.Model):
	user = models.OneToOneField(User, related_name="blogger", on_delete=models.CASCADE)
	bio = models.TextField(max_length=500)
	page = models.SlugField(max_length=100, blank=True)
	joined = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(blank=True, null=True, editable=False)


	def __str__(self):
		return "%: %" % (self.user.username, self.joined)

	def save(self, *args, **kwargs):
		if not page:
			user_names = self.user.first_name + self.user.last_name
			self.page = slugify(user_names[:90])

		super(Blogger, self).save(*args, **kwargs)

class Blog(models.Model):
	owner = models.ForeignKey(Blogger, related_name="blogs", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	desc = models.TextField()
	page = models.SlugField(max_length=110, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(null=True, blank=True, editable=False)

	def __str__(self):
		return "%s" % (self.name)

	def save(self, *args, **kwargs):
		if not self.page:
			self.page = slugify(self.name)
		super(Blog, self).save(*args, **kwargs)
    		

class BlogCategory(models.Model):
	name = models.CharField(max_length=100)
	desc = models.TextField(verbose_name="Description", max_length=350)
	page = models.SlugField(max_length=120, blank=True)
	blog = models.ForeignKey(Blog, related_name="categories", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Blog Category"
		verbose_name_plural = "Blog Categories"

	def save(self, *args, **kwargs):
		if not self.page:
			self.page = slugify(self.name)
		super(BlogCategory, self).save(*args, **kwargs)


	def __str__(self):
		return self.name 

class BlogPost(models.Model):
	category = models.ForeignKey(BlogCategory, related_name="posts", on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	page = models.SlugField(max_length=120, blank=True)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(blank=True, null=True, editable=False)

	def __str__(self):
		return "%s => %s" % (self.title, self.category.name)

class Comment(models.Model):
	commenter = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
	subject = models.CharField(max_length=100)
	page = models.SlugField(max_length=120, blank=True)
	blog_post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
	body = models.TextField(max_length=500)
	comment_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "%s" % (self.subject)

	def save(self, *args, **kwargs):
		if not self.page:
			self.page = slugify(self.subject)
		super(Comment, self).save(*args, **kwargs)
