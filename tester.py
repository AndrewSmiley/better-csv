__author__ = 'pridemai'
import csv,sys
from parse_functions import BetterCSV
from excel_functions import iterate
import time
better_csv=BetterCSV()
master_copy = better_csv.get_lists(better_csv.get_lines(open("master_test.csv").read()))
# master_copy_lines=[]
# for line in master_copy:
#     if len(line) < 32:
#         line.append('0')
#
#     master_copy_lines.append(line)
# hs = open("master_copy_new.csv","w")
# for line in master_copy_lines:
#     hs.write(",".join(line)+"\r")
start=time.time()
fuck=[]
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


#all the new stuff 9/21
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
raw_qpe= better_csv.get_lists(better_csv.get_lines(open("raw_qpe.csv").read()))
ge_lta2= better_csv.get_lists(better_csv.get_lines(open("ge_lta2.csv___jb_bak___").read()))

#new stuff as of 10/18
afsrr_leap_tracker= better_csv.get_lists(better_csv.get_lines(open("afsrr_leap_tracker.csv").read()))
print "loaded afsrr"
fontana= better_csv.get_lists(better_csv.get_lines(open("fontana.csv").read()))
print "loaded fontana"
frisa_leap_rings_tracker= better_csv.get_lists(better_csv.get_lines(open("frisa_leap_rings_tracker.csv").read()))
print "loaded frisa leap"
ge_leap_lta_tracker=better_csv.get_lists(better_csv.get_lines(open("ge_leap_lta_tracker.csv").read()))
print "loaded ge lta leap"
leap_program_updates=better_csv.get_lists(better_csv.get_lines(open("leap_program_updates.csv").read()))
print "loaded leap program updates"
leap_weekly_updates=better_csv.get_lists(better_csv.get_lines(open("leap_weekly_updates.csv").read()))
print "loaded leap weekly updates"
print "files loaded"
master_copy = iterate(master_copy, raw_qpe,[1,10],[0],{4:6, 3:2},"Raw QPE")

master_copy = iterate(master_copy, afsrr_leap_tracker, [1,10], [1,3], {4:2,19:12,31:18,7:19}, "AFSRR Leap")
master_copy = iterate(master_copy, fontana, [1,10],[1,3],{4:2,31:8,19:9,7:16}, "Fontana")
master_copy = iterate(master_copy, ge_leap_lta_tracker, [1,10], [1,2], {31:7,19:8,16:9,7:13}, "GE Leap LTA tracker")
master_copy = iterate(master_copy, frisa_leap_rings_tracker, [1,10], [1,2], {2:3,31:4,19:5, 7:6}, "Frisa leap rings tracker")
master_copy = iterate(master_copy, leap_program_updates, [1,10], [1,2], {31:7,19:8,7:9,16:17,14:25})
master_copy = iterate(master_copy, leap_weekly_updates, [1,10], [1,2], {31:7, 19:8, 16:17})

master_copy = iterate(master_copy, firth_rixon, [1,10],[16,17],{18:12, 16:15,19:13,31:11},"Firth Rixson")
master_copy = iterate(master_copy,welded_ring,[1,10],[1,2],{18:8,16:6,19:9,7:5}, "Welded Ring 1")
master_copy = iterate(master_copy,sandy, [1,10],[1,8],{7:6,11:9,14:12}, "Sandy's Data")
master_copy = iterate(master_copy,mountain_top, [1,10],[0], {18:3,16:5,7:1}, "Mountain Top")
master_copy = iterate(master_copy,cfw,[1,10],[0], {7:1, 18:2, 19:3, 15:4, 16:5, 14:7}, "CFW 1")
master_copy = iterate(master_copy,suzhou,[1,10],[0,6], {7:4,11:7,14:10}, "Suzhou 1")
master_copy = iterate(master_copy,leap_tracker,[1,10],[1,3], {4:2,31:8,19:9,7:30}, "LEAP tracker 1")
master_copy = iterate(master_copy, leap_tracker_welded_ring_update,[1,10],[1,2],{16:17,19:8,31:7,7:9,14:25}, "LEAP welded ring update")
master_copy = iterate(master_copy,tei,[1,10],[1,8],{7:6,11:9,14:12}, "TEI")
master_copy = iterate(master_copy,cfw_lta,[1,10],[0], {7:1,18:2,19:3,16:5,14:7}, "CFW LTA")
master_copy = iterate(master_copy, firth_rixson2, [1,10],[15,16,17,18], {31:10,18:11,19:12,15:13,7:14}, "Firth Rixson 2")
master_copy = iterate(master_copy,frisa_lta,[1,10],[2,3], {7:6,18:9,19:11}, "Frisa LTA")
master_copy = iterate(master_copy,ge_lta, [1,10],[16,17,18], {31:11,18:12,19:13,15:14,7:15}, "GE LTA")
master_copy = iterate(master_copy,leap_and_passport1, [1,10], [22, 4], { 7:0,18:8,16:10}, "Leap Passport 1")
master_copy = iterate(master_copy, leap_and_passport2, [1,10],[19,4], {7:0, 18:7,16:9}, "Leap Passport 2")
master_copy = iterate(master_copy,leap_and_passport3, [1,10], [1], {7:0, 18:7,16:9}, "Leap Passport 3")
master_copy = iterate(master_copy,leap_tracker2, [1,10], [1,3], {4:2,31:8, 19:9, 7:30}, "Leap Tracker 2")
master_copy = iterate(master_copy, leap_tracker3, [1,10], [0,1], {}, "Leap Tracker 3")
master_copy = iterate(master_copy, mountain_top2, [1,10], [0], {7:1, 18:3,16:5, 14:7}, "Mountain Top 2")
master_copy = iterate(master_copy, welded_ring2, [1,10], [1,2], {7:5, 16:6, 18:8, 19:9}, "Welded Ring 2")
master_copy = iterate(master_copy,ge_lta2, [1,10],[1,2], {2:3, 18:7, 16:9, 19:8, 7:13, 15:5}, "GE LTA 2")
"""
billet_diameter = line[15]
yield_value = line[14]
weight = line[16]
weight_type = line[17]
alloy = line[18]
spec = line[19]
qpe = line[4]
raw_material_type = line[11]
alloy_family = line[31]
engine_program = line[7]
engine_model = line[8]
flash_welding_permitted = line[20]
"""



# print "Raw QPE: %s" % raw_qpe_count
# print "Firth Rixson: %s" % firth_rixon_found
# print "Welded Ring: %s" % welded_ring_found
# print "Mountain Top: %s" % mountain_top_found
# print "CFW: %s" % cfw_found
# print "Suzhou: %s" % suzhou_found
# print "Leap tracker: %s" % leap_tracker_found
# print "Leap tracker welded ring update: %s" % leap_tracker_welded_ring_update_found
# print "Suzhou Min: %s" % suzhou_min_found
# print "TEI: %s" % tei_found
# print "CFW LTA: %s" % cfw_lta_count
# print "Firth Rixson 2: %s" % firth_rixson2_count
# print "Frisa LTA: %s" % frisa_lta_count
# print "GE LTA: %s" % ge_lta_count
# print "Leap Passport Sheet 1: %s" % leap_and_passport1_count
# print "Leap Passport Sheet 2: %s" % leap_and_passport2_count
# print "Leap Passport Sheet 3: %s" % leap_and_passport3_count
# print "Leap Tracker 2: %s" % leap_tracker2_count
# print "Leap Tracker 3: %s" % leap_tracker3_count
# print "Mountain Top 2: %s" % mountain_top2_count
# print "Welded Ring Count: %s" % welded_ring2_count
# print "GE LTA 2 Count: %s" % ge_lta2_count
# print "Sandy: %s" % sandy_found
# print "Total: %s" %sum([firth_rixon_found,welded_ring_found,mountain_top_found,cfw_found,suzhou_found,leap_tracker_found,leap_tracker_welded_ring_update_found,suzhou_min_found,tei_found])


hs = open("this_is_it_101.csv","w")
for mline in master_copy:
    hs.write(",".join(mline)+"\r")

hs.close()

end = time.time()
print end-start
"""
Ignore this
"""
# updated= better_csv.get_lists(better_csv.get_lines(open("this_is_it_3.csv").read()))
# changed_row_count = 0
# updates=[]
# for u in updated:
#     # print ("checking updates")
#     for l in master_copy:
#         if u[0] == l[0] and u[0] in changed_rows:
#             updates.append("Changes detected in row %s. Values changed- Billet Diameter: %s=>%s, Alloy: %s=>%s,"
#                                " Weight: %s=>%s, Weight Type: %s=>%s, Spec: %s=>%s, Yield: %s=>%s,"
#                                " QPE: %s=>%s, R/M Type: %s=>%s, Alloy Family: %s=>%s, Engine Program: %s=>%s" % (u[0], l[15], u[15], l[18],u[18], l[16], u[16],l[17],u[17],
#                                                                                           l[19], u[19],l[14],u[14],l[4],u[4],l[11],u[11],l[31],u[31],l[7],u[7]))
#             changed_row_count = changed_row_count+1
#             #billet diameter
#             # line[15]= f[14]
#             #alloy
#             # line[18] = f[12]
#             #weight
#             # line[16] = f[15]
#             #spec
#             # line[19]=/ f[13]
#
#
#
#     # print "".join(line)
#
#
# hs = open("updates.txt","w")
# for p in updates:
#     hs.write(p+"\r")
#
# hs.close()
# print "Changed row count: %s/%s" % (len(changed_rows),sum([firth_rixon_found,welded_ring_found,mountain_top_found,cfw_found,suzhou_found,leap_tracker_found,leap_tracker_welded_ring_update_found,suzhou_min_found,tei_found]))

# print "Discrepancy count: %s" % discrepancy_count
# print (sum([firth_rixon_found,welded_ring_found,mountain_top_found,cfw_found,suzhou_found,leap_tracker_found,leap_tracker_welded_ring_update_found,suzhou_min_found,tei_found]) - discrepancy_count)
# search(["2463M43P05",""], ["2463M43P05-AS02","2463M43P05JEKQ"])
