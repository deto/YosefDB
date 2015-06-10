from django.shortcuts import render, render_to_response;
from django.template.context_processors import csrf;
from django.http import HttpResponse;
from django.template import RequestContext, loader;

from .fileOps import handle_uploaded_file;

from .models import Sample;
from .forms import UploadFileForm;
# Create your views here.

def index(request):
    sample = Sample.objects.first();
    context = {'sample': sample};
    return render(request, 'SampleLibrary/index.html', context);


def uploadSample(request):
    c = {};
    c.update(csrf(request));
    if(request.method == 'POST'):
        import pdb; pdb.set_trace();
        form = UploadFileForm(request.POST, request.FILES);
        if(form.is_valid()):
            handle_uploaded_file(request.FILES['file'])
    else:
        form = UploadFileForm();

    c.update({'file_form':form});

    return render_to_response('SampleLibrary/uploadSample.html',c );


