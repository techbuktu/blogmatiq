from django.conf.urls import url 
from socialite import views

urlpatterns = [
   url(r'^$', views.home, name="home"),
   url(r'^facebook/(?P<page_url>.*)/$', views.facebook_share, name="share_on_facebook"),
   url(r'^twitter/(?P<page_url>.*)/$', views.twitter_share, name="share_on_twitter"),
   url(r'^linkedin/(?P<page_url>.*)/$', views.linkedin_share, name="share_on_linkedin"),
]

