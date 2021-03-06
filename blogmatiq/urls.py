"""blogmatiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin
from socialite.api.views import blogmatiq_api_root 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('django.contrib.auth.urls', namespace="auth")),
    url(r'^social/', include('social_django.urls', namespace="social")),
    url(r'^api/$', blogmatiq_api_root, name="blogmatiq_api_root"),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^socialite/', include('socialite.urls', namespace="socialite")),
    url(r'', include('blogger.urls', namespace="blogger")),
    url(r'^api/blogger/', include('blogger.api.urls', namespace="blogger_api")),
    url(r'^api/socialite/', include('socialite.api.urls', namespace='socialite_api')),
]
