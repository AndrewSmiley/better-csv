__author__ = 'pridemai'
from parse_functions import BetterCSV
better_csv = BetterCSV()
# master_copy_new_data = better_csv.get_lists(better_csv.get_lines(open("master_copy_new_data.csv").read()))
master_copy_new_data = better_csv.get_lists(better_csv.get_lines(open("this_is_it_6.csv").read()))
# master_copy = better_csv.get_lists(better_csv.get_lines(open("master_copy_new.csv").read()))
fuck=better_csv.get_lines(open("fuck.txt").read())
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
print len(welded_ring2)
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
bad_count =0
for m in master_copy_new_data:

    if m[15]=="#N/A" and m[16]=="#N/A" and m[17]=="#N/A" and m[18]=="#N/A" :# and m[19]=="#N/A":
        for f in fuck:
            if " "+m[0]+" " in f:
                print f
                bad_count=bad_count+1
                break
    elif m[15]=="0" and m[16]=="0" and m[17]=="0" and m[18]=="0" :#and m[19]=="0":
        for f in fuck:
            if " "+m[0]+" " in f:
                print f
                bad_count=bad_count+1
                break


print bad_count
# master_copy_updated_lines=[]
# for line in master_copy:
#     for line_new_data in master_copy_new_data:
#         if line[0] == line_new_data[0]:
#             line[15]=line_new_data[15]
#             line[14]=line_new_data[14]
#             line[16]=line_new_data[16]
#             line[17]=line_new_data[17]
#             line[18]=line_new_data[18]
#             line[19]=line_new_data[19]
#             line[4]=line_new_data[4]
#             line[11]=line_new_data[11]
#             line[7]=line_new_data[7]
#             line[8]=line_new_data[8]
#             line[20]=line_new_data[20]
#     master_copy_updated_lines.append(line)
#
# hs = open("master_copy_updated_data.csv","w")
# for mline in master_copy_updated_lines:
#     hs.write(",".join(mline)+"\r")
#
# hs.close()
