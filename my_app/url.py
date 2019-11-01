from django.conf.urls import url
from .views import HomeView, PostView, BlogsView

urlpatterns = [
    url('home/', HomeView.as_view(), name='home_url'),
    url('blogs/', BlogsView.as_view(), name='blog_url'),
    url(r'^post/(\d+)/$', PostView.as_view(), name='post_url'),
]