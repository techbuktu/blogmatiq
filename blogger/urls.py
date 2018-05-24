from django.conf.urls import url 
from blogger import views 

urlpatterns = [
    url(r'^$',views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^newsletter/$', views.newsletter, name="newsletter"),
    url(r'^legal/$', views.legal_terms, name="legal"),
    url(r'^comment/(?P<post_link>[-\w]+)/$', views.comment_on_post, name="comment"),

]