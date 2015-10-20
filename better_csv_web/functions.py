__author__ = 'pridemai'
from models import File,ColumnMapping
from better_csv_web.settings import *
import traceback
def get_all_filenames():

    return File.objects.filter(is_master=False)

def upload_file(request, is_master):
    file = File()
    file.filename = request.FILES['csv'].name
    file.is_master = is_master
    file.save()
    #write the file to the disk
    with open(BASE_DIR+"/data/"+request.FILES['csv'].name, 'wb+') as destination:
        for chunk in request.FILES['csv'].chunks():
            destination.write(chunk)


def rename_file(fname, new_filename):
    try:
        file = File.objects.get(filename=fname)
        file.filename = new_filename
        file.save()
        return {"result":True}
    except:
        return {"result":False, "message": traceback.print_exc()}

