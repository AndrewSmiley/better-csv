__author__ = 'Andrew'
from main import *

updated= get_lists(get_lines(open("this_is_it.csv").read()))
master_copy = get_lists(get_lines(open("master_sheet.csv").read()))
#here's an example of bubble sort, kind of
changed_row_count = 0
updates=[]
for u in updated:
    # print ("checking updates")
    for l in master_copy:
        if u[0] == l[0]:
            if u[15] != l[15] or u[18] != l[18] or u[16] != l[16] or u[19] != l[19]:
                updates.append("Changes detected in row %s. Values changed- Billet Diameter: %s=>%s, Alloy: %s=>%s, Weight: %s=>%s, Spec: %s=>%s" % (u[0], l[15], u[15], l[18],u[18], l[16], u[16], l[19], u[19]))
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