__author__ = 'pridemai'
import csv,sys
from parse_functions import BetterCSV
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

# firth_rixon=(better_csv.get_lines(open("firth_rixon.csv").read()))
# welded_ring = (better_csv.get_lines(open("welded_ring.csv").read()))
# mountain_top= (better_csv.get_lines(open("mountain_top.csv").read()))
# cfw = (better_csv.get_lines(open("cfw.csv").read()))
# suzhou= (better_csv.get_lines(open("suzhou.csv").read()))
# leap_tracker=(better_csv.get_lines(open("leap_tracker.csv").read()))
# leap_tracker_welded_ring_update=(better_csv.get_lines(open("leap_tracker_welded_ring_update.csv").read()))
# suzhou_min= (better_csv.get_lines(open("suzhou_min.csv").read()))
# tei= (better_csv.get_lines(open("tei.csv").read()))
# sandy = (better_csv.get_lines(open("sandy.csv").read()))

# firth_rixon_found = 0
# welded_ring_found = 0
# mountain_top_found = 0
# suzhou_found = 0
# cfw_found=0
# leap_tracker_found=0
# leap_tracker_welded_ring_update_found = 0
# suzhou_min_found = 0
# tei_found=0
# discrepancy_count = 0
# sandy_found=0
# not_found_count =0
# count = 0
# for line in sandy:
#     count = count+1
#     found = False
#     for f in firth_rixon:
#         # if line[1] in firth_rixon
#         if better_csv.search([line[1],line[8]], [f[16],f[17]]) or better_csv.search([f[16],f[17]],[line[1],line[8]]):
#             firth_rixon_found = firth_rixon_found+1
#             found = True
#             break
#     for w in welded_ring:
#         if better_csv.search([line[1],line[8]], [w[1],w[2]]) or better_csv.search([w[1],w[2]],[line[1],line[8]]):
#             welded_ring_found = welded_ring_found+1
#             found = True
#             break
#     for mt in mountain_top:
#         if better_csv.search([line[1],line[8]], [mt[0]]) or better_csv.search([mt[0]],[line[1],line[8]]):
#             mountain_top_found = mountain_top_found+1
#             found = True
#             break
#     for c in cfw:
#         if better_csv.search([line[1],line[8]], [c[0]]) or better_csv.search([c[0]],[line[1],line[8]]):
#             cfw_found = cfw_found+1
#             found = True
#             break
#     for s in suzhou:
#         if better_csv.search([line[1],line[8]], [s[0],s[6]]) or better_csv.search([s[0],s[6]],[line[1],line[8]]):
#             suzhou_found = suzhou_found+1
#             found = True
#             break
#     for l in leap_tracker:
#         if better_csv.search([line[1],line[8]], [l[1],l[3]]) or better_csv.search([l[1],l[3]], [line[1],line[8]]):
#             leap_tracker_found = leap_tracker_found+1
#             found = True
#             break
#     for l in leap_tracker_welded_ring_update:
#         if better_csv.search([line[1],line[8]], [l[1],l[2]]) or better_csv.search([l[1],l[2]], [line[1],line[8]]):
#             leap_tracker_welded_ring_update_found = leap_tracker_welded_ring_update_found+1
#             found = True
#             break
#     for l in suzhou_min:
#         if better_csv.search([line[1],line[8]], [l[0],l[6]]) or better_csv.search([l[0],l[6]],[line[1],line[8]]):
#             found = True
#             suzhou_min_found = suzhou_min_found +1
#             break
#     for t in tei:
#         if better_csv.search([line[1],line[8]], [t[1],t[8]]) or better_csv.search([t[1],t[8]],[line[1],line[8]] ):
#             found = True
#             tei_found = tei_found +1
#             break
#
#     if not found:
#
#         # print "Not found: %s,%s" % (line[1], line[8])
#         not_found_count = not_found_count+1


    # if not found:
    #     master_copy_lines.append(line)
    # if not found:
    #     master_copy_lines.append(line)

# print "Firth Rixson: %s/%s" % (firth_rixon_found, len(firth_rixon))
# print "Welded Ring: %s/%s" % (welded_ring_found, len(welded_ring))
# print "Mountain Top: %s/%s" % (mountain_top_found, len(mountain_top))
# print "CFW: %s/%s" % (cfw_found,len(cfw))
# print "Suzhou: %s/%s" % (suzhou_found, len(suzhou))
# print "Leap tracker: %s/%s" % (leap_tracker_found, len(leap_tracker))
# print "Leap tracker welded ring update: %s/%s" % (leap_tracker_welded_ring_update_found,len(leap_tracker_welded_ring_update))
# print "Suzhou Min: %s/%s" % (suzhou_min_found,len(suzhou_min))
# print "TEI: %s/%s" % (tei_found,len(tei))
# print "Not found: %s/%s" % (not_found_count, count)
# print "Total: %s" %sum([firth_rixon_found,welded_ring_found,mountain_top_found,cfw_found,suzhou_found,leap_tracker_found,leap_tracker_welded_ring_update_found,suzhou_min_found,tei_found])

firth_rixon_found = 0
welded_ring_found = 0
mountain_top_found = 0
suzhou_found = 0
cfw_found=0
leap_tracker_found=0
leap_tracker_welded_ring_update_found = 0
suzhou_min_found = 0
tei_found=0
discrepancy_count = 0
sandy_found=0
master_copy_lines=[]
changed_rows=[]
not_found_count = 0
for line in master_copy:
    found = False
    # print line[0]
    for f in firth_rixon:
        if better_csv.search([line[1],line[10]], [f[16],f[17]]) or better_csv.search([f[16],f[17]],[line[1],line[10]]):
            fuck.append("Found part %s in Firth Rixson" % str("ID: "+line[0]))
            firth_rixon_found = firth_rixon_found +1
            #billet diameter
            if line[15] != f[14] or line[18] != f[12] or line[16] != f[15] or line[19] != f[13] or line[31] != f[11]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            line[15]= f[14]

            #alloy
            line[18] = f[12]
            #weight
            line[16] = f[15]
            #spec
            line[19]= f[13]
            #alloy family
            line[31] = f[11]
            found=True
            master_copy_lines.append(line)

            break
    if not found:
        master_copy_lines.append(line)
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for w in welded_ring:
        if better_csv.search([line[1],line[10]], [w[1],w[2]]) or better_csv.search([w[1],w[2]],[line[1],line[10]]):
            fuck.append("Found part %s in Welded Ring" % str("ID: "+line[0]))
            welded_ring_found = welded_ring_found+1

            if line[18] != w[8] or line[16] != w[6] or line[19] != w[9] or line[7] != w[5]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            #a lloy
            line[18]=w[8]
            #weight
            line[16]=w[6]
            #spec
            line[19]=w[9]
            #engine program
            line[7]=w[5]
            found = True
            master_copy_lines.append(line)
            break
    if not found:
        master_copy_lines.append(line)
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
# master_copy = master_copy_lines
# master_copy_lines = []
# for line in master_copy:
#     found = False
#     for s in sandy:
#         if better_csv.search([line[1],line[10]], [s[1],s[8]]) or better_csv.search([s[1],s[8]],[line[1],line[10]]):
#             sandy_found = sandy_found+1
#             fuck.append("Found part %s in Sandy" % str("ID: "+line[0]))
#             if line[7] != s[6] or line[11] != s[9] or line[14] != s[12]:
#                 if line[0] not in changed_rows:
#                     changed_rows.append(line[0])
#                     #engine program
#             line[7]=s[6]
#             #raw material type
#             line[11]=s[9]
#             line[14]=s[12]
#             found = True
#             master_copy_lines.append(line)
#             break
#     if not found:
#         master_copy_lines.append(line)

master_copy = master_copy_lines
master_copy_lines = []


for line in master_copy:
    found = False
    for mt in mountain_top:
        if better_csv.search([line[1],line[10]], [mt[0]]) or better_csv.search([mt[0]],[line[1],line[10]]):
            mountain_top_found = mountain_top_found+1
            fuck.append("Found part %s in Mountain Top" % str("ID: "+line[0]))
            break
            if line[18] != mt[3] or line[16] != mt[5] or line[7] != mt[1]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            #allow
            line[18] = mt[3]
            #weight
            line[16] = mt[5]
            #engine program
            line[7] = mt[1]

            found = True
            master_copy_lines.append(line)
    if not found:
        master_copy_lines.append(line)
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for c in cfw:
        if better_csv.search([line[1],line[10]], [c[0]]) or better_csv.search([c[0]],[line[1],line[10]]):
            cfw_found = cfw_found+1
            fuck.append("Found part %s in CFW" % str("ID: "+line[0]))
            found = True
            if line[7] != c[1] or line[18] != c[2] or line[19] != c[3] or line[15] != c[4] or line[16] != c[5] or line[14] != c[7]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            #engine program
            line[7] = c[1]
            #alloy
            line[18] = c[2]
            #spec
            line[19]=c[3]
            #billet diameter
            line[15]=c[4]
            #weight
            line[16]=c[5]
            #yield
            line[14]=c[7]


            master_copy_lines.append(line)

            break
    if not found:
        master_copy_lines.append(line)

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
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for s in suzhou:

        if better_csv.search([line[1],line[10]], [s[0],s[6]]) or better_csv.search([s[0],s[6]],[line[1],line[10]]):
            fuck.append("Found part %s in Suzhou" % str("ID: "+line[0]))
            suzhou_found = suzhou_found+1
            if line[7] != s[4] or line[11] != s[7] or line[14] != s[10]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            line[7]=s[4]
            line[11] = s[7]
            line[14] = s[10]
            # # line[18] = s[2]
            # line[19] = s[3]
            # line[16] = s[5]
            found = True
            master_copy_lines.append(line)
            break
    if not found:
        master_copy_lines.append(line)
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for l in leap_tracker:
        if better_csv.search([line[1],line[10]], [l[1],l[3]]) or better_csv.search([l[1],l[3]], [line[1],line[10]]):
            fuck.append("Found part %s in Leap Tracker" % str("ID: "+line[0]))
            leap_tracker_found = leap_tracker_found+1
            #qpe
            if line[4] != l[2] or line[31] !=l[8] or line[19]!=l[9] or line[7] != l[30]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            #engine program
            line[4]=l[2]
            #alloy family
            line[31]=l[8]
            #spec
            line[19] = l[9]
            line[7]=l[30]
            found = True
            master_copy_lines.append(line)
            break
    if not found:
        master_copy_lines.append(line)
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for l in leap_tracker_welded_ring_update:
        if better_csv.search([line[1],line[10]], [l[1],l[2]]) or better_csv.search([l[1],l[2]], [line[1],line[10]]):
            fuck.append("Found part %s in Leap Tracker Welded Ring" % str("ID: "+line[0]))
            leap_tracker_welded_ring_update_found = leap_tracker_welded_ring_update_found+1
            if line[16] != l[17] or line[19] != l[8] or line[31] != l[7] or line[7] != l[9] or line[14] != l[25]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
                            #weight
            line[16] = l[17]
            #spec
            line[19] = l[8]
            #alloy family
            line[31]=l[7]
            #engine program
            line[7]=l[9]
            #yield
            line[14]=l[25]
            master_copy_lines.append(line)
            found=True
            break
    if not found:
        master_copy_lines.append(line)
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for l in suzhou_min:
        if better_csv.search([line[1],line[10]], [l[0],l[6]]) or better_csv.search([l[0],l[6]],[line[1],line[10]]):
            # leap_tracker_welded_ring_update_found = leap_tracker_welded_ring_update_found+1
            #engine program
            fuck.append("Found part %s in Suzhou Min" % str("ID: "+line[0]))
            if line[7] != l[4] or line[11] != l[7] or line[14]!=l[10]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])

            # discrepancy_count = discrepancy_count + 1
            line[7]=l[4]
            #raw material type
            line[11]=l[7] #L7
            #yield
            line[14]=l[10]
            suzhou_min_found = suzhou_min_found+1
            found = True
            master_copy_lines.append(line)

            break
    if not found:
        master_copy_lines.append(line)
master_copy = master_copy_lines
master_copy_lines = []
for line in master_copy:
    found = False
    for l in tei:
        if better_csv.search([line[1],line[10]], [l[1],l[8]]) or better_csv.search([l[1],l[8]],[line[1],line[10]] ):
            fuck.append("Found part %s in TEI" % str("ID: "+line[0]))
            tei_found = tei_found +1
            found = True

            if line[7] != l[6] or line[11] != l[9] or line[14]!=l[12]:
                if line[0] not in changed_rows:
                    changed_rows.append(line[0])
            # discrepancy_count = discrepancy_count + 1
            line[7]=l[6]
            line[11]=l[9]
            line[14]=l[12]
            master_copy_lines.append(line)
            break
    if not found:
        master_copy_lines.append(line)

print "Firth Rixson: %s" % firth_rixon_found
print "Welded Ring: %s" % welded_ring_found
print "Mountain Top: %s" % mountain_top_found
print "CFW: %s" % cfw_found
print "Suzhou: %s" % suzhou_found
print "Leap tracker: %s" % leap_tracker_found
print "Leap tracker welded ring update: %s" % leap_tracker_welded_ring_update_found
print "Suzhou Min: %s" % suzhou_min_found
print "TEI: %s" % tei_found
# print "Sandy: %s" % sandy_found
print "Total: %s" %sum([firth_rixon_found,welded_ring_found,mountain_top_found,cfw_found,suzhou_found,leap_tracker_found,leap_tracker_welded_ring_update_found,suzhou_min_found,tei_found])


hs = open("this_is_it_6.csv","w")
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
