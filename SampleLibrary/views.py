from django.shortcuts import render, render_to_response, redirect;
from django.template.context_processors import csrf;
from django.http import HttpResponse;
from django.template import RequestContext, loader;
from django.core import serializers;
import CustomSerializers;
from django.views.decorators.csrf import csrf_exempt;
from django.contrib.auth import authenticate, login, logout;
from django.contrib.auth.decorators import login_required;

from .fileOps import handle_uploaded_file, validate_upload;

from .models import Sample, Upload, UnvalidatedUpload, UnvalidatedSample;
from .forms import UploadFileForm, AccountSettingsForm;
import re;
# Create your views here.

@login_required
def uploadSample(request):
    c = {};
    c.update(csrf(request));
    if(request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES);
        if(form.is_valid()):
            this_upload = handle_uploaded_file(request.user, request.FILES['file'])
            response = redirect("validateUpload");
            response['Location'] += '?id=' + str(this_upload.UploadId);
            return response;

    form = UploadFileForm();
    c.update({'file_form':form});
    return render_to_response('SampleLibrary/uploadSample.html',c );

@login_required
def accountSettings(request):
    c = {};
    c.update(csrf(request));
    page_errors = [];
    if(request.method == 'POST'):
        form = AccountSettingsForm(request.POST);
        if(form.is_valid()):
            firstname = form.cleaned_data['firstname'];
            lastname = form.cleaned_data['lastname'];
            email = form.cleaned_data['email'];

            old_pw = form.cleaned_data['currentpassword'];
            new_pw = form.cleaned_data['newpassword'];
            new_pw_rp = form.cleaned_data['newpassword_repeat'];
            change_password = False;
            if(old_pw != "" or new_pw != "" or new_pw_rp != ""):
                change_password = True;
                if(not request.user.check_password(old_pw)):
                    page_errors.append("Current Password is not correct.");

                if(new_pw != new_pw_rp):
                    page_errors.append("New Passwords do not match.")

                if(new_pw != "" and old_pw == ""):
                    page_errors.append("Current Password required to change password");

            if(len(page_errors) > 0):
                c.update({"page_errors": page_errors});
            else:
                user = request.user;
                user.first_name = firstname;
                user.last_name = lastname;
                user.email = email;
                if(change_password):
                    user.set_password(new_pw);

                user.save();
                c.update({"save_success": True})
    else:
        form = AccountSettingsForm(initial={
            "firstname": request.user.first_name,
            "lastname": request.user.last_name,
            "email": request.user.email,
        });

    c.update({'username': request.user.username});
    c.update({'account_settings_form': form});

    return render_to_response("SampleLibrary/accountSettings.html", c);


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
def validateUpload(request):
    if(request.method == "POST"):
        if("save" in request.POST):
            uuid = request.POST["uploadUUID"];
            unvalidatedUpload = UnvalidatedUpload.objects.get(UploadId = uuid);
            validate_upload(unvalidatedUpload);
            return redirect("viewSample");
        else:
            return redirect("uploadSample");


    c = {}
    c.update(csrf(request));
    uuid = request.GET["id"];
    unvalidatedUpload = UnvalidatedUpload.objects.get(UploadId = uuid);
    unrecognized_headers = unvalidatedUpload.UnrecognizedCols.split("\n");
    if(len(unrecognized_headers) == 1 and unrecognized_headers[0] == ""):
        unrecognized_headers = [];
    c.update({"unrecognized_headers": unrecognized_headers});
    c.update({"has_unrecognized": len(unrecognized_headers) > 0});
    c.update({"uuid": uuid});
    return render_to_response('SampleLibrary/validateUpload.html',c);

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
def unvalidatedUpload_samples_asJson(request):
    uuid = request.GET["id"];
    samples = UnvalidatedSample.objects.filter(UploadBatch = uuid);
    json_samples = '"data": ' + serializers.serialize('json',samples);
    json = "{" + json_samples + "}";
    return HttpResponse(json, content_type='application/json');


@csrf_exempt
@login_required
def samples_asJson(request):
    params = request.POST;

    #Determine sort order
    sort_col = params['order[0][column]'];
    sort_dir = params['order[0][dir]'];

    sort_name = params['columns[' + sort_col + '][name]'];

    if(sort_name == "Uploader"):
        sort_name = "UploadBatch__UploadedBy__first_name";

    if(sort_dir == "desc"):
        sort_name = '-' + sort_name;  #negative in front means descending

    #Extract any search terms
    search_patterns = list();
    for key in params.keys():
        if(key.find("[search][value]") > -1 and key.startswith('columns[') and params[key] != ''):
            col_prefix = re.search('columns\[\d+\]', key).group();
            name = params[col_prefix + '[name]'];
            val = params[col_prefix + '[search][value]'];
            vals = [x.strip() for x in val.split(';')];
            for val in vals:
                search_patterns.append({'name':name, 'value':val});


    #Filter by number and offset.
    start = int(params["start"]);
    length = int(params["length"]);
    samples = Sample.objects.select_related().all();

    for search_pattern in search_patterns:
        if(search_pattern['name'] == "Uploader"):
            search_pattern['name'] = "UploadBatch__UploadedBy__first_name";

        #Seems to work on ints too?
        samples = samples.filter(**{search_pattern['name'] +'__icontains': search_pattern['value']});

    samples = samples.order_by(sort_name);
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
    uploads = Upload.objects.all();
    json_uploads = '"data": ' + CustomSerializers.serialize_uploads(uploads);

    json = "{" + json_uploads + "}";

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