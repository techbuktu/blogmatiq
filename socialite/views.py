from django.shortcuts import render

SITE_URL = "http://Example.com" #REPLACE with your actual website URL
# Create your views here.
def home(request):
    return render(request, "Socialite Home")


def facebook_share(request, page_url):
    page_url = page_url
    data = {
        'page_url': page_url
    }
    return render(request, "socialite/facebook_share.html", data)

def twitter_share(request, page_url):
    data = {}
    return render(request, "socialite/twitter_share.html", data)

def linkedin_share(request, page_url):
    data = {}
    return render(request, "socialite/linkedin_share.html", data)
