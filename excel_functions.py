__author__ = 'pridemai'
import sys
sys.path.insert(0, './better-csv')
from parse_functions  import BetterCSV

def update_row(master_row, data_row, master_row_columns, data_row_columns):
    iterator = 0
    if len(master_row_columns) != len(data_row_columns):
        print("Invalid row count on row: {0} \nCannot upate row data for this column".format(master_row))
        return master_row
    while iterator < len(master_row_columns):
        master_row[master_row_columns[iterator]] = data_row[data_row_columns[iterator]]
    return master_row


"""
 for line in master_copy:
    found = False
    for g in ge_lta2:
        #        f[6]
        # if (line[10] in f[16] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[16] and line [1] != '' and len(line[1]) > 2) or (line[10] in f[17] and line [10] != '' and len(line[10]) > 2) or (line[1] in f[17] and line [1] != '' and len(line[1]) > 2):
        if better_csv.search([line[1], line[10]], [g[1],g[2]]) or better_csv.search([g[1],g[2]], [line[1], line[10]]):
            # updated_parts.append("Found Firth Rixson {0}. Values inserted: Billet Diameter: {1} Alloy: {2} Weight: {3} Spec: {4} ID:{5}".format(line[10], f[14], f[12], f[15],f[13], line[0]))
            found = True
            # firth_rixon_count = firth_rixon_count +1
            line[2]=g[3]
            line[18]=g[7]
            line[16]=g[9]
            line[19]=g[8]
            line[7]=g[13]
            line[15]=g[5]


            ge_lta2_count=ge_lta2_count+1
            master_copy_lines.append(line)
            break
        else:
            continue
    if not found:
        master_copy_lines.append(line)
 :param master_copy:
 :param data_copy:
 :param master_search_columns:
 :param data_search_columns:
 :return:
"""
def iterate(master_copy,data_copy, master_search_columns, data_search_columns, master_data_columns, data_columns, filname="N/A"):
    better_csv = BetterCSV()
    new_master = []
    found_count = 0
    for line in master_copy:
        for column in master_search_columns:
            master_args.append(line[column])
        for d in data_copy:
            data_args =[]
            master_args=[]
            for column in data_search_columns:
                data_args.append(d[column])
            if better_csv.search(master_args, data_args):
                line = update_row(line, d, master_data_columns,data_columns)
                found_count = found_count + 1
        new_master.append(line)
    return new_master







