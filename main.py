__author__ = 'pridemai'
from parts import Part


def get_lines(str):
    return str.split("\r")


def get_lists(lines):
    arrays = []
    for line in lines:
        line.replace("\"", "")
        line.replace("\'", "")
        arrays.append(line.split(","))

    return arrays


#here's the shit
#fuck
master_copy = get_lists(get_lines(open("master_sheet.csv").read()))
firth_rixon = get_lists(get_lines(open("firth_rixon.csv").read()))
welded_ring = get_lists(get_lines(open("welded_ring.csv").read()))
mountain_top= get_lists(get_lines(open("mountain_top.csv").read()))
cfw = get_lists(get_lines(open("cfw.csv").read()))
sandy= get_lists(get_lines(open("sandy.csv").read()))
suzhou= get_lists(get_lines(open("suzhou.csv").read()))
leap_tracker=get_lists(get_lines(open("leap_tracker.csv").read()))
leap_tracker_welded_ring_update=get_lists(get_lines(open("leap_tracker_welded_ring_update.csv").read()))
master_copy_lines = []

# counter = 0
# for line in firth_rixon[0]:
#     print "[{0}] {1}".format(counter, line)
#     counter +=1
#
updated_parts=[]
for line in master_copy:
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
    if "Firth_Rixson" == line[12]:

        #so now we can search for the part number
        found = False
        if line[16] == '0' and line[15] =='0' and line[18] =='0':
            # print ("we found firth rixson with missing data")
            for f in firth_rixon:
                #        f[6]
                if line[1] in f[16]:
                    updated_parts.append("Firth Rixson: {0}".format(line[1]))
                    found = True
                    #billet diameter
                    line[15]= f[14]
                    #alloy
                    line[18] = f[12]
                    #weight
                    line[16] = f[15]
                    #spec
                    line[19]= f[13]
                    break
                else:
                    continue

           # if found:
                # print "we found info for part number {0}".format(line[1])
            master_copy_lines.append(line)
            continue
        else:
            master_copy_lines.append(line)
            continue

    elif "Welded_Ring" == line[12]:
        if line[16] == '0' and line[15] =='0' and line[18] =='0':
            # print("We found welded_ring with missing data")
            found=False
            for w in welded_ring:
                if line[1] in w[1]:
                    updated_parts.append("Welded ring: {0}".format(line[1]))
                    found=True
                    #alloy
                    line[18]=w[8]
                    #weight
                    line[16]=w[6]
                    #spec
                    line[19]=w[9]
            # if found:
            #     print("We found data for part {0}".format(line[1]))

            master_copy_lines.append(line)
            continue

    else:
        #this will help us search for parts in the other files, regardless of supplier
        found = False
        if line[16] == '0' and line[15] =='0' and line[18] =='0':
            if not found:
                print
                found_part = False
                #checking the mountain top CSV
                # print "checking mountain top for part %s" % line[1]
                for m in mountain_top:
                    if line[1] in m[1]:
                        updated_parts.append("Mountain Top: {0}".format(line[1]))
                        found_part=True
                        found=True
                        #only alloy and weight are available from this one
                        line[18]=m[3]
                        line[16]=m[5]
                # if found_part

            #checking CFW now
            if not found:
                found_part=False
                # print "checking CFW for part %s" % line[1]
                for c in cfw:
                    if line[1] in c[1]:
                        found_part=True
                        found=True
                        updated_parts.append("CFW {0}".format(line[1]))
                        line[18]=c[2]
                        line[19]=c[3]
                        line[16]=c[5]

            if not found:
                found_part=False
                # print "checking SANDY for part %s" % line[1]
                for c in sandy:
                    if line[1] in c[1]:
                        found_part=True
                        found=True
                        updated_parts.append("Found in Sandy, but no info for: {0}".format(line[1]))
                        # line[18]=c[2]
                        # line[19]=c[3]
                        # line[16]=c[5]

            if not found:
                found_part=False
                # print "checking suzhou for part %s" % line[1]
                for c in suzhou:
                    if line[1] in c[1]:
                        found_part=True
                        found=True
                        updated_parts.append("Found in Suzhou, but no info for:  {0}".format(line[1]))
                        # line[18]=c[2]
                        # line[19]=c[3]
                        # line[16]=c[5]

            if not found:
                found_part=False
                # print "checking leap tracker for part %s" % line[1]
                for c in leap_tracker:
                    if line[1] in c[1]:
                        found_part=True
                        found=True
                        updated_parts.append("Found in leap tracker, but no info for:  {0}".format(line[1]))
                        # line[18]=c[2]
                        # line[19]=c[3]
                        # line[16]=c[5]
            if not found:
                found_part=False
                # print "checking leap tracker welded ring update for part %s" % line[1]
                for c in leap_tracker_welded_ring_update:
                    if line[1] in c[1]:
                        found_part=True
                        found=True
                        updated_parts.append("Found in leap tracker welded ring update, but no info for:  {0}".format(line[1]))
                        # line[18]=c[2]
                        # line[19]=c[3]
                        # line[16]=c[5]



        master_copy_lines.append(line)
        continue
print("Here's the updated parts")

for part in updated_parts:
    print(part)

hs = open("this_is_it.csv","a")
for line in master_copy_lines:
    hs.write(",".join(line)+"\r")

hs.close()

    # print ",".join(line)







    # print "".join(line)

