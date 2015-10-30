__author__ = 'pridemai'
import string

"""
function to search for a term in an array
"""
def excel_binary_search(search_term, array,search_key):
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        if  str(array[middle_pos][search_key].value) < search_term :
            if BetterCSV().search([array[middle_pos][search_key].value],[search_term]):
                print "match found: %s = %s" % (array[middle_pos][search_key].value, search_term)
                return {'result':True, 'index': middle_pos}
            lower_bound = middle_pos + 1
        elif str(array[middle_pos][search_key].value) > search_term:
            if BetterCSV().search([search_term], [array[middle_pos][search_key].value]):
                print "match found: %s = %s" % (array[middle_pos][search_key].value, search_term)
                return {'result':True, 'index': middle_pos}
            upper_bound = middle_pos - 1
        else:
            print "match found: %s = %s" % (array[middle_pos][search_key].value, search_term)
            return {'result':True, 'index': middle_pos}

    return {'result':False,'index':middle_pos}
    pass
"""
Function to read a file and return a string of the contents
"""
def binary_search(master_row, source_data,master_search_index, source_search_index):
    lower_bound = 0
    upper_bound = len(source_data) - 1
    found = False
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2
        # if BetterCSV().search([source_data[middle_pos][source_search_index]],master_row[master_search_index]):
        #         # print "Match found %s in %s" % (master_row[master_search_index], source_data[middle_pos][source_search_index])
        #         found = True
        #         break
        if source_data[middle_pos][source_search_index] < master_row[master_search_index]:
            if BetterCSV().search([source_data[middle_pos][source_search_index]],[master_row[master_search_index]]):
                # print "Match found %s in %s" % (master_row[master_search_index], source_data[middle_pos][source_search_index])
                return {"result": True, "index": middle_pos}
                break
            # print "working lower bound"
            lower_bound = middle_pos + 1

        elif source_data[middle_pos][source_search_index] > master_row[master_search_index] :
            if BetterCSV().search([master_row[master_search_index]],[source_data[middle_pos][source_search_index]]):
                # print "Match found %s in %s" % (master_row[master_search_index], source_data[middle_pos][source_search_index])
                return {"result": True, "index": middle_pos}
                break
            # print "working upper bound"
            upper_bound = middle_pos - 1
        else:
            # print " BINARY SEARCH Match found %s in %s" % (master_row[master_search_index], source_data[middle_pos][source_search_index])
            if len(source_data[middle_pos][source_search_index]) > 5:

                return {"result": True, "index": middle_pos}
            else:
                break


    return {"result": False, "index": -1}
"""
function to search for a term in an array
"""
def basic_binary_search(search_term, array):
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        if  array[middle_pos] < search_term :
            lower_bound = middle_pos + 1
        elif array[middle_pos] > search_term:
            upper_bound = middle_pos - 1
        else:
            return True

    return False

"""
function to search for a term in an array
"""
def basic_binary_search_with_added_shit(search_term, array):
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        if  array[middle_pos] < search_term :
            if BetterCSV().search([array[middle_pos]],[search_term]):
                return {'result':True, 'index': middle_pos}
            lower_bound = middle_pos + 1
        elif array[middle_pos] > search_term:
            if BetterCSV().search([search_term], [array[middle_pos]]):
                return {'result':True, 'index': middle_pos}
            upper_bound = middle_pos - 1
        else:
            return {'result':True, 'index': middle_pos}

    return {'result':False,'index':middle_pos}
    pass
class BetterCSV:


    def make_parseable(self,string,characters):
        for search,replace_with in characters.iteritems():
                if search in string:
                    string = string.replace(search, replace_with)

        return string


    def trim_whitespace(self, string):
        return string.replace(" ","")

    def read_file(self,filename, arguments=""):
        f  = open(filename, arguments)
        values = f.read()
        f.close()
        return values


    def search(self,search_terms, search_values,threshold=0):
        valid_search_terms=[]
        valid_search_values=[]
        for s in search_terms:
            if s == None:
                continue
            try:
               s = str(s)
            except:
               break
            s = s.replace("("," ")
            s = s.replace(")"," ")
            s = s.replace(")"," ")
            s = s.replace(","," ")
            s = s.replace(":"," ")
            s = s.replace("/"," ")
            # s = self.make_parseable(s, {"/": " ", "(":" ",")":" ",",":" "})
            if len(s) > 4 and any(char.isdigit() for char in s):
                if "/" in s:
                    new = s.split("/")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) > 4:
                            valid_search_terms.append(sn)
                elif "," in s:
                    new = s.split(",")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_terms.append(sn)

                elif ", " in s:
                    new = s.split(", ")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_terms.append(sn)
                elif " " in s:
                    new = s.split(" ")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_terms.append(sn)
                else:
                    valid_search_terms.append(s.replace(" ",""))
        for s in search_values:
            if s == None:
                continue
            try:
                s = str(s)
            except:
                break
            # s = self.make_parseable(s, {"/": " ", "(":" ",")":" "})
            s = s.replace("("," ")
            s = s.replace(")"," ")
            s = s.replace(")"," ")
            s = s.replace(","," ")
            s = s.replace(":"," ")
            s = s.replace("/"," ")
            if len(s) > 4 and any(char.isdigit() for char in s):
                if "/" in s:
                    new = s.split("/")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_values.append(sn)
                elif "," in s:
                    new = s.split(",")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_values.append(sn)
                elif ", " in s:
                    new = s.split(", ")
                    for sn in new:
                        sn.replace(" ","")
                        if len(sn) >4:
                            valid_search_values.append(sn)
                elif " " in s:
                    new = s.split(" ")
                    for sn in new:
                        if len(sn) >4:
                            valid_search_values.append(sn)



                else:
                    valid_search_values.append(s.replace(" ",""))

        if len(valid_search_terms) > 0 and len(valid_search_values) > 0:
            #really want to get away from using
            if threshold != 0:
                from_end=0
                while from_end <= threshold:
                    for search_term in valid_search_terms:
                        if from_end <= 0:
                            from_end = from_end+1
                            for search_value in valid_search_values:
                                if search_term in search_value:
                                    print "Match Found: %s in %s" % (search_term,search_value)
                                    return True
                        else:
                            from_end = from_end+1
                            for search_value in valid_search_values:
                                if search_term[:from_end*-1] in search_value:
                                    print "Match Found: %s in %s" % (search_term,search_value)
                                    return True
            else:
                for search_term in valid_search_terms:
                    # try:
                    #     valid_search_values.index(search_term)
                    #     return True
                    # except:
                    #     return False
                    for search_value in valid_search_values:
                        if search_term in search_value:
                            print "Match Found: %s in %s" % (search_term,search_value)
                            return True
            # print "No valid search terms :("
            # for search_value in valid_search_values:
            #     for search_term in valid_search_terms:
            #         if search_term in search_value:
            #             return True


        return False

    def get_lines(self,text_string):
        return text_string.split("\r") if len(text_string.split("\r")) > 1 else text_string.split("\n") if len(text_string.split("\n")) > 1 else text_string.split("\r\n")

    # string = "\" $(3,562.86)\",\"$174,565.86\",,,Liming new source,\"sympathetic, never let it show the way i feel i do \",data,,,\"fuck\",balls"
    def get_lists(self,lines):
        arrays = []
        for string in lines:
            # print string
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
                            end_pos = last_position+string[last_position+1:].find("\"")+2
                            multiple_qoutes = False
                            if string[end_pos] != ",":
                                end_pos = end_pos+1
                                while not multiple_qoutes:
                                    if string[end_pos] == ",":
                                        multiple_qoutes = True
                                        end_pos = end_pos +1
                                    else:
                                        end_pos = end_pos +1


                            tmp =string[last_position:end_pos]
                            line.append(tmp)
                            # line.append(string[last_position:last_position+string[last_position:].find("\"")+1])
                            #the +1 ensures we skip passed the next one
                            last_position = string.find(tmp)+1+len(tmp) if string.find(tmp)+1+len(tmp) > last_position else last_position +1
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
                                multiple_qoutes = False
                                try:
                                    if string[open_qoute_pos + close_qoute_pos + 2] == "\"" or string[open_qoute_pos + close_qoute_pos + 2] != ",":
                                        while not multiple_qoutes:
                                            if string[open_qoute_pos + close_qoute_pos + 2 +1] == ",":
                                                multiple_qoutes = True
                                                close_qoute_pos = close_qoute_pos +1
                                            else:
                                                close_qoute_pos = close_qoute_pos +1
                                except:
                                    pass
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
                # print string
                #print ("nothing to do")
                arrays.append(string.split(","))
                should_get_last = False
                continue
            if should_get_last:
                # print string
                line.append(string[last_position:len(string)])
            arrays.append(line)



        return  arrays

    """
    Function to get a list of dictionaries with the column names from the index_row argument
    """
    def get_dicts(self,lines,headers_row=0):
        rows = self.get_lists(lines)
        column_headers= rows[headers_row]
        dicts = []
        #in this, we're making the assumtion that the csv is consistent in column length
        for row in rows:
            dict_container={}
            i = 0
            while i < len(column_headers):
                try:
                    dict_container[column_headers[i]]=row[i]
                except IndexError as ie:
                    print "Bad index in row %s column %s: %s" % (row,i,ie)
                    return None
                i = i+1

            dicts.append(dict_container)

        #assuming that all worked, return dicts
        return dicts


    """
    Function to find the first index of a partular row (i.e. a list inside of our collection of list)
    searchterm: The string searchterm to look for
    rows: The list of lists to search in
    """
    def find_row(self, searchterm, rows):
        for row in rows:
            try:
                if row.index(searchterm):
                    return rows.index(row)
            except Exception:
                continue
        #todo-fill this one in
        raise Exception("Could not Find Row")

    """
    Function to the index of all rows that contain the search term
    searchterm: The string searchterm to look for
    rows: The list of lists to search in
    """
    def find_rows(self, searchterm, rows):
        indexes = []
        #todo-fill this one in
        return indexes
    """
    Function to append list_a into list_b
    """
    def append_list(self, list_a, list_b):

        #todo-fill me in
        return list_a

    def file_contents_as_string(self, filename):
        file=open(filename, "r")
        file_contents=file.read()
        file.close()
        return file_contents






