import django.conf.urls
from . import views

urlpatterns = [
    django.conf.urls.url(r'^$', views.index, name='index'),
    django.conf.urls.url(r'^Contact/', views.contact, name='contact'),
    django.conf.urls.url(r'^Login/', views.login, name='login'),
    django.conf.urls.url(r'^Signin/', views.signin, name='signin'),
    ]
