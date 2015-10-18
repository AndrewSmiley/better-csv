__author__ = 'pridemai'
import csv,sys
from parse_functions import BetterCSV
from excel_functions import iterate
better_csv=BetterCSV()
master_copy = better_csv.get_lists(better_csv.get_lines(open("master_copy_updated_data.csv").read()))
# master_copy_lines=[]
# for line in master_copy:
#     if len(line) < 32:
#         line.append('0')
#
#     master_copy_lines.append(line)
# hs = open("master_copy_new.csv","w")
# for line in master_copy_lines:
#     hs.write(",".join(line)+"\r")
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
print "files loaded"

master_copy = iterate(master_copy, firth_rixon, [1,10],[16,17],{18:12, 16:15,19:13,31:11},"Firth Rixson")
master_copy = iterate(master_copy,welded_ring,[1,10],[1,2],{18:8,16:6,19:9,7:5}, "Welded Ring 1")
# master_copy = iterate(master_copy, raw_qpe,[1,10],[0],{4:6},"Raw QPE")
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
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for g in ge_lta:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         #16,17,18 the full parts search
#         if better_csv.search([line[1], line[10]], [g[16],g[17],g[18]]) or better_csv.search([g[16],g[17],g[18]], [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             ge_lta_count = ge_lta_count + 1
#             # found_parts = found_parts + 1
#             line[31] = g[11]
#             line[18] = g[12]
#             line[19] = g[13]
#             line[15] = g[14]
#             line[7] = g[15]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for l in leap_and_passport1:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [l[22], l[4]]) or better_csv.search([l[22], l[4]],
#                                                                                       [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             leap_and_passport1_count = leap_and_passport1_count + 1
#             # found_parts = found_parts + 1
#             line[7] = l[0]
#             line[18] = l[8]
#             line[16] = l[10]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for l in leap_and_passport2:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [l[19], l[4]]) or better_csv.search([l[19], l[4]],
#                                                                                       [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             leap_and_passport2_count = leap_and_passport2_count + 1
#             # found_parts = found_parts + 1
#             line[7] = l[0]
#             line[18] = l[7]
#             line[16] = l[9]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for l in leap_and_passport3:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [l[1]]) or better_csv.search([l[1]], [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             leap_and_passport3_count = leap_and_passport3_count + 1
#             # found_parts = found_parts + 1
#             # line[7]=l[0]
#             # line[18]=l[7]
#             # line[16]=l[9]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for l in leap_tracker2:
#          #        f[6]
#          # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#          if better_csv.search([line[1], line[10]], [l[1], l[3]]) or better_csv.search([l[1], l[3]],
#                                                                                       [line[1], line[10]]):
#              # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#              found = True
#              # firth_rixon_count = firth_rixon_count +1
#              leap_tracker2_count = leap_tracker2_count + 1
#              # found_parts = found_parts + 1
#              line[4] = l[2]
#              line[31] = l[8]
#              line[19] = l[9]
#              line[7] = l[30]
#              master_copy_lines.append(line)
#              break
#          else:
#              continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for l in leap_tracker3:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [l[0], l[1]]) or better_csv.search([l[0], l[1]], [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             leap_tracker3_count = leap_tracker3_count + 1
#             # found_parts = found_parts + 1
#             # line[4]=l[2]
#             # line[31]=l[8]
#             # line[19]=l[9]
#             # line[7]=l[30]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for m in mountain_top2:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [m[0]]) or better_csv.search([m[0]], [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             mountain_top2_count = mountain_top2_count + 1
#             # found_parts = found_parts + 1
#             line[7] = m[1]
#             line[18] = m[3]
#             line[17] = 'lbs'
#             line[16] = m[5]
#             line[14] = '1=' + m[7]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for w in welded_ring2:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [w[1], w[2]]) or better_csv.search([w[1], w[2]], [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             welded_ring2_count = welded_ring2_count + 1
#             # found_parts = found_parts + 1
#             line[7] = w[5]
#             line[16] = w[6]
#             line[18] = w[8]
#             line[19] = w[9]
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)
#
# """
# billet_diameter = line[15]
# yield_value = line[14]
# weight = line[16]
# weight_type = line[17]
# alloy = line[18]
# spec = line[19]
# qpe = line[4]
# raw_material_type = line[11]
# alloy_family = line[31]
# engine_program = line[7]
# engine_model = line[8]
# flash_welding_permitted = line[20]
# """
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for g in ge_lta2:
#         #        f[6]
#         # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
#         if better_csv.search([line[1], line[10]], [g[1],g[2]]) or better_csv.search([g[1],g[2]], [line[1], line[10]]):
#             # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
#             found = True
#             # firth_rixon_count = firth_rixon_count +1
#             line[2]=g[3]
#             line[18]=g[7]
#             line[16]=g[9]
#             line[19]=g[8]
#             line[7]=g[13]
#             line[15]=g[5]
#
#
#             ge_lta2_count=ge_lta2_count+1
#             master_copy_lines.append(line)
#             break
#         else:
#             continue
#     if not found:
#         master_copy_lines.append(line)

# print "Raw QPE: %s" % raw_qpe_count
print "Firth Rixson: %s" % firth_rixon_found
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


hs = open("this_is_it_1006.csv","w")
for mline in master_copy_lines:
    hs.write(",".join(mline)+"\r")

hs.close()

hs = open("fuck2.txt","w")
for f in fuck:
    # hs.write(",".join(mline)+"\r")
    hs.write(f+"\r")

hs.close()
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
