__author__ = 'pridemai'
import csv,sys
from parse_functions import get_lists,search


search(["2463M43P05",""], ["2463M43P05-AS02","2463M43P05JEKQ"])

# string = "1,2301M66P02,\"SEAL, ROT 4R AFT (GENX)\",,,Yes,80739-PARADIGM PRECISION - TEMPE OPERATIONS   ,Genx,,102,2301M66P02,Seamless,Firth_Rixson,Suzhou,1=1,6,70,Billet ,I-718,B50TF15,,,\" $1,746.36 \",\" $1,711.43 \",Yes, $(34.93),\" $(3,562.86)\",\"$174,565.86\",Liming new source,,wubbalubbadubdub,,"new_string=""
# print get_lists(["\" $(3,562.86)\",\"$174,565.86\",Liming new source,,12.32,\"Can't you see that I love my cock?\",83.43,wubbalubbadubdub,,"])
# string = '$(3562.86),\"$174,565.86\",\"as\",,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls,,\"asf\",,data'
# string ='526,2302M40G01,GENX BRG HSG,,,Yes,58714-FAST,Genx,,91,4013703-931P02,Forging_Ring_Seamless_or_Welded_W,Firth_Rixson,Viking,1=1,14,"1,214.0",Yielded,15.5PH,AMS 5659,,," $15,357.83 "," $15,050.67 ",Yes, $(307.16), $(307.16)," $(20,963.67)",,,N/A'
# def get_lists(lines):
#     arrays = []
#     for string in lines:
#         should_get_last = True
#         last_position = 0
#         line = []
#         if "\"" in string:
#             last_position = 0
#             print ("%s/%s" % (last_position,len(string)))
#             while string[last_position:len(string)].find(",") != -1:
#                 comma_pos = string[last_position:len(string)].find(",")
#                 # check to see if we found a qoute
#                 if "\"" in string[last_position:comma_pos+last_position]:
#                     #check to see if there's a comma within the qouted string
#                     first_qoute = string[last_position:].find("\"")
#                     second_qoute = string[last_position+first_qoute+1:].find("\"")
#                     if "," in string[first_qoute+last_position:second_qoute+last_position+1]:
#                     # if (string[last_position+comma_pos:].find(",") < string[last_position+comma_pos:].find("\"")) and string[last_position+comma_pos:].find(",") != -1:
#                         #yes, there's a comma in it
#                         #so basically we want
#                         #" $(3,562.86)",
#                         first_comma = string[last_position:].find(",")+1
#                         second_comma = string[last_position+first_comma:].find(",")
#                         line.append(string[last_position: last_position+first_comma+second_comma])
#                         last_position = last_position+first_comma+second_comma+1
#                     else:
#                         tmp =string[last_position:last_position+string[last_position+1:].find("\"")+2]
#                         line.append(tmp)
#                         # line.append(string[last_position:last_position+string[last_position:].find("\"")+1])
#                         #the +1 ensures we skip passed the next one
#                         last_position = string.find(tmp)+1+len(tmp)
#                         # last_position = last_position+string[last_position+1:].find("\"")+1
#
#
#                     #get the
#                     # last_comma_pos = last_position+(comma_pos+1)
#                     # comma_pos = string[last_comma_pos:].find(",")
#                     # if "\"" in string[last_comma_pos:comma_pos+last_comma_pos]:
#                     #     line.append(string[last_position:(comma_pos+last_comma_pos)])
#                     #     last_position = (comma_pos+last_comma_pos)+1
#                     # else:
#                     #     line.append(string[last_position:last_comma_pos-1])
#                     #     last_position = (comma_pos+last_comma_pos)+1
#                 else:
#                     if last_position == 0:
#                         print(string[last_position:comma_pos])
#                     if last_position < len(string) -1:
#                         # has_qoutes=[string[last_position + comma_pos + 1] == '\"',string[last_position] == "\"" ]
#                         if string[(last_position + comma_pos + 1) if (last_position + comma_pos + 1) < len(string) else len(string)-1] == '\"' or string[last_position] == "\"" :
#                             #begin processing for qoute
#                             line.append(string[last_position:comma_pos + last_position:])
#                             open_qoute_pos = last_position + comma_pos + 1
#                             close_qoute_pos = string[open_qoute_pos + 1:len(string)].find('\"')
#                             line.append(string[open_qoute_pos:(close_qoute_pos + 2) + open_qoute_pos])
#                             last_position = open_qoute_pos + close_qoute_pos + 2
#                             if last_position == len(string):
#                                 should_get_last = False
#                                 break
#                             if string[last_position] != ",":
#                                 print("whoa something is fucky on line %s" % line)
#                             else:
#                                 #just so we start at at the character after the comma
#                                 last_position = last_position + 1
#                                 # print string[open_qoute_pos:close_qoute_pos+open_qoute_pos+2]
#                         else:
#                             # print "found comma at position %s" % str(last_position+comma_pos+1)
#
#                             line.append(string[last_position:comma_pos + last_position])
#                             # string = string[string.find(",")+1:]
#                             #because we want to start the seardch after the comma
#                             last_position = last_position + (comma_pos + 1)
#                     else:
#                         if string[last_position-1] == ",":
#                             while string[last_position-1:len(string)].find(",") != -1:
#                                 line.append(string[last_position:string[last_position+1:len(string)].find(",")])
#                                 last_position = last_position+1
#                                 should_get_last = False
#                         else:
#                             while string[last_position-1:len(string)].find(",") != -1:
#                                 line.append(string[last_position:string[last_position+1:len(string)].find(",")])
#                                 last_position = last_position+1
#                                 should_get_last = False
#
#                         # line.append(string[last_position:len(string)])
#                 # arrays.append(line)
#         else:
#             # print ("nothing to do")
#             arrays.append(string.split(","))
#             should_get_last =False
#         if should_get_last:
#             line.append(string[last_position:len(string)])
#         arrays.append(line)
#     return  arrays
#
# arrays = get_lists([string])
# for l in arrays:
#     print (l)



"""
Back this shit up
"""

# string = "61,2466M25P01,2466M25P01.000W,\"RING, RETAINER\",0.17,15.397,15.435,I718,B50TF15 CL-E,LEAP A/C,93689-VSE-15-02411,5,,,,,Space-Craft ,12.52,Welded Ring Products,$117,,y,y,y,10/26/15,1=6 ring,12/4/15,5 weeks,LTA FPN 2609M10G03"
# new_string=""
# line=[]
# last_position=0
# while string[last_position:len(string)].find(",") != -1:
#     comma_pos = string[last_position:len(string)].find(",")
#     if string[comma_pos+1] == '\"':
#         print "found comma at position %s" % str(comma_pos+1)
#     line.append(string[last_position:comma_pos+last_position])
#     # string = string[string.find(",")+1:]
#     #because we want to start the search after the comma
#     last_position = last_position+(comma_pos+1)
#
# line.append(string[last_position:len(string)])
# for l in line:
#     print l


