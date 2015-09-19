__author__ = 'pridemai'




def search(search_terms, search_values):
    valid_search_terms=[]
    valid_search_values=[]
    for s in search_terms:
        if len(s) > 4:
            valid_search_terms.append(s)
    for s in search_values:
        if len(s) > 4:
            valid_search_values.append(s)

    if len(valid_search_terms) > 0 and len(valid_search_values) > 0:
        #really want to get away from using
        for search_term in valid_search_terms:
            for search_value in search_values:
                if search_term in search_value:
                    return True


    return False


def get_lines(str):
    return str.split("\r")


# string = "\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls"
def get_lists(lines):
    arrays = []
    for string in lines:
        should_get_last = True
        last_position = 0
        line = []
        if "\"" in string:
            last_position = 0
            #print ("%s/%s" % (last_position,len(string)))
            while string[last_position:len(string)].find(",") != -1:
                comma_pos = string[last_position:len(string)].find(",")
                # check to see if we found a qoute
                if "\"" in string[last_position:comma_pos+last_position]:
                    #check to see if there's a comma within the qouted string
                    first_qoute = string[last_position:].find("\"")
                    second_qoute = string[last_position+first_qoute+1:].find("\"")
                    if "," in string[first_qoute+last_position:second_qoute+last_position+1]:
                    # if (string[last_position+comma_pos:].find(",") < string[last_position+comma_pos:].find("\"")) and string[last_position+comma_pos:].find(",") != -1:
                        #yes, there's a comma in it
                        #so basically we want
                        #" $(3,562.86)",
                        first_comma = string[last_position:].find(",")+1
                        second_comma = string[last_position+first_comma:].find(",")
                        line.append(string[last_position: last_position+first_comma+second_comma])
                        last_position = last_position+first_comma+second_comma+1
                    else:
                        tmp =string[last_position:last_position+string[last_position+1:].find("\"")+2]
                        line.append(tmp)
                        # line.append(string[last_position:last_position+string[last_position:].find("\"")+1])
                        #the +1 ensures we skip passed the next one
                        last_position = string.find(tmp)+1+len(tmp)
                        # last_position = last_position+string[last_position+1:].find("\"")+1


                    #get the
                    # last_comma_pos = last_position+(comma_pos+1)
                    # comma_pos = string[last_comma_pos:].find(",")
                    # if "\"" in string[last_comma_pos:comma_pos+last_comma_pos]:
                    #     line.append(string[last_position:(comma_pos+last_comma_pos)])
                    #     last_position = (comma_pos+last_comma_pos)+1
                    # else:
                    #     line.append(string[last_position:last_comma_pos-1])
                    #     last_position = (comma_pos+last_comma_pos)+1
                else:
                    # if last_position == 0:
                        #print(string[last_position:comma_pos])
                    if last_position < len(string) -1:
                        # has_qoutes=[string[last_position + comma_pos + 1] == '\"',string[last_position] == "\"" ]
                        if string[(last_position + comma_pos + 1) if (last_position + comma_pos + 1) < len(string) else len(string)-1] == '\"' or string[last_position] == "\"" :
                            #begin processing for qoute
                            line.append(string[last_position:comma_pos + last_position:])
                            open_qoute_pos = last_position + comma_pos + 1
                            close_qoute_pos = string[open_qoute_pos + 1:len(string)].find('\"')
                            line.append(string[open_qoute_pos:(close_qoute_pos + 2) + open_qoute_pos])
                            last_position = open_qoute_pos + close_qoute_pos + 2
                            if last_position == len(string):
                                should_get_last = False
                                break
                            if string[last_position] != ",":
                                print("whoa something is fucky on line %s" % line)
                            else:
                                #just so we start at at the character after the comma
                                last_position = last_position + 1
                                # #print string[open_qoute_pos:close_qoute_pos+open_qoute_pos+2]
                        else:
                            # #print "found comma at position %s" % str(last_position+comma_pos+1)

                            line.append(string[last_position:comma_pos + last_position])
                            # string = string[string.find(",")+1:]
                            #because we want to start the seardch after the comma
                            last_position = last_position + (comma_pos + 1)
                    else:
                        if string[last_position-1] == ",":
                            while string[last_position-1:len(string)].find(",") != -1:
                                line.append(string[last_position:string[last_position+1:len(string)].find(",")])
                                last_position = last_position+1
                                should_get_last = False
                        else:
                            while string[last_position-1:len(string)].find(",") != -1:
                                line.append(string[last_position:string[last_position+1:len(string)].find(",")])
                                last_position = last_position+1
                                should_get_last = False

                        # line.append(string[last_position:len(string)])
                # arrays.append(line)
        else:
            #print ("nothing to do")
            arrays.append(string.split(","))
            should_get_last = False
            continue
        if should_get_last:
            line.append(string[last_position:len(string)])
        arrays.append(line)



    return  arrays

# def get_lists(lines):
#     arrays = []
#     for string in lines:
#         should_get_last = True
#         last_position = 0
#         line = []
#         if "\"" in string:
#             last_position = 0
#             #print ("%s/%s" % (last_position,len(string)))
#             while string[last_position:len(string)].find(",") != -1:
#                 comma_pos = string[last_position:len(string)].find(",")
#                 # check to see if we found a qoute
#                 if "\"" in string[last_position:comma_pos+last_position]:
#
#                     last_comma_pos = last_position+(comma_pos+1)
#                     comma_pos = string[last_comma_pos:].find(",")
#                     if "\"" in string[last_comma_pos:comma_pos+last_comma_pos]:
#                         line.append(string[last_position:(comma_pos+last_comma_pos)])
#                         last_position = (comma_pos+last_comma_pos)+1
#                     else:
#                         line.append(string[last_position:last_comma_pos-1])
#                         last_position = (comma_pos+last_comma_pos)+1
#                 else:
#                     if last_position == 0:
#                         #print(string[last_position:comma_pos])
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
#                                 #print("whoa something is fucky on line %s" % line)
#                             else:
#                                 #just so we start at at the character after the comma
#                                 last_position = last_position + 1
#                                 # #print string[open_qoute_pos:close_qoute_pos+open_qoute_pos+2]
#                         else:
#                             # #print "found comma at position %s" % str(last_position+comma_pos+1)
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
#             #print ("nothing to do")
#             # arrays.append(string.split(","))
#         if should_get_last:
#             line.append(string[last_position:len(string)])
#         arrays.append(line)
#     return  arrays


# arrays = get_lists([string])
# for l in arrays:
#     #print (l)