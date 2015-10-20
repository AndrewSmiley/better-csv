__author__ = 'pridemai'
from models import File,ColumnMapping,SearchColumn
from better_csv_web.settings import *
import traceback
import time
from parse_functions import BetterCSV
DATA_DIR = "/data/"
MASTERS_DIR = "/masters/"

def write_csv(filepath,rows):
    hs = open(filepath,"w+")
    for mline in rows:
        hs.write(",".join(mline)+"\r")

    hs.close()
def get_all_filenames():

    return File.objects.filter(is_master=False)

def upload_file(request, is_master):
    file = File()
    file.filename = request.FILES['csv'].name
    file.is_master = is_master
    file.save()
    #write the file to the disk
    with open(BASE_DIR+DATA_DIR+request.FILES['csv'].name, 'wb+') as destination:
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

def execute(request):

    messages=[]
    for master in File.objects.filter(is_master=True):
        master_copy= BetterCSV().get_lists(BetterCSV().get_lines(open(BASE_DIR+DATA_DIR+master.filename).read()))
        filenames = []

        for file in request.POST.getlist('filenames'):
            data_file= BetterCSV().get_lists(BetterCSV().get_lines(open(BASE_DIR+DATA_DIR+file).read()))
            #load the search columns
            master_search_columns = []
            for msc in SearchColumn.objects.filter(datafile=master):
                master_search_columns.append(msc.column_id-1)
            data_search_columns =[]
            for dsc in SearchColumn.objects.filter(datafile=File.objects.get(filename=file)):
                data_search_columns.append(dsc.column_id-1)
            #load the mappings
            mappings = {}
            for mapping in ColumnMapping.objects.filter(datafile=File.objects.get(filename=file)):
                mappings[mapping.master_column_id-1]=mapping.source_column_id-1
            #actually execute and update
            results =iterate(master_copy, data_file,master_search_columns,data_search_columns,mappings,file)
            master_copy = results['data']
            messages.append(results['message'])


        write_csv(str(BASE_DIR+MASTERS_DIR+str(time.strftime("%d%m%Y"))+str(time.strftime("%H-%M-%S"))+".csv"), master_copy)
        return messages




def update_row(master_row, data_row, column_mapping):
    for key,value in column_mapping.iteritems():
        master_row[key]=data_row[value]
    return master_row

def iterate(master_copy,data_copy, master_search_columns, data_search_columns, column_mapping, filname="N/A"):
    """
    Function to do stuff
    :param master_copy:
    :param data_copy:
    :param master_search_columns:
    :param data_search_columns:
    :param master_data_columns:
    :param data_columns:
    :param filname:
    :return:
    """
    better_csv = BetterCSV()
    new_master = []
    found_count = 0
    for line in master_copy:
        master_args=[]
        for column in master_search_columns:
            master_args.append(line[column])
        for d in data_copy:
            data_args =[]
            for column in data_search_columns:
                data_args.append(d[column])
            if better_csv.search(master_args, data_args) :
                line = update_row(line, d, column_mapping)
                found_count = found_count + 1
                break
        new_master.append(line)
    return {"data":new_master, "message": "%s count: %s" % (filname, found_count)}