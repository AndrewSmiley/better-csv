__author__ = 'Andrew'
from parse_functions import BetterCSV
better_csv = BetterCSV()
updated= better_csv.get_lists(better_csv.get_lines(open("this_is_it_2.csv").read()))
master_copy = better_csv.get_lists(better_csv.get_lines(open("master_copy_updated_data.csv").read()))
#here's an example of bubble sort, kind of
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
changed_row_count = 0
updates=[]
for u in updated:
    # print ("checking updates")
    for l in master_copy:
        if u[0] == l[0]:
            if u[15] != l[15] or u[18] != l[18] or u[16] != l[16] or u[19] != l[19] or u[14] != l[14] or u[17] != l[17] or u[4] != l[4] or u[11] != l[11] or u[31] != l[31] or u[7] != l[7]:
                updates.append("Changes detected in row %s. Values changed- Billet Diameter: %s=>%s, Alloy: %s=>%s,"
                               " Weight: %s=>%s, Weight Type: %s=>%s, Spec: %s=>%s, Yield: %s=>%s,"
                               " QPE: %s=>%s, R/M Type: %s=>%s, Alloy Family: %s=>%s, Engine Program: %s=>%s" % (u[0], l[15], u[15], l[18],u[18], l[16], u[16],l[17],u[17],
                                                                                          l[19], u[19],l[14],u[14],l[4],u[4],l[11],u[11],l[31],u[31],l[7],u[7]))
                changed_row_count = changed_row_count+1
            #billet diameter
            # line[15]= f[14]
            #alloy
            # line[18] = f[12]
            #weight
            # line[16] = f[15]
            #spec
            # line[19]=/ f[13]



    # print "".join(line)

for p in updates:
    print  p
print changed_row_count