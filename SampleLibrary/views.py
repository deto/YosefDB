from django.shortcuts import render
from django.http import HttpResponse;
from django.template import RequestContext, loader;

from .models import Sample;
# Create your views here.

def index(request):
    sample = Sample.objects.first();
    context = {'sample': sample};
    return render(request, 'SampleLibrary/index.html', context);


def uploadSample(request):
    try:
        filename = request.POST["filename"];
    except KeyError:
        return render(request, 'SampleLibrary/uploadSample.html')

    context = {'filename': filename};
    return render(request, 'SampleLibrary/uploadSample.html', context);
