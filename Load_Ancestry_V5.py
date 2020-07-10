
import re


class DNA_Result(object):

    def __init__(self, index=99999, offset = 0, who="", centimorgans=0, segments=0, people="", keystring="", tree="", kit_duplicate_check="", kit="wally", kit_number = 99):


        self.index = index
        self.mega_index = index + offset
        self.who = who
        self.centimorgans = centimorgans
        self.segments = segments
        self.people = people
        self.keystring = keystring
        self.people = people
        self.tree = tree
        self.kit_duplicate_check = kit_duplicate_check
        self.kit = kit
        self.kit_number = kit_number



def get_data(word_list,index_offset , line_no, kit, kit_number):
    new_word_dict = {}
    new_word_dict["People"] = "zero"
    new_word_dict["Tree"] = ""
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

    test_result = DNA_Result(int(line_no) , index_offset, new_word_dict["who"] , new_word_dict["cM"] ,
                             new_word_dict["segments"], new_word_dict["People"], new_word_dict["key_string"],
                             new_word_dict["Tree"], kit_duplicate_check , kit, kit_number)


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
        search_duplicate_string = kit_duplicate_check
        #print(test_result.keystring)

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
            #print(keystring)

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

    return  Test_Result_Dict, cousin_key_list

def main():


    total_dna_list = []
    kit1_index_list = []
    kit2_index_list = []
    kit1_file_list = ["Glyn", "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM","Dad_B"]
    #kit1_file_list = ["Glyn"]
    #kit1_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM" , "Wayne_8cM", "Wayne_7cM","Wayne_6cM","Wayne_A"]
    kit1_number = 1

    #kit2_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM" , "Wayne_8cM", "Wayne_7cM","Wayne_6cM","Wayne_A"]
    #kit2_file_list = ["Wayne"]
    kit2_number = 2
    kit2_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM","Sally_L"]
    #kit2_file_list = ["Helen", "Helen_B"]

    kit1_Test_Result_Dict, kit1_index_list = load_matches(kit1_file_list, kit1_number, total_dna_list)
    kit2_Test_Result_Dict, kit2_index_list = load_matches(kit2_file_list, kit2_number, total_dna_list)

    intersection_list = list(set(kit1_index_list).intersection(set(kit2_index_list)))

    intersectcount = 1
    for cousin_key in intersection_list:
        key_string = cousin_key
        kit1_index = kit1_Test_Result_Dict[key_string].index
        kit2_index = kit2_Test_Result_Dict[key_string].index
        kit1_cousin = kit1_Test_Result_Dict[key_string].who
        kit2_cousin = kit2_Test_Result_Dict[key_string].who
        kit1_cousin_cM = kit1_Test_Result_Dict[key_string].centimorgans
        kit2_cousin_cM = kit2_Test_Result_Dict[key_string].centimorgans
        kit1_cousin_seg = kit1_Test_Result_Dict[key_string].segments
        kit2_cousin_seg = kit2_Test_Result_Dict[key_string].segments
        if kit1_Test_Result_Dict[key_string].people != 'zero':
            kit1_people = kit2_Test_Result_Dict[key_string].people + " People"
        else:
            kit1_people = ''

        if kit2_Test_Result_Dict[key_string].people != 'zero':
            kit2_people = kit2_Test_Result_Dict[key_string].people + " People"
        else:
            kit2_people = ''

        print('{0:4} | {1:36}  {2:4} | {3:4}cM | {4:2}seg | {5:13}|***| {6:4}cM | {7:2}seg | {8:13}| {9:4} |'\
                   .format(intersectcount, kit1_cousin, kit1_index, kit1_cousin_cM, kit1_cousin_seg, kit1_people, kit2_cousin_cM, kit2_cousin_seg, kit2_people,kit2_index))
        intersectcount += 1

    difference_list = list(set(kit1_index_list).symmetric_difference(set(kit2_index_list)))
    difference_count = 1
    cousin1_list = []
    cousin2_list = []
    cousin1_shadow_list = []
    cousin2_shadow_list = []

    for cousin_key in difference_list:
        if cousin_key in kit1_index_list:
            cousin = kit1_Test_Result_Dict[cousin_key].who
            if kit1_Test_Result_Dict[cousin_key].people != 'zero':
                cousin1_list.append(cousin)
                cousin1_shadow_list.append(kit1_Test_Result_Dict[cousin_key].keystring)
        else:
            cousin = kit2_Test_Result_Dict[cousin_key].who
            if kit2_Test_Result_Dict[cousin_key].people != 'zero':
                cousin2_list.append(cousin)
                cousin2_shadow_list.append(kit2_Test_Result_Dict[cousin_key].keystring)
        #print (difference_count, cousin)
        difference_count += 1

    mismatch_list = []
    mismatch_index = 1
    mismatch_list = list(set(cousin1_list).intersection(set(cousin2_list)))
    for cousin_who in mismatch_list:
        index1 = cousin1_list.index(cousin_who)
        index2 = cousin2_list.index(cousin_who)
        key1 = cousin1_shadow_list[index1]
        key2 = cousin2_shadow_list[index2]
        cm1 = kit1_Test_Result_Dict[key1].centimorgans
        cm2 = kit2_Test_Result_Dict[key2].centimorgans
        #print(mismatch_index, cousin_who, key1, key2)
        print('{0:4} | {1:36} | {2:36} {3:3} | {4:36} {5:3} '\
                   .format(mismatch_index, cousin_who, key1, cm1, key2, cm2))

        mismatch_index += 1




 #   for everbody in total_dna_list:
  #      print (everbody.who, everbody.kit, everbody.keystring)



if __name__ == '__main__':
      main()
