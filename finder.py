__author__ = 'pridemai'
from main import get_lines, get_lists

master_copy = get_lists(get_lines(open("master_sheet.csv").read()))
firth_rixon = get_lists(get_lines(open("firth_rixon.csv").read()))
welded_ring = get_lists(get_lines(open("welded_ring.csv").read()))
mountain_top= get_lists(get_lines(open("mountain_top.csv").read()))
cfw = get_lists(get_lines(open("cfw.csv").read()))
sandy= get_lists(get_lines(open("sandy.csv").read()))
suzhou= get_lists(get_lines(open("suzhou.csv").read()))
leap_tracker=get_lists(get_lines(open("leap_tracker.csv").read()))
leap_tracker_welded_ring_update=get_lists(get_lines(open("leap_tracker_welded_ring_update.csv").read()))
suzhou_master=get_lists(get_lines(open("suzou_master.csv").read()))
found_count =0

for l in master_copy:
    for f in firth_rixon
