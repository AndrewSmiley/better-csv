__author__ = 'pridemai'
import time
from parse_functions import BetterCSV
new_lines = []

def iterate(sandy,master, input_file, master_columns, input_columns, input_parts,last_id):
    if len(master_columns) != len(input_columns):
        print "Column counts do not match"
        return
    better_csv=BetterCSV()
    missing_rows=[]
    # last_id = master[len(master)-1][0]
    for row in input_file:
        found = False
        for s in sandy:
            for part_column in input_parts:
                if better_csv.search([row[part_column]],[s[1],s[8]]):
                    found = True

            if found:
                break
        if not found:
            last_id = int(last_id)+1
            i = 0
            new_line = ['']*32
            new_line[0]=str(last_id)
            while i < len(master_columns):
                new_line[master_columns[i]]=row[input_columns[i]]
                i = i+1
            print "Adding new line with ID %s" % str(last_id)
            new_lines.append(new_line)

    # hs = open("master_test.csv","w")
    # for mline in master:
    #     hs.write(",".join(mline)+"\r")
    #
    # hs.close()




better_csv=BetterCSV()
master_copy = better_csv.get_lists(better_csv.get_lines(open("master_copy_updated_data.csv").read()))
firth_rixon=better_csv.get_lists(better_csv.get_lines(open("firth_rixon.csv").read()))
welded_ring = better_csv.get_lists(better_csv.get_lines(open("welded_ring.csv").read()))
mountain_top= better_csv.get_lists(better_csv.get_lines(open("mountain_top.csv").read()))
cfw = better_csv.get_lists(better_csv.get_lines(open("cfw.csv").read()))
suzhou= better_csv.get_lists(better_csv.get_lines(open("suzhou.csv").read()))
leap_tracker=better_csv.get_lists(better_csv.get_lines(open("leap_tracker.csv").read()))
leap_tracker_welded_ring_update=better_csv.get_lists(better_csv.get_lines(open("leap_tracker_welded_ring_update.csv").read()))
suzhou_min= better_csv.get_lists(better_csv.get_lines(open("suzhou_min.csv").read()))
tei= better_csv.get_lists(better_csv.get_lines(open("tei.csv").read()))
sandy = better_csv.get_lists(better_csv.get_lines(open("sandy.csv").read()))
cfw_lta = better_csv.get_lists(better_csv.get_lines(open("cfw_lta.csv").read()))
firth_rixson2 = better_csv.get_lists(better_csv.get_lines(open("firth_rixson2.csv").read()))
frisa_lta= better_csv.get_lists(better_csv.get_lines(open("frisa_lta.csv").read()))
ge_lta= better_csv.get_lists(better_csv.get_lines(open("ge_lta.csv").read()))
leap_and_passport1= better_csv.get_lists(better_csv.get_lines(open("leap_and_passport_rings1.csv").read()))
leap_and_passport2= better_csv.get_lists(better_csv.get_lines(open("leap_and_passport_rings2.csv").read()))
leap_and_passport3= better_csv.get_lists(better_csv.get_lines(open("leap_and_passport_rings3.csv").read()))
leap_tracker2= better_csv.get_lists(better_csv.get_lines(open("leap_tracker2.csv").read()))
welded_ring2= better_csv.get_lists(better_csv.get_lines(open("welded_ring2.csv").read()))
leap_tracker3= better_csv.get_lists(better_csv.get_lines(open("leap_tracker3.csv").read()))
mountain_top2= better_csv.get_lists(better_csv.get_lines(open("mountain_top2.csv").read()))

iterate(sandy,master_copy,firth_rixon,[1,2,15,16,19,26,28],[16,19,14,15,13,8,38],[16,17,18],master_copy[len(master_copy)-1][0])
iterate(sandy,master_copy,welded_ring,[1,6,7,16,18,19],[1,0,5,6,8,9],[1,2],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,mountain_top,[1,7,18,16,14],[0,1,3,5,7],[0],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,cfw,[1,7,18,19,16,14],[0,1,2,3,5,7],[0],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,suzhou,[1,2,6,5,7,9,11,13,14,23,3,28],[0,1,2,3,4,5,7,9,10,11,12,13],[0,6],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_tracker,[1,4,2,31,19,7,28],[1,2,4,8,9,30,36],[1,3],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_tracker_welded_ring_update,[1,2,31,19,7,16,14,28],[1,3,7,8,9,17,25,28],[1,2],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,suzhou_min,[1,2,6,5,7,9,11,13,14,23,3,28],[0,1,2,3,4,5,7,9,10,11,12,13],[0,6],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,tei,[1,2,3,5,6,7,9,11,12,13,14,22,23,28],[1,2,3,4,5,6,7,9,10,11,12,13,14,15],[1,8],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,cfw_lta,[1,7,18,19,16,14,22,23],[0,1,2,3,5,7,8,9],[0],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,firth_rixson2,[31,18,19,15,7,1,2,22,23,26,28],[10,11,12,13,14,15,19,28,29,7,32],[15,16,17,18],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,frisa_lta,[1,7,18,19,27],[2,6,9,11,17],[2,3],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,ge_lta,[26,1,31,18,19,15,7,2,16,28],[8,16,11,12,13,14,15,19,24,38],[16,17,18],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_and_passport1,[7,2,18,16,28],[0,6,8,10,20],[4,22],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_and_passport2,[7,2,18,16,14,1],[0,6,7,9,17,19],[4,19],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_and_passport3,[1,2,28],[1,2,8],[1],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_tracker2,[1,4,2,31,19,7,28],[1,2,4,8,9,30,36],[1,3],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,leap_tracker3,[1,2],[0,2],[0,1],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,welded_ring2,[1,7,16,18,19],[1,5,6,8,9],[1,2],new_lines[len(new_lines)-1][0])
iterate(sandy,master_copy,mountain_top2,[1,7,18,16,14],[0,1,3,5,7],[0],new_lines[len(new_lines)-1][0])
for line in new_lines:
    master_copy.append(line)
filename="master_test.csv"
hs = open(filename,"w")
for mline in master_copy:
    hs.write(",".join(mline)+"\r")

hs.close()

print "Added %s parts"% len(new_lines)