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

master_copy_lines = []
# counter = 0
# for line in firth_rixon[0]:
#     print "[{0}] {1}".format(counter, line)
#     counter +=1
#
for line in master_copy:
    print "working a line"
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
    if "Firth_Rixson" != line[12]:
        master_copy_lines.append(line)
        continue
    else:
        print ("we found firth rixson")
        #so now we can search for the part number
        found = False
        for f in firth_rixon:
            #        f[6]
            if line[1] in f[16]:
                found = True
                line[15]= f[14]
                line[18] = f[12]
                line[16] = f[15]
                line[19]= f[13]
                break
            else:
                continue

        if found:
            print "we found info for part number {0}".format(line[1])
        master_copy_lines.append(line)
        continue
hs = open("this_is_it.csv","a")
for line in master_copy_lines:
    hs.write(",".join(line)+"\r")

hs.close()

    # print ",".join(line)







    # print "".join(line)

