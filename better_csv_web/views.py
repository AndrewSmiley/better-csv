__author__ = 'pridemai'
from django.shortcuts import render, render_to_response
from functions import *
def index(request):
    return render(request, 'index.html')

def batch_selection(request):

    return render(request, "batch_selection.html",{
     'filenames' : get_all_filenames()
    })

    pass

def run_batch(request):
    results = execute(request)
    return render(request, "results.html",{
            "results": results
    })

def file_upload(request):
    if request.method == 'POST':
        upload_file(request, 'is_master' in request.POST)
        return render(request, "file_upload.html",{
             "message":"File %s uploaded" % (request.FILES['csv'].name)
        })
    return render(request, "file_upload.html")