from django.conf.urls import url;

from . import views

urlpatterns = [
    url(r'^Upload$', views.uploadSample, name='uploadSample'),
    url(r'^Browse$', views.viewSample, name='viewSample'),
    url(r'^samples_asJson$', views.samples_asJson, name='DT_Ajax'),
    url(r'^$', views.publicView, name='PublicView'),
    url(r'^Logout', views.logout_view, name='LogoutView')
]