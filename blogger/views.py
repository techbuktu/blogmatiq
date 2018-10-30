from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blogger.models import (Blogger, Blog, BlogCategory, BlogPost, Comment)

# Create your views here.
PAGE_URL = "page-url-here"
def home(request):
    blog_list = Blog.objects.all()
    data = {
        'blog_list': blog_list,
        "page_url": PAGE_URL
    }
    return render(request, "blogger/index.html", data)

def comment_on_post(request, post_link):
    data = {}
    return HttpResponse("Comment on %s " % (post_link))

def about(request):
    data = {
        'page_url': PAGE_URL
    }
    return render(request, "blogger/about.html", data)

def contact(request):
    data = {
         'page_url': PAGE_URL
    }
    return render(request, "blogger/contact.html", data)

def newsletter(request):
    data = {
         'page_url': PAGE_URL
    }
    return render(request, "blogger/newsletter.html", data)

def legal_terms(request):
    data = {
         'page_url': PAGE_URL
    }
    return render(request, "blogger/legal.html", data)

def blog_detail(request, blog_page):
    blog = Blog.objects.get(page=blog_page)
    blog_categories = BlogCategory.objects.filter(blog=blog)
    blogposts_list = BlogPost.objects.filter(category__blog__page=blog_page)
    page_url = request.path
    context_data = {
        'blog': blog,
        'page_url': page_url,
        'blog_categories': blog_categories,
        'blogposts_list': blogposts_list
    }
    return render(request, 'blogger/blog_detail.html', context_data)

def blog_category_detail(request, blog_page, category_page):
    category = BlogCategory.objects.get(blog__page=blog_page, page=category_page)
    category_posts = BlogPost.objects.filter(category=category)
    data = {
        'category': category,
        'category_posts': category_posts
    }
    return render(request, 'blogger/blog_category_detail.html', data)

def blog_post_detail(request, blog_page, category_page, post_page):
    blog_post = BlogPost.objects.get(page=post_page)
    comments = blog_post.comments.al()
    data = {
        'blog_post': blog_post,
        'comments_on_post': comments
    }
    return render(request, 'blogger/blog_post.html', data)

