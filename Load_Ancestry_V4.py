
import re

class DNA_Result(object):

    def __init__(self, index=99999, offset = 0, who="", centimorgans=0, segments=0, people = "", keystring = "", kit_duplicate_check = "", kit = "wally", kit_number = 99):


        self.index = index
        self.mega_index = index + offset
        self.who = who
        self.centimorgans = centimorgans
        self.segments = segments
        self.people = people
        self.keystring = keystring
        self.kit_duplicate_check = kit_duplicate_check
        self.kit = kit
        self.kit_number = kit_number



def get_data(word_list,index_offset , line_no, kit, kit_number):
    new_word_dict = {}
    new_word_dict["People"] = "zero"
    i = 0
    new_index = 9999999

    for column in word_list:
        if column == "Cousin" and index_offset == 0:
            new_word_dict["index"] = word_list[0]
            new_index = word_list[0]
            new_word_dict[column] = word_list[i-1]
            if i == 3:
                new_word_dict["who"] = word_list[1]
            if i == 4:
                new_word_dict["who"] = word_list[1] + word_list[2]
            if i == 5:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3]
            if i == 6:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4]
            if i == 7:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5]
            if i == 8:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6]
            if i == 9:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7]
            if i == 10:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8]
            if i == 11:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8] + word_list[9]
            if i == 12:
                new_word_dict["who"] = word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8] + word_list[9] + word_list[10]
        elif column == "Cousin" and index_offset != 0:
            new_index = line_no + index_offset
            new_word_dict["index"] = line_no + index_offset
            new_word_dict[column] = word_list[i-1]
            if i == 2:
                new_word_dict["who"] = word_list[0]
            if i == 3:
                new_word_dict["who"] = word_list[0] + word_list[1]
            if i == 4:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2]
            if i == 5:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3]
            if i == 6:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4]
            if i == 7:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5]
            if i == 8:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6]
            if i == 9:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7]
            if i == 10:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8]
            if i == 11:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8] + word_list[9]
            if i == 12:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8] + word_list[9] + word_list[10]

        if column == "cM":
            new_word_dict[column] = word_list[i-1]
            # new_word_dict["who"] = new_word_dict["who"] + word_list[i-1] + "cM"
        if column == "segments":
            new_word_dict[column] = word_list[i-1]
        if column == "People":
            #print(new_word_dict["index"])
            new_word_dict[column] = word_list[i-1]
            #new_word_dict["People"] = new_word_dict["People"].replace(',', '')
            new_word_dict["key_string"] = new_word_dict["who"] + "_" + word_list[i-1]
        if column == "Unlinked":
            #print(new_word_dict["index"])
            new_word_dict["Tree"] = "Unlinked Tree"
            #new_word_dict["who"] = new_word_dict["who"] + "_U"
            new_word_dict["key_string"] = new_word_dict["who"] + "_U"
        if column == "Trees":
            #print(new_word_dict["index"])
            new_word_dict["Tree"] = "No Trees"
            new_word_dict["key_string"] = new_word_dict["who"] + "_N"
        if column == "unavailable":
            new_word_dict["Tree"] = "unavailable"
            new_word_dict["key_string"] = new_word_dict["who"] + "_u"
        if column == "Common":
            new_word_dict[column] = "Wally"
        if column == "GEDMATCH":
            new_word_dict[column] = word_list[i+1]
        if column == "CHROMOSOMES":
            new_word_dict[column] = word_list[i+1]

        i += 1
    #print(int(new_index) , new_word_dict["who"])
    #kit_duplicate_check = new_word_dict["key_string"] + "_" + new_word_dict["cM"] + "_" + new_word_dict["segments"]
    kit_duplicate_check = new_word_dict["who"] + "_" + new_word_dict["cM"] + "_" + new_word_dict["segments"]  # allow for recent tree changes

    test_result = DNA_Result(int(line_no) , index_offset, new_word_dict["who"] , new_word_dict["cM"] , new_word_dict["segments"]
                             , new_word_dict["People"], new_word_dict["key_string"], kit_duplicate_check , kit, kit_number)

    return new_word_dict, test_result, kit_duplicate_check


def get_cousin_dict(kit,kit_number, index_offset,  kit_key_list,duplicate_key_list, kit_who_list,kit_who_dict, dna_list, dna_list_index, duplicate_dict, total_dna_list, cousin_key_list, Test_Result_Dict):

    dict_of_lists = {}
    old_index=9999999999
    line_no = 1
    for line in open(kit + '.txt'):
        line = line.rstrip()
        line = line.replace('\t',' ')
        line = line.replace(',', '')
        word_list = line.split()
        search_duplicate_string = ""
        kit_word_dict, test_result, kit_duplicate_check = get_data(word_list, index_offset , line_no, kit, kit_number)
        #search_duplicate_string = kit_word_dict["key_string"] + "_" + kit_word_dict["cM"] + "_" + kit_word_dict["segments"]  # allow for recent tree changes
        search_duplicate_string = kit_duplicate_check
        #print(kit_word_dict["who"], search_duplicate_string)
        #no_in_tree = kit_word_dict["Tree"]

        if kit_word_dict["key_string"] not in kit_key_list:
              kit_key_list.append(kit_word_dict["key_string"])
        else:
            error_string = kit + " " + str(line_no) + " " + kit_word_dict["key_string"]
            duplicate_key_list.append(error_string)
        if search_duplicate_string in kit_who_list:
            old_index = kit_who_dict[search_duplicate_string]
            old_index2 = dna_list_index.index(old_index)
            old_test = dna_list[old_index2]
            #print(old_index, search_duplicate_string , "!!!!" , old_test.kit, old_test.index, old_test.keystring , "posible duplicate", kit, line_no, test_result.keystring)
            if search_duplicate_string in duplicate_dict:
                duplicate_dict[search_duplicate_string].append(test_result.mega_index)
            else:
                duplicate_dict[search_duplicate_string] = [old_test.mega_index, test_result.mega_index]
        else:
            kit_who_list.append(search_duplicate_string)
            kit_who_dict[search_duplicate_string] = line_no + index_offset
        kit_word_dict["index"] = line_no + index_offset
        #kit_person_dict[int(line_no) + int(index_offset)] = test_result
        dict_of_lists[int(line_no) + int(index_offset)] = kit_word_dict
        dna_list.append(test_result)
        total_dna_list.append(test_result)
        keystring = test_result.keystring
        if keystring not in cousin_key_list:
            cousin_key_list.append(keystring)
            Test_Result_Dict[keystring] = test_result

        dna_list_index.append(line_no + index_offset)
        line_no = line_no + 1
    return dict_of_lists


def load_matches(file_list, kit_number, total_dna_list):
    dict_of_lists = {}
    kit_offset_index = 0
    kit_who_list = []
    kit_key_list = []
    Test_Result_Dict = {}
    cousin_key_list = []
    duplicate_key_list=[]
    kit_who_dict = {}
    dna_list = []
    dna_list_index = []
    duplicate_dict = {}


    file_list_length = len(file_list)
    for text_file in file_list:
        kit_person = file_list[0]
        temp_dict_of_lists = {}
        #print (text_file, 10000* kit_offset_index)
        temp_dict_of_lists = get_cousin_dict(text_file, kit_number, kit_offset_index * 20000, kit_key_list, duplicate_key_list, kit_who_list,
                                             kit_who_dict, dna_list, dna_list_index, duplicate_dict,total_dna_list, cousin_key_list, Test_Result_Dict)
        dict_of_lists.update(temp_dict_of_lists)
        kit_offset_index += 1
    duplicate_index = 1
    for error in duplicate_key_list:
        print(duplicate_index, "duplicate key >>>>>", error)
        duplicate_index += 1
    duplicate_index = 1
    for duplo in duplicate_dict:
        new_index = 0
        print("--------------------" , duplicate_index , "------------------------------------")
        for mega_index1 in duplicate_dict[duplo]:
              old_index2 = dna_list_index.index(mega_index1)
              test = dna_list[old_index2]
              kitname = test.kit
              line_no = test.index
              keystring = test.keystring
              check = test.kit_duplicate_check
              print( check, kitname, line_no, keystring)
        duplicate_index += 1

    return dict_of_lists, Test_Result_Dict

def main():


    total_dna_list = []
    kit1_file_list = ["Glyn", "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM","Dad_B"]
    #kit1_file_list = ["Glyn"]
    kit1_number = 1

    kit2_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM" , "Wayne_8cM", "Wayne_7cM","Wayne_6cM_new","Wayne_A"]
    #kit2_file_list = ["Wayne"]
    kit2_number = 2
    #kit2_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM", "Sally_6cm_A","Sally_L"]
    #kit2_file_list = ["Helen", "Helen_B"]

    kit1_dict_of_lists, kit1_Test_Result_Dict = load_matches(kit1_file_list, kit1_number, total_dna_list)
    kit1_index_list = []
    kit1_index_dict = {}
    kit1_cM_dict = {}
    kit1_index_keystring_dict = {}
    for cousin in kit1_dict_of_lists:
        #print(cousin,kit1_dict_of_lists[cousin]["key_string"])
        key = kit1_dict_of_lists[cousin]["key_string"]
        #key = kit1_dict_of_lists[cousin]["who"]
        kit1_index_dict[kit1_dict_of_lists[int(cousin)]["key_string"]] = kit1_dict_of_lists[int(cousin)]["index"]
        kit1_index_keystring_dict[kit1_dict_of_lists[int(cousin)]["key_string"]] = kit1_dict_of_lists[int(cousin)]["who"]
        kit1_cM_dict[kit1_dict_of_lists[int(cousin)]["key_string"]] = int(kit1_dict_of_lists[int(cousin)]["cM"])
        kit1_index_list.append(key)



    kit2_dict_of_lists, kit2_Test_Result_Dict = load_matches(kit2_file_list, kit2_number, total_dna_list)
    kit2_index_dict = {}
    kit2_index_list = []
    kit2_keystring_list = []
    kit2_index_keystring_dict = {}
    for cousin in kit2_dict_of_lists:
        key = kit2_dict_of_lists[cousin]["key_string"]
        #key = kit2_dict_of_lists[cousin]["who"]
        kit2_index_dict[kit2_dict_of_lists[int(cousin)]["key_string"]] = kit2_dict_of_lists[int(cousin)]["index"]
        kit2_index_keystring_dict[kit2_dict_of_lists[int(cousin)]["key_string"]] = kit2_dict_of_lists[int(cousin)]["key_string"]
        kit2_index_list.append(key)

    intersection_list = list(set(kit1_index_list).intersection(set(kit2_index_list)))

    #print(len(intersection_list))
    intersection_dict = {}
    intersection_index = 1
    for cousin in intersection_list:
        #print(intersection_index, cousin, int(kit1_index_dict[cousin]) )
        print(intersection_index, kit1_Test_Result_Dict[cousin].who,kit1_Test_Result_Dict[cousin].centimorgans, kit2_Test_Result_Dict[cousin].who, kit2_Test_Result_Dict[cousin].centimorgans)
        #intersection_dict[cousin] = int(kit1_index_dict[cousin])
        intersection_dict[cousin] = int(kit1_index_dict[cousin])
        intersection_index += 1

    intersectcount = 1
    for cousin_key in sorted(intersection_dict.items(), key=lambda x: x[1], reverse=False):
        kit1_index = cousin_key[1]
        key_string = cousin_key[0]
        kit2_index = kit2_index_dict[key_string]
        kit1_cousin_info = kit1_dict_of_lists[kit1_index]
        kit2_cousin_info = kit2_dict_of_lists[kit2_index]
        kit1_people = 0
        kit2_people = 0
        kit1_cousin = kit1_cousin_info["who"]
        kit2_cousin = kit2_cousin_info["who"]
        kit1_cousin_cM = kit1_cousin_info["cM"]
        kit2_cousin_cM = kit2_cousin_info["cM"]
        kit1_cousin_seg = kit1_cousin_info["segments"]
        kit2_cousin_seg = kit2_cousin_info["segments"]
        if "People" in kit1_cousin_info:
             kit1_people = kit1_cousin_info["People"] + " People"
        if "People" in kit2_cousin_info:
             kit2_people = kit2_cousin_info["People"] + " People"

        if "Tree" in kit1_cousin_info:
             kit1_people = kit1_cousin_info["Tree"]
        if "Tree" in kit2_cousin_info:
             kit2_people = kit2_cousin_info["Tree"]

        if kit1_people == kit2_people:   # check its the same person not a homonym
             print('{0:4} | {1:36}  {2:4} | {3:4}cM | {4:2}seg | {5:13}|***| {6:4}cM | {7:2}seg | {8:13}| {9:4} |'\
                   .format(intersectcount, kit1_cousin, kit1_index, kit1_cousin_cM, kit1_cousin_seg, kit1_people, kit2_cousin_cM, kit2_cousin_seg, kit2_people,kit2_index))
             intersectcount += 1
        else:
            print(
                '{0:3} | {1:36}  {2:4} | {3:4}cM | {4:2}seg | {5:13}|***| {6:4}cM | {7:2}seg | {8:13}| {9:4} |' \
                .format(intersectcount, kit1_cousin, kit1_index, kit1_cousin_cM, kit1_cousin_seg, kit1_people,
                        kit2_cousin_cM, kit2_cousin_seg, kit2_people, kit2_index))
            print ("ouch ", )

 #   for everbody in total_dna_list:
  #      print (everbody.who, everbody.kit, everbody.keystring)



if __name__ == '__main__':
      main()
