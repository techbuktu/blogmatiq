from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blogger.models import Blog 

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
    page_url = request.path.strip('')
    context_data = {
        'blog': blog,
        'page_url': page_url
    }
    return render(request, 'blogger/blog_detail.html', context_data)