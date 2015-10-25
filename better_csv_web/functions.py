__author__ = 'pridemai'
from models import File,ColumnMapping,SearchColumn
from better_csv_web.settings import *
import traceback
import time
from os import listdir
from os.path import isfile, join
from parse_functions import BetterCSV, binary_search
import time
DATA_DIR = "/data/"
MASTERS_DIR = "/results/"

def write_csv(filepath,rows):
    hs = open(filepath,"w+")
    for mline in rows:
        hs.write(",".join(mline)+"\r")

    hs.close()
def get_all_source_file_names():
    return File.objects.filter(is_master=False)

def get_all_master_file_names():
    return File.objects.filter(is_master=True)

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
    start = time.time()
    messages=[]
    for master in request.POST.getlist('master_files[]'):
        master_copy = BetterCSV().get_lists(BetterCSV().get_lines(open(BASE_DIR + DATA_DIR + master).read()))


        for file in request.POST.getlist('source_files[]'):
            print "Processing file"+file
            data_file = BetterCSV().get_lists(BetterCSV().get_lines(open(BASE_DIR + DATA_DIR + file).read()))
            # load the search columns
            master_search_columns = []
            for msc in SearchColumn.objects.filter(file=File.objects.get(filename=master)):
                master_search_columns.append(msc.column_id - 1)
            data_search_columns = []
            for dsc in SearchColumn.objects.filter(file=File.objects.get(filename=file)):
                data_search_columns.append(dsc.column_id - 1)
            # load the mappings
            mappings = {}
            for mapping in ColumnMapping.objects.filter(master_file=File.objects.get(filename=master),
                                                        source_file=File.objects.get(filename=file)):
                mappings[mapping.master_column_id - 1] = mapping.source_column_id - 1
            # actually execute and update
            results = iterate(master_copy, data_file, master_search_columns, data_search_columns, mappings, file)
            master_copy = results['data']
            messages.append(results['message'])


            write_csv(str(BASE_DIR+MASTERS_DIR+master.split(".")[0]+"_"+str(time.strftime("%d%m%Y"))+".csv"), master_copy)

    return {"messages": messages, "runtime":time.time()-start}




def update_row(master_row, data_row, column_mapping):
    for key,value in column_mapping.iteritems():

        master_row[key]=data_row[value] if len(data_row[value]) > 0 and data_row[value] != "0" else master_row[key]
    return master_row

def iterate(master_copy,data_copy, master_search_columns, data_search_columns, column_mapping, filname="N/A"):

    better_csv = BetterCSV()
    new_master = []
    found_count = 0
    for line in master_copy:
        for m in master_search_columns:
            found = False
            for d in data_search_columns:
                data_copy = sorted(data_copy, key=lambda x: x[d], reverse=False)
                results = binary_search(line, data_copy,m, d)
                found = results["result"]
                if found:
                    line = update_row(line, data_copy[results["index"]], column_mapping)
                    found_count = found_count +1
                    break
            if found:
                break
        new_master.append(line)

        # master_args=[]
        # for column in master_search_columns:
        #     master_args.append(line[column])
        # for d in data_copy:
        #     data_args =[]
        #     for column in data_search_columns:
        #         data_args.append(d[column])
        #     if better_csv.search(master_args, data_args) :
        #         line = update_row(line, d, column_mapping)
        #         found_count = found_count + 1You
        #         break
        # new_master.append(line)
    return {"data":new_master, "message": "%s count: %s" % (filname, found_count) }

def get_result_files():

    return [ f for f in listdir(BASE_DIR+MASTERS_DIR) if isfile(join(BASE_DIR+MASTERS_DIR,f)) ]

def get_all_files():
    return [ f for f in listdir(BASE_DIR+MASTERS_DIR) if isfile(join(BASE_DIR+MASTERS_DIR,f)) ] + [ f for f in listdir(BASE_DIR+DATA_DIR) if isfile(join(BASE_DIR+DATA_DIR,f)) ]

def get_file(filepath, filename):
    return open(filepath+filename)

def get_files_in_folder(filepath):
    return [ f for f in listdir(filepath) if isfile(join(filepath,f)) ]

def searchInFiles(request):
    search_results = []
    for file in request.POST.getlist('search_files[]'):
        rows =BetterCSV().get_lists(BetterCSV().get_lines(get_file("%s/%s/"%(BASE_DIR,request.POST['folder']))))
        i = 0
        while i < len(rows[0]):
            rows = sorted(rows, key=lambda x: x[i], reverse=False)
            results = binary_search(line, data_copy,m, d)


