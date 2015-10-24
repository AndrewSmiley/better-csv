__author__ = 'pridemai'
from django.shortcuts import render, render_to_response, HttpResponseRedirect, HttpResponse
from functions import *
from django.core.urlresolvers import reverse
from better_csv_web.settings import *
from functions import get_file
from models import Folder

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
        response['Content-Disposition'] = 'attachment; filename="%s"' % request.POST['filename']
        response.write(file.read())
        return response
    else:
        return HttpResponseRedirect(reverse("dowload_list"))

def view_data_selection(request):
    return  render(request, "view_data_selection.html", {"files": get_all_files(), "folders":Folder.objects.all()})
def view_data(request):
    if request.method != 'POST':
        return ("This is not a valid way to access")
    else:
        return render(request, "view_data.html", {"rows":BetterCSV().get_lists(BetterCSV().get_lines(get_file("%s/%s/"%(BASE_DIR,request.POST['folder']), request.POST['filename']).read())), "file":request.POST['filename']})
def ajax_handler(request,action):
    if action == u'get_files':
        return HttpResponse(''.join(list("<option value=\"%s\">%s</option>" % (x,x) for x in get_files_in_folder(("%s/%s/" % (BASE_DIR,request.GET['folder']))))))
        pass
    elif action == u'run_batch':
        results = execute(request)
        messages = results['messages']
        messages.append("Total Time: "+str(results['runtime'])+" Seconds")
        return HttpResponse(''.join(list("<p>%s</p>" % (x) for x in messages)))
    elif action == u'search':
        results = searchInFiles()

    return HttpResponse("Proof of concept: %s" % (action))

def search(request):
    return render(request, "search.html",{"files":get_all_files()})