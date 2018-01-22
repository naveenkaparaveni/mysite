from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment
from . import views 

app_name = 'blog'
urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                           template_name="blog/blog.html")),
                url(r'^(?P<pk>\d+)$', views.post_detail, name='post_detail'),
                url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name = 'add_comment'),
                ]

























