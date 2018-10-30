from django.conf.urls import url 
from blogger import views 

urlpatterns = [
    url(r'^$',views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^newsletter/$', views.newsletter, name="newsletter"),
    url(r'^legal/$', views.legal_terms, name="legal"),
    url(r'^comment/(?P<post_link>[-\w]+)/$', views.comment_on_post, name="comment"),
    url(r'^(?P<blog_page>[-\w]+)/$', views.blog_detail, name="blog_detail"),
    url(r'^(?P<blog_page>[-\w]+)/(?P<category_page>[-\w]+)/$', views.blog_category_detail, name="blog_category"),
    url(r'^(?P<blog_page>[-\w]+)/(?P<category_page>[-\w]+)/(?P<post_page>[-\w]+)/$', views.blog_post_detail, name="blog_post"),
    

]