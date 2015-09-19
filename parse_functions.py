__author__ = 'pridemai'

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
            print ("%s/%s" % (last_position,len(string)))
            while string[last_position:len(string)].find(",") != -1:
                comma_pos = string[last_position:len(string)].find(",")
                # check to see if we found a qoute
                if "\"" in string[last_position:comma_pos+last_position]:

                    last_comma_pos = last_position+(comma_pos+1)
                    comma_pos = string[last_comma_pos:].find(",")
                    if "\"" in string[last_comma_pos:comma_pos+last_comma_pos]:
                        line.append(string[last_position:(comma_pos+last_comma_pos)])
                        last_position = (comma_pos+last_comma_pos)+1
                    else:
                        line.append(string[last_position:last_comma_pos-1])
                        last_position = (comma_pos+last_comma_pos)+1
                else:
                    if last_position == 0:
                        print(string[last_position:comma_pos])
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
                                # print string[open_qoute_pos:close_qoute_pos+open_qoute_pos+2]
                        else:
                            # print "found comma at position %s" % str(last_position+comma_pos+1)

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
            print ("nothing to do")
            # arrays.append(string.split(","))
        if should_get_last:
            line.append(string[last_position:len(string)])
        arrays.append(line)
    return  arrays


# arrays = get_lists([string])
# for l in arrays:
#     print (l)