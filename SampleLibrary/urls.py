from django.conf.urls import url;

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadSample', views.uploadSample, name='uploadSample')
]