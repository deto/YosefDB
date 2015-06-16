from django.shortcuts import render, render_to_response;
from django.template.context_processors import csrf;
from django.http import HttpResponse;
from django.template import RequestContext, loader;
from django.core import serializers;
from django.views.decorators.csrf import csrf_exempt;

from .fileOps import handle_uploaded_file;

from .models import Sample;
from .forms import UploadFileForm;
# Create your views here.

def uploadSample(request):
    c = {};
    c.update(csrf(request));
    if(request.method == 'POST'):
        form = UploadFileForm(request.POST, request.FILES);
        if(form.is_valid()):
            handle_uploaded_file(form.cleaned_data["uploadedBy"], request.FILES['file'])
    else:
        form = UploadFileForm();

    c.update({'file_form':form});

    return render_to_response('SampleLibrary/uploadSample.html',c );


def viewSample(request):
    c = {}
    c.update(csrf(request));
    return render_to_response('SampleLibrary/viewSamples.html',c);

@csrf_exempt
def samples_asJson(request):
    #import pdb; pdb.set_trace();
    params = request.POST;

    #Filter by number and offset.
    start = int(params["start"]);
    length = int(params["length"]);
    samples = Sample.objects.all();
    paged_samples = samples[start:(start+length)];
    json_samples = '"data": ' + serializers.serialize('json',paged_samples);

    other_DT_vals = dict({
        "draw": int(params["draw"]),
        "recordsTotal": Sample.objects.count(),
        "recordsFiltered": len(samples),
    });


    json_list = ['"'+key+'": ' + str(val) for key,val in other_DT_vals.items()];
    json_list.append(json_samples);
    json = "{" + ','.join(json_list) + "}";

    return HttpResponse(json, content_type='application/json');
