__author__ = 'pridemai'
import requests


f  ={'bbox','-84.288180,,-84.288180,',}
# r = requests.get("http://api.openstreetmap.org/api/0.6/map?[bbox=-84.300092,39.240952,-84.299577,39.241554]")
r = requests.get("http://www.overpass-api.de/api/xapi?*[maxspeed=*][bbox=-84.265587,39.236655,-84.264814,39.236998]")
print r.content
#
# 39.236998, -84.265587
# 39.236655, -84.264814