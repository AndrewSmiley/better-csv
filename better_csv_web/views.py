__author__ = 'pridemai'
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from functions import *
from django.core.urlresolvers import reverse
from better_csv_web.settings import *
from functions import get_file

def index(request):
    return render(request, 'index.html')
def batch_selection(request):

    return render(request, "batch_selection.html",{
     'source_files' : get_all_source_file_names(),
     'master_files' : get_all_master_file_names()
    })

    pass
def run_batch(request):
    results = execute(request)
    return render(request, "results.html",{
            "results": results["messages"], "runtime":results["runtime"]
    })
def file_upload(request):
    if request.method == 'POST':
        upload_file(request, 'is_master' in request.POST)
        return render(request, "file_upload.html",{
             "message":"File %s uploaded" % (request.FILES['csv'].name)
        })
    return render(request, "file_upload.html")
def download_list(request):
    return render(request, "download_list.html",{
        "files": get_result_files()
    })

def download(request):
    if request.method == 'POST':
        file = get_file(BASE_DIR+MASTERS_DIR, request.POST['filename'])
        response = HttpResponse()
        response['Content-Disposition'] = 'attachment; filename="%"' % request.POST['filename']
        response.write(file.body)
        return response
    else:
        return HttpResponseRedirect(reverse("dowload_list"))