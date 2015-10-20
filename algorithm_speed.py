__author__ = 'pridemai'
from parse_functions import BetterCSV
import time
from threading import Thread
from time import sleep
#searchable
master_copy = BetterCSV().get_lists(BetterCSV().get_lines(open("master_copy_updated_data.csv").read()))
firth_rixon=BetterCSV().get_lists(BetterCSV().get_lines(open("firth_rixon.csv").read()))
start=time.time()




#base
# for line in master_copy:
#     for f in firth_rixon:
#         if BetterCSV().search([line[1],line[10]], [f[16],f[17]]):
#             break

def threaded():
    found_count = 0
    for line in master_copy:
        negative_index = -1
        positive_index = 0
        middle_element = len(firth_rixon) /2 if len(firth_rixon) %2 == 0 else (len(firth_rixon)-1) /2
        found = False

        while positive_index < middle_element:
            # print str(positive_index)+","+str(negative_index)
            if BetterCSV().search([line[1],line[10]], [firth_rixon[positive_index][16],firth_rixon[positive_index][17],firth_rixon[negative_index][16],firth_rixon[negative_index][17]]):
                found_count = found_count+1
                break
            positive_index = positive_index +1
            negative_index = negative_index -1
    print found_count


threaded()
# thread = Thread(target = threaded, args = ( ))
# thread.start()
# thread.join()

end = time.time()
print end-start
