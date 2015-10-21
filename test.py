__author__ = 'Andrew'
from parse_functions import BetterCSV
from excel_functions import iterate
# res = BetterCSV().get_lists(["1974,\"6019T88 G03\",,,,,\"Welded Ring\",CF34,,,9431-01,,,,,,14.77,,\"AMS 5754\",\"AMS 5754\",,,,,,,,,,,,"])
better_csv=BetterCSV()
master_copy = better_csv.get_lists(better_csv.get_lines(open("data/leah.csv").read()))
leah = better_csv.get_lists(better_csv.get_lines(open("master_tesdoet.csv").read()))
master_copy= iterate(master_copy, leah, [3,7],[1,10],{18:3,19:4,20:15,21:16,22:17}, "Master")
# print "hello "
# for l in master_copy:
#     print l
hs = open("this_is_it_101.csv","w")
for mline in master_copy:
    hs.write(",".join(mline)+"\r")

hs.close()