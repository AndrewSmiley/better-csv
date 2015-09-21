__author__ = 'pridemai'
from parts import Part
from parse_functions import *
import csv


#here's the shit
#fuck
better_csv = BetterCSV()
# master_copy = get_lists(get_lines())
master_copy = better_csv.get_lists(better_csv.get_lines(open("master_copy_updated_data.csv").read()))
firth_rixon=better_csv.get_lists(better_csv.get_lines(open("firth_rixon.csv").read()))
# firth_rixon = get_lists(get_lines(open().read()))
welded_ring = better_csv.get_lists(better_csv.get_lines(open("welded_ring.csv").read()))
mountain_top= better_csv.get_lists(better_csv.get_lines(open("mountain_top.csv").read()))
cfw = better_csv.get_lists(better_csv.get_lines(open("cfw.csv").read()))
# sandy= get_lists(get_lines(open("sandy.csv").read()))
suzhou= better_csv.get_lists(better_csv.get_lines(open("suzhou.csv").read()))
leap_tracker=better_csv.get_lists(better_csv.get_lines(open("leap_tracker.csv").read()))
leap_tracker_welded_ring_update=better_csv.get_lists(better_csv.get_lines(open("leap_tracker_welded_ring_update.csv").read()))
# suzhou_master=get_lists(get_lines(open("suzou_master.csv").read()))
suzhou_min= better_csv.get_lists(better_csv.get_lines(open("suzhou_min.csv").read()))
tei= better_csv.get_lists(better_csv.get_lines(open("tei.csv").read()))
#all the new stuff 9/21
cfw_lta = better_csv.get_lists(better_csv.get_lines(open("cfw_lta.csv").read()))
firth_rixson2 = better_csv.get_lists(better_csv.get_lines(open("firth_rixson2.csv").read()))
frisa_lta= better_csv.get_lists(better_csv.get_lines(open("frisa_lta.csv").read()))
ge_lta= better_csv.get_lists(better_csv.get_lines(open("ge_lta.csv").read()))
leap_and_passport1= better_csv.get_lists(better_csv.get_lines(open("leap_and_passport_rings1.csv").read()))
leap_and_passport2= better_csv.get_lists(better_csv.get_lines(open("leap_and_passport_rings2.csv").read()))
leap_and_passport3= better_csv.get_lists(better_csv.get_lines(open("leap_and_passport_rings3.csv").read()))
leap_tracker2= better_csv.get_lists(better_csv.get_lines(open("leap_tracker2.csv").read()))
leap_tracker3= better_csv.get_lists(better_csv.get_lines(open("leap_tracker3.csv").read()))
mountain_top2= better_csv.get_lists(better_csv.get_lines(open("mountain_top2.csv").read()))
welded_ring2= better_csv.get_lists(better_csv.get_lines(open("welded_ring2.csv").read()))
master_copy_lines = []
m_found = 0
# for m in mountain_top:
#     found = False
#     for l in master_copy:
#         if m[0] in l[1] or m[0] in l[10]:
#             found = True
#             m_found = m_found+1
#             break
#
#     print ("found %s " % m[0] if found else "not found %s" % m[0])

# counter = 0
# for line in firth_rixon[0]:
#     print "[{0}] {1}".format(counter, line)
#     counter +=1
#
updated_parts=[]
mountain_top_count = 0
firth_rixon_count = 0
welded_ring_count = 0
unfound_parts = 0
leap_tracker_welded_ring_update_count = 0
leap_tracker_count =0
suzhou_count = 0
suzhou_min_count=0
tei_count=0
found_parts =0
total_parts=0
cfw_count =0
# lt = []
# for l in leap_tracker:
#     if l[1] + "/"+l[3] not in lt:
#         lt.append(l[1]+"/"+l[3])
#
# print len(lt)
#
#
# leap_tracker_found_parts= []
# for m in master_copy:
#     # print "master copy %s" %m[0]
#     found = False
    # if not found:
    #     for l in leap_tracker:
    #         # print "leap tracker welded ring %s" %l[0]
    #         # if m[1] in l[1]+"/"+l[3] or m[10] in l[1]+"/"+l[3] and (len(l[1]) > 4 and len(l[3]) > 4):
    #         if search([m[1], m[10]], [l[1],l[3]]):
    #         # if (m[1] in l[1]) or  (m[10] in l[1]) or (m[1] in l[3]) or  (m[10] in l[3]):
    #             leap_tracker_found_parts.append("Found leap tracker part: query %s,%s in %s" % (m[1],m[10],l[1]+"/"+l[3]))
    #             # found = True
    #             break
#     if not found:
#         for l in leap_tracker_welded_ring_update:
#             if search([m[1], m[10]], [l[1],l[2]]):
#                 leap_tracker_found_parts.append("Found leap tracker part: query %s,%s in %s" % (m[1],m[10],l[1]+"/"+l[2]))
#                 # found = True
#                 break
# #
# #
# for lt in leap_tracker_found_parts:
#     print (lt)
# print(len(leap_tracker_found_parts))
#leap_tracker_parts = []
#print "Trying to find leap tracker welded ring update"
# for l in leap_tracker_welded_ring_update:
#
#     for m in master_copy:
#         # if (l[1] in m[1]) or  (l[1] in m[10]) or (l[2] in m[1]) or  (l[2] in m[10]):
#         if (m[1] in l[1]) or  (m[10] in l[1]) or (m[1] in l[2]) or  (m[10] in l[2]):
#             leap_tracker_parts.append("Found leap tracker welded ring part: %s" % m[1])



#
# for lp in leap_tracker_parts:
#     print lp

# print("Here's the updated parts")
#
for line in master_copy:
    total_parts = total_parts +1
    # print "working a line"
    # p = Part()
    # p.id = line[0]
    # p.part_number = line[1]
    # p.nomeclature = line[2]
    # p.qpa = line[3]
    # p.qpe = line[4]
    # p.ge_neg = line[5]
    # p.finsihed_part_supplier = line[6]
    # p.engine_program = line[7]
    # p.engine_model = line[8]
    # p.this_year_quantity = line[9]
    # p.part_type = line[10]
    # p.raw_material_type = line[11]
    # p.raw_material_supplier = line[12]
    # p.plant = line[13]
    # p.yield_value = line[14]
    # p.billet_diameter = line[15]
    # p.weight = line[16]
    # p.weight_type = line[17]
    # p.alloy = line[18]
    # p.spec = line[19]
    # p.flash_welding_permitted = line[20]
    # p.e_r_n = line[21]
    # p.raw_material_unit_price_last_year = line[22]
    # p.raw_material_unit_price_this_year = line[23]
    # p.po_ammended = line[24]
    # p.this_year_raw_material_delta = line[25]
    # p.this_year_material_deflation = line[26]
    # p.this_year_material_extended_value = line[27]
    # p.machine_part_comments = line[28]
    # p.leap_pp = line[29]
    # p.chip_revert_part = line[30]



    #so now that we have that
    # if "Firth_Rixson" == line[12]:

        #so now we can search for the part number
    found = False
    # if (line[16] == '0' or line[16] == '' or line[16] == '#N/A') and (line[15] =='0' or line[15] == ''  or line[15] == '#N/A') and (line[18] =='0' or line[18] == ''  or line[18] == '#N/A'):

    # print ("we found firth rixson with missing data")
    if not found:
        for f in firth_rixon:
            #        f[6]
            # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
            if better_csv.search([line[1],line[10]], [f[16],f[17]]) or better_csv.search([f[16],f[17]],[line[1],line[10]]):
                updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
                found = True
                firth_rixon_count = firth_rixon_count +1
                found_parts=found_parts +1
                #billet diameter
                line[15]= f[14]
                #alloy
                line[18] = f[12]
                #weight
                line[16] = f[15]
                #spec
                line[19]= f[13]
                master_copy_lines.append(line)
                break
            else:
                continue

                    # if found:
                    # print "we found info for part number {0}".format(line[1])


        #if (line[16] == '0' or line[16] == '' or line[16] == '#N/A') and (line[15] =='0' or line[15] == ''  or line[15] == '#N/A') and (line[18] =='0' or line[18] == ''  or line[18] == '#N/A'):
        # if True:
        # print("We found welded_ring with missing data")
    if not found:    # found=False
        for w in welded_ring:
            # if (line[10] in w[1] and line [10] != '' and len(line[10]) > 2) or (line[1] in w[1] and line [1] != '' and len(line[1]) > 2) or (line[10] in w[2] and line [10] != '' and len(line[10]) > 2) or (line[1] in w[2] and line [1] != '' and len(line[1]) > 2):
            if better_csv.search([line[1],line[10]], [w[1],w[2]]) or better_csv.search([w[1],w[2]],[line[1],line[10]]):
                updated_parts.append("Found in Welded ring: {0}. Values Inserted: Alloy: {1} Weight: {2} Spec: {3}, ID: {4}".format(line[10], w[8], w[6], w[9], line[0]))
                found=True
                welded_ring_count = welded_ring_count +1
                found_parts=found_parts +1
                #alloy
                line[18]=w[8]
                #weight
                line[16]=w[6]
                #spec
                line[19]=w[9]
                master_copy_lines.append(line)
                break
            # if found:
            #     print("We found data for part {0}".format(line[1]))




    if not found:

        #if (line[16] == '0' or line[16] == '' or line[16] == '#N/A') and (line[15] =='0' or line[15] == ''  or line[15] == '#N/A') and (line[18] =='0' or line[18] == ''  or line[18] == '#N/A'):

        # print
        if not found:
            found_part = False
            #checking the mountain top CSV
            # print "checking mountain top for part %s" % line[1]
            for mt in mountain_top:

                # if line[10] in m[1] and line [10] != '' and len(line[10]) > 2:
                #         updated_parts.append("Found in Mountain Top: {0}, values injected: Alloy {1}, Weight: {2}, ID: {3}".format(line[10], m[3], m[5], line[0]))
                #         found_part=True
                #         found=True
                #         #only alloy and weight are available from this one
                #         line[18]=m[3]
                #         line[16]=m[5]
                #         break

                # if (line[10] in m[0] and line [10] != '') or (line[1] in m[0] and line [1] != '') :
                if better_csv.search([line[1],line[10]], [mt[0]]) or better_csv.search([mt[0]],[line[1],line[10]]):
                    updated_parts.append(
                        "Found in Mountain Top: {0}, values injected: Alloy {1}, Weight: {2}, ID: {3}".format(
                            "(PN: %s PT %s" % (line[1], line[10]), mt[3], mt[5], line[0]))
                    mountain_top_count = mountain_top_count + 1
                    found_parts = found_parts + 1
                    m_found = m_found + 1
                    found_part = True
                    found = True
                    #only alloy and weight are available from this one
                    line[18] = mt[3]
                    line[16] = mt[5]
                    master_copy_lines.append(line)
                    break
                    # else:
                    #     if line[1] in m[1] and line [10] != '' and len(line[1]) > 2:
                    #         updated_parts.append("Found in Mountain Top: {0}, values injected: Alloy {1}, Weight: {2}, ID: {3}".format(line[1], m[3], m[5], line[0]))
                    #         found_part=True
                    #         found=True
                    #         #only alloy and weight are available from this one
                    #         line[18]=m[3]
                    #         line[16]=m[5]
                    #         break
                    # if found_part

                    #checking CFW now

        if not found:
            found_part = False
            # print "checking CFW for part %s" % line[1]
            for c in cfw:
                # if line[10] in c[1] and line [10] != '' and len(line[10]) > 2:
                if better_csv.search([line[1],line[10]], [c[0]]) or better_csv.search([c[0]],[line[1],line[10]]):
                    found_part = True
                    found = True
                    found_parts = found_parts + 1
                    updated_parts.append(
                        "Found in CFW {0}. Values inserted: Alloy {1}, Spec {2}, Weight {3}, ID: {4}".format(line[10],
                                                                                                             c[2], c[3],
                                                                                                             c[5],
                                                                                                             line[0]))
                    cfw_count = cfw_count + 1
                    line[18] = c[2]
                    line[19] = c[3]
                    line[16] = c[5]
                    master_copy_lines.append(line)
                    break
                    # if not found:
                    #     found_part=False
                    #     # print "checking SANDY for part %s" % line[1]
                    #     for c in sandy:
                    #         if line[10] in c[1] and line [10] != '' and len(line[10]) > 2:
                    #             found_part=True
                    #             found=True
                    #             updated_parts.append("Found in Sandy, but no info for: {0}".format(line[10]))
                    #             # line[18]=c[2]
                    #             # line[19]=c[3]
                    #             # line[16]=c[5]
                    #             break

        if not found:
            found_part = False
            # print "checking suzhou for part %s" % line[1]
            for s in suzhou:
                # if (line[10] in c[1] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[1] and line [1] != '' and len(line[1]) > 4):
                if better_csv.search([line[1],line[10]], [s[0],s[6]]) or better_csv.search([s[0],s[6]],[line[1],line[10]]):
                    found_part = True
                    found = True
                    found_parts = found_parts + 1
                    updated_parts.append("Found in Suzhou, but no info for:  {0}".format(line[10]))
                    suzhou_count = suzhou_count + 1
                    master_copy_lines.append(line)
                    # line[18]=c[2]
                    # line[19]=c[3]
                    # line[16]=c[5]
                    break

        if not found:
            found_part = False
            # print "checking leap tracker for part %s" % line[1]
            for l in leap_tracker:
                if better_csv.search([line[1],line[10]], [l[1],l[3]]) or better_csv.search([l[1],l[3]], [line[1],line[10]]):
                    # if (line[1] in c[1]) or  ((line[10] in c[1]) and len(line[10])>4) or (line[1] in c[3]) or ((line[10] in c[3]) and len(line[10])>4):
                    # if (line[10] in c[1] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[1] and line [1] != '' and len(line[1]) > 4) or (line[10] in c[3] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[3] and line [1] != '' and len(line[1]) > 4):
                    found_part = True
                    found = True
                    found_parts = found_parts + 1
                    updated_parts.append("Found in leap tracker, but no info for:  {0}".format(line[10]))
                    leap_tracker_count = leap_tracker_count + 1
                    line[19] = l[9]
                    master_copy_lines.append(line)
                    # line[18]=c[2]
                    # line[19]=c[3]
                    # line[16]=c[5]
                    break

        if not found:
            found_part = False
            # print "checking leap tracker welded ring update for part %s" % line[1]
            for l in leap_tracker_welded_ring_update:
                if better_csv.search([line[1],line[10]], [l[1],l[2]]) or better_csv.search([l[1],l[2]], [line[1],line[10]]):
                    # if (line[1] in c[1]) or ((line[10] in c[1]) and len(line[10])>4) or (line[1] in c[2]) or  (line[10] in c[2] and len(line[10])>4):
                    # if (line[10] in c[1] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[1] and line [1] != '' and len(line[1]) > 4) or (line[10] in c[2] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[2] and line [1] != '' and len(line[1]) > 4):
                    found_part = True
                    found = True
                    found_parts = found_parts + 1
                    updated_parts.append(
                        "Found in leap tracker welded ring update, but no info for:  {0}".format(line[10]))
                    leap_tracker_welded_ring_update_count = leap_tracker_welded_ring_update_count + 1
                    line[16] = l[17]
                    line[19] = l[8]
                    master_copy_lines.append(line)
                    # line[18]=c[2]
                    # line[19]=c[3]
                    # line[16]=c[5]
                    break

        if not found:
            found_part = False
            # print "checking leap tracker welded ring update for part %s" % line[1]
            for l in suzhou_min:
                if better_csv.search([line[1],line[10]], [l[0],l[6]]) or better_csv.search([l[0],l[6]],[line[1],line[10]]):
                    # if (line[10] in c[0] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[0] and line [1] != '' and len(line[1]) > 4):
                    found_part = True
                    found = True
                    found_parts = found_parts + 1
                    updated_parts.append(
                        "Found in GE Suzhou master from minneapolis, but no info for:  {0}".format(line[10]))
                    suzhou_min_count = suzhou_min_count + 1
                    master_copy_lines.append(line)
                    # line[18]=c[2]
                    # line[19]=c[3]
                    # line[16]=c[5]
                    break

        if not found:
            found_part = False
            # print "checking leap tracker welded ring update for part %s" % line[1]
            for l in tei:
                if better_csv.search([line[1],line[10]], [l[1],l[8]]) or better_csv.search([l[1],l[8]],[line[1],line[10]] ):
                    # if (line[10] in c[1] and line [10] != '' and len(line[10]) > 4) or (line[1] in c[1] and line [1] != '' and len(line[1]) > 4):
                    found_part = True
                    found = True
                    found_parts = found_parts + 1
                    updated_parts.append("Found in TEI from minneapolis, but no info for:  {0}".format(line[10]))
                    tei_count = tei_count + 1
                    master_copy_lines.append(line)
                    # line[18]=c[2]
                    # line[19]=c[3]
                    # line[16]=c[5]
                    break

    if not found:
        unfound_parts = unfound_parts + 1
        master_copy_lines.append(line)
    # master_copy_lines.append(line)
    continue
# for part in updated_parts:
#     print(part)

hs = open("this_is_it_2.csv","w")
for line in master_copy_lines:
    hs.write(",".join(line)+"\r")

hs.close()

    # print ",".join(line)


print "Firth Rixson count: %s" % firth_rixon_count
print "Welded Ring count: %s" %welded_ring_count
print "Leap tracker count: %s" %leap_tracker_count
print "Leap Tracker Welded ring count: %s " % leap_tracker_welded_ring_update_count
print "CFW count: %s" % cfw_count
print "Mountain Top count: %s" % m_found
print "Suzhou count: %s" % suzhou_count
print "Suzhou Minneapolis count: %s" % suzhou_min_count
print "TEI count: %s" % tei_count
print "Total parts not found: %s/%s" % (unfound_parts, total_parts)
print "Total parts found: %s/%s" % (found_parts, total_parts)


# updated= get_lists(get_lines(open("this_is_it.csv").read()))
#here's an example of bubble sort, kind of
# changed_row_count = 0
# updates=[]
# for u in updated:
#     # print ("checking updates")
#     for l in master_copy:
#         if u[0] == l[0]:
#             if u[15] != l[15] or u[18] != l[18] or u[16] != l[16] or u[19] != l[19]:
#                 updates.append("Changes detected in row %s. Values changed- Billet Diameter: %s=>%s, Alloy: %s=>%s, Weight: %s=>%s, Spec: %s=>%s" % (u[0], l[15], u[15], l[18],u[18], l[16], u[16], l[19], u[19]))
#                 changed_row_count = changed_row_count+1
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
# for p in updates:
#     print  p