
import re




def get_data(word_list,index_offset):
    new_word_dict = {}
    i = 0
    new_word_dict["index"] = word_list[0]
    for column in word_list:
        if column == "Cousin" and index_offset == 0:
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
            #print(new_word_dict["index"], word_list)
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

    return new_word_dict


def get_cousin_dict(kit, index_offset,kit_who_list, duplicate_check_flag):

#    kit_who_list = []
    dict_of_lists = {}
    line_no = 1
    for line in open(kit + '.txt'):
        line = line.rstrip()
        line = line.replace('\t',' ')
        line = line.replace(',', '')
        word_list = line.split()
        kit_word_dict = get_data(word_list, index_offset)
        #print(kit_word_dict)
        search_duplicate_string = kit_word_dict["who"] + "_" + kit_word_dict["cM"] + "_" + kit_word_dict["segments"]  # allow for recent tree changes
        #print(kit_word_dict["who"])
        #no_in_tree = kit_word_dict["Tree"]
        if duplicate_check_flag:
          if search_duplicate_string in kit_who_list:
            keystring_duplicate = kit_word_dict["key_string"]
            print(kit_who_list.index(search_duplicate_string) + 1, kit, line_no, "duplicate", kit_word_dict["who"], kit_word_dict["cM"], "cM",
                   search_duplicate_string, keystring_duplicate)
          else:
            kit_who_list.append(search_duplicate_string)
        kit_word_dict["index"] = line_no + index_offset
        dict_of_lists[int(line_no + index_offset)] = kit_word_dict
        line_no = line_no + 1
    return dict_of_lists


def load_matches(file_list, duplicate_check_flag):
    dict_of_lists = {}
    kit_offset_index = 0
    kit_who_list = []
    for text_file in file_list:
        temp_dict_of_lists = {}
        #print (text_file, 10000* kit_offset_index)
        temp_dict_of_lists = get_cousin_dict(text_file, kit_offset_index * 20000, kit_who_list, duplicate_check_flag)
        dict_of_lists.update(temp_dict_of_lists)
        kit_offset_index += 1

    return dict_of_lists

def main():


    kit1_file_list = ["Glyn", "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_7cM_B", "Dad_6cM","Dad_6cM_F" ,"Dad_B"]
    kit2_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM" , "Wayne_8cM", "Wayne_7cM","Wayne_6cM","Wayne_A"]

    #kit2_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM", "Sally_6cM_A","Sally_L"]
    #kit2_file_list = ["Helen", "Helen_B"]
    duplicate_check_flag = True

    kit1_dict_of_lists = load_matches(kit1_file_list, duplicate_check_flag)
    kit1_index_list = []
    kit1_index_dict = {}
    kit1_cM_dict = {}
    kit1_index_keystring_dict = {}
    for cousin in kit1_dict_of_lists:
        #print(cousin,kit1_dict_of_lists[cousin]["key_string"])
        #key = kit1_dict_of_lists[cousin]["key_string"]
        key = kit1_dict_of_lists[cousin]["who"]
        kit1_index_dict[kit1_dict_of_lists[int(cousin)]["who"]] = kit1_dict_of_lists[int(cousin)]["index"]
        kit1_index_keystring_dict[kit1_dict_of_lists[int(cousin)]["index"]] = kit1_dict_of_lists[int(cousin)]["key_string"]
        kit1_cM_dict[kit1_dict_of_lists[int(cousin)]["key_string"]] = int(kit1_dict_of_lists[int(cousin)]["cM"])
        kit1_index_list.append(key)



    kit2_dict_of_lists = load_matches(kit2_file_list, duplicate_check_flag)
    kit2_index_dict = {}
    kit2_index_list = []
    kit2_keystring_list = []
    kit2_index_keystring_dict = {}
    for cousin in kit2_dict_of_lists:
        #key = kit2_dict_of_lists[cousin]["key_string"]
        key = kit2_dict_of_lists[cousin]["who"]
        kit2_index_dict[kit2_dict_of_lists[int(cousin)]["who"]] = kit2_dict_of_lists[int(cousin)]["index"]
        kit2_index_keystring_dict[kit2_dict_of_lists[int(cousin)]["index"]] = kit2_dict_of_lists[int(cousin)]["key_string"]
        kit2_index_list.append(key)

    intersection_list = list(set(kit1_index_list).intersection(kit2_index_list))

    #print(len(intersection_list))
    intersection_dict = {}

    for cousin in intersection_list:
        intersection_dict[cousin] = int(kit2_index_dict[cousin])

    intersectcount = 1
    for intersection_dict in sorted(intersection_dict.items(), key=lambda x: x[1], reverse=False):
        kit1_people = 0
        kit2_people = 0
        cousin = intersection_dict[0]
        kit1_cousin_index = kit1_index_dict[cousin]
        kit1_cousin = kit1_dict_of_lists[kit1_cousin_index]["who"]
        kit2_cousin_index = kit2_index_dict[cousin]
        kit2_cousin = kit2_dict_of_lists[kit2_cousin_index]["who"]
        kit1_cousin_cM = kit1_dict_of_lists[kit1_cousin_index]["cM"]
        kit2_cousin_cM = kit2_dict_of_lists[kit2_cousin_index]["cM"]
        kit1_cousin_seg = kit1_dict_of_lists[kit1_cousin_index]["segments"]
        kit2_cousin_seg = kit2_dict_of_lists[kit2_cousin_index]["segments"]
        if "People" in kit1_dict_of_lists[kit1_cousin_index]:
             kit1_people = kit1_dict_of_lists[kit1_cousin_index]["People"] + " People"
        if "People" in kit2_dict_of_lists[kit2_cousin_index]:
             kit2_people = kit2_dict_of_lists[kit2_cousin_index]["People"] + " People"

        if "Tree" in kit1_dict_of_lists[kit1_cousin_index]:
             kit1_people = kit1_dict_of_lists[kit1_cousin_index]["Tree"]
        if "Tree" in kit2_dict_of_lists[kit2_cousin_index]:
             kit2_people = kit2_dict_of_lists[kit2_cousin_index]["Tree"]

        if kit1_people == kit2_people:   # check its the same person not a homonym
             #print('{0:4} | {1:36}  {2:4} | {3:4}cM | {4:2}seg | {5:13}|***| {6:4}cM | {7:2}seg | {8:13}| {9:4} |'\
             #      .format(intersectcount, kit1_cousin, kit1_cousin_index, kit1_cousin_cM, kit1_cousin_seg, kit1_people, kit2_cousin_cM, kit2_cousin_seg, kit2_people,kit2_cousin_index))
             intersectcount += 1
        else:
            print(
                '{0:3} | {1:36}  {2:4} | {3:4}cM | {4:2}seg | {5:13}|***| {6:4}cM | {7:2}seg | {8:13}| {9:4} |' \
                .format(intersectcount, kit1_cousin, kit1_cousin_index, kit1_cousin_cM, kit1_cousin_seg, kit1_people,
                        kit2_cousin_cM, kit2_cousin_seg, kit2_people, kit2_cousin_index))
            print ("ouch ", )




if __name__ == '__main__':
      main()
