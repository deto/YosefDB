from django.conf.urls import url;

from . import views

urlpatterns = [
    url(r'^Upload$', views.uploadSample, name='uploadSample'),
    url(r'^Browse$', views.viewSample, name='viewSample'),
    url(r'^ManageUploads$', views.manageUploads, name='manageUploads'),
    url(r'^ViewUpload$', views.viewUpload, name='viewUpload'),
    url(r'^ValidateUpload$', views.validateUpload, name='validateUpload'),
    url(r'^samples_asJson$', views.samples_asJson, name='DT_Ajax'),
    url(r'^uploads_asJson$', views.uploads_asJson, name="Uploads_Ajax"),
    url(r'^uploads_Samples_asJson$', views.singleUpload_Samples_asJson, name='SingleUploads_Samples_Ajax'),
    url(r'^unverified_samples_asJson$', views.unvalidatedUpload_samples_asJson, name='UnvalidatedUpload_Samples_Ajax'),
    url(r'^Delete_Upload', views.delete_Upload, name='Delete_Upload_Ajax'),
    url(r'^$', views.publicView, name='PublicView'),
    url(r'^Logout', views.logout_view, name='LogoutView')
]