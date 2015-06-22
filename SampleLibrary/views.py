from django.shortcuts import render, render_to_response, redirect;
from django.template.context_processors import csrf;
from django.http import HttpResponse;
from django.template import RequestContext, loader;
from django.core import serializers;
import CustomSerializers;
from django.views.decorators.csrf import csrf_exempt;
from django.contrib.auth import authenticate, login, logout;
from django.contrib.auth.decorators import login_required;

from .fileOps import handle_uploaded_file;

from .models import Sample, Upload;
from .forms import UploadFileForm;
# Create your views here.

@login_required
def uploadSample(request):
    c = {};
    c.update(csrf(request));
    if(request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES);
        if(form.is_valid()):
            handle_uploaded_file(request.user, request.FILES['file'])
    else:
        form = UploadFileForm();

    c.update({'file_form':form});

    return render_to_response('SampleLibrary/uploadSample.html',c );


@login_required
def viewSample(request):
    c = {}
    c.update(csrf(request));
    return render_to_response('SampleLibrary/viewSamples.html',c);

@login_required
def viewUpload(request):
    c = {}
    c.update(csrf(request));
    uuid = request.GET["id"];
    c.update({"uuid": uuid});
    return render_to_response('SampleLibrary/viewSingleUpload.html',c);

@login_required
def manageUploads(request):
    c = {}
    c.update(csrf(request));
    return render_to_response('SampleLibrary/manageUploads.html',c);

@csrf_exempt
@login_required
def singleUpload_Samples_asJson(request):
    uuid = request.GET["id"];
    samples = Sample.objects.filter(UploadBatch = uuid);
    json_samples = '"data": ' + serializers.serialize('json',samples);
    json = "{" + json_samples + "}";
    return HttpResponse(json, content_type='application/json');

@csrf_exempt
@login_required
def samples_asJson(request):
    #import pdb; pdb.set_trace();
    params = request.POST;

    #Filter by number and offset.
    start = int(params["start"]);
    length = int(params["length"]);
    samples = Sample.objects.select_related().all();
    paged_samples = samples[start:(start+length)];
    json_samples = '"data": ' + CustomSerializers.serialize_samples(paged_samples);

    other_DT_vals = dict({
        "draw": int(params["draw"]),
        "recordsTotal": Sample.objects.count(),
        "recordsFiltered": len(samples),
    });

    json_list = ['"'+key+'": ' + str(val) for key,val in other_DT_vals.items()];
    json_list.append(json_samples);
    json = "{" + ','.join(json_list) + "}";

    return HttpResponse(json, content_type='application/json');

@csrf_exempt
@login_required
def uploads_asJson(request):
    #import pdb; pdb.set_trace();
    params = request.POST;

    #Filter by number and offset.
    start = int(params["start"]);
    length = int(params["length"]);
    uploads = Upload.objects.all();
    paged_uploads = uploads[start:(start+length)];
    json_uploads = '"data": ' + serializers.serialize('json',paged_uploads);

    other_DT_vals = dict({
        "draw": int(params["draw"]),
        "recordsTotal": Upload.objects.count(),
        "recordsFiltered": len(uploads),
    });

    json_list = ['"'+key+'": ' + str(val) for key,val in other_DT_vals.items()];
    json_list.append(json_uploads);
    json = "{" + ','.join(json_list) + "}";

    return HttpResponse(json, content_type='application/json');

@csrf_exempt
@login_required
def delete_Upload(request):
    uuid = request.POST["uuid"];
    upload_to_delete = Upload.objects.get(UploadId = uuid);
    upload_to_delete.delete(); #This should cascade-delete all samples in the upload
    return HttpResponse(status=200);


def logout_view(request):
    logout(request);
    return redirect("PublicView");

def publicView(request):
    c = {};
    c.update(csrf(request));
    c["loginFail"] = False;
    if(request.method == "POST"):
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(username=username, password=password);
        if user is not None:
            if user.is_active:
                login(request, user);
                return redirect("viewSample");
        else:
           c["loginFail"] = True;

    return render_to_response("SampleLibrary/public.html", c);