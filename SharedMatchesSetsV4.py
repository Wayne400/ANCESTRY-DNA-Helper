
import re
import sys
import operator
from Load_Ancestry_V5 import  load_matches
from Profiles import load_profile



def swap_in_index(list_of_lists,homonym_to_primarykey_dict):

    new_list_of_lists = []
    for list in list_of_lists:
        new_list = []
#        print(list)
        for homonym in list:
            try:
                primary_key = homonym_to_primarykey_dict[homonym]
                new_list.append(primary_key)
            except:
                print("duplicate key = ", homonym)

        new_list_of_lists.append(new_list)
    return new_list_of_lists

def filter_list(list_to_filter, index_match_filter_list):

    new_filtered_list = []
    for entry in list_to_filter:
        if entry not in index_match_filter_list:
            new_filtered_list.append(entry)
    return new_filtered_list



def get_shared_matches(kit3, match_filter_list, file_path):
    list_of_lists = []
    new_list_of_lists = []
    homonym_to_primarykey_dict = {}
    check_all_entry_list = []  # check to find all shared matches are indexed too
    primary_entry_list = []
    print("here", match_filter_list)

    for line in open(file_path + kit3 + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        homonym_to_primarykey_dict[orig_word_list[1]] = int(orig_word_list[0])  # will overwrite additonal lines
        del orig_word_list[0]
        check_all_entry_list.extend(orig_word_list)
        primary_entry_list.append(orig_word_list[0])
    for entry in check_all_entry_list:
        if entry not in primary_entry_list:
            print(entry, "index is missing in file _Shared")
            exit(1)

    index_match_filter_list = []
    for entry in match_filter_list:
            index_match_filter_list.append(homonym_to_primarykey_dict[entry])
    print(index_match_filter_list)
    last_cousin = "wally"
    for line in open(file_path + kit3 + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        this_cousin = orig_word_list[1]
        cousin_primary_index =  orig_word_list[0]
        del orig_word_list[0]  # remove index
        #if this_cousin not in match_filter_list:
        if (this_cousin != last_cousin) and (this_cousin not in match_filter_list):
              #  del orig_word_list[0]  # the index number
                list_of_lists.append(filter_list(orig_word_list, match_filter_list))
                last_cousin = this_cousin
        elif (this_cousin == last_cousin) and (this_cousin not in match_filter_list):
               # del orig_word_list[0]  # dont add  cousin name again
                del orig_word_list[0]
                list_of_lists[-1].extend(filter_list(orig_word_list, match_filter_list))

        new_list_of_lists = swap_in_index(list_of_lists, homonym_to_primarykey_dict)


    return list_of_lists, new_list_of_lists


def get_places(kit1_places, kit1_who_dict, file_path):
    dict_of_places = {}
    line_no = 1
    for line in open(file_path + kit1_places + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        this_cousin = kit1_who_dict[orig_word_list[1]]
        del orig_word_list[0]  # the index number
        del orig_word_list[0]  # cousin
        dict_of_places[this_cousin] = orig_word_list
        line_no += 1

    return dict_of_places


def main():
    person = "Wayne"
    file_path = "c:/Users/Wayne/DNA/"

    if len(sys.argv) > 1:
      if sys.argv[1] == "ubuntu":
        file_path = '/mnt/c/Users/Wayne/DNA/'
        person = sys.argv[2]
      else:
        file_path = "c:/Users/Wayne/DNA/"
    duplicate_check_flag = False
    print_filter = False
    places_flag = False
    match_filter_list = [""]

    if person == "Glyn":
        kit3 = 'Glyn_Shared'
        kit3_places = 'Glyn_Places'
        kit6 = 'Glyn_Common2'
        kit1_file_list,kit2_file_list,kit4_file_list, kit5_file_list, kit7_file_list, kit8_file_list, match_filter_list = load_profile(person)

    if person == "Wayne":
        kit3 = 'Wayne_Shared'
        kit3_places = 'Wayne_Places'
        kit6 = 'Wayne_Common'
        kit1_file_list,kit2_file_list,kit4_file_list, kit5_file_list, kit7_file_list, kit8_file_list, match_filter_list = load_profile(person)

    if person == "Gary":
        kit3 = 'Gary_Shared'
        kit3_places = 'Gary_Places'
        kit6 = 'Gary_Common'
        kit1_file_list,kit2_file_list,kit4_file_list, kit5_file_list, kit7_file_list, kit8_file_list, match_filter_list = load_profile(person)

    if person == "Sally":
        kit3 = 'Sally_Shared'
        kit3_places = 'Sally_Places'
        kit6 = 'Sally_Common'
        kit1_file_list,kit2_file_list,kit4_file_list, kit5_file_list, kit7_file_list, kit8_file_list, match_filter_list = load_profile(person)


    dict_of_places = []
    list_of_lists, new_list_of_lists = get_shared_matches(kit3, match_filter_list, file_path)
    kit1_Test_Result_Dict = load_matches(kit1_file_list, 1, duplicate_check_flag, file_path)
    kit1_key_dict = {}
    kit1_who_dict = {}
    kit1_index_dict = {}
    kit1_index_keystring_dict = {}
    kit1_cM_dict = {}
    kit1_primary_index = {}
    kit1_keystring_list = []
    for kit1_Test_Result in kit1_Test_Result_Dict:
        kit1_keystring_list.append(kit1_Test_Result_Dict[kit1_Test_Result].keystring)
    for kit1_Test_Result in kit1_Test_Result_Dict:
        kit1_index_dict[kit1_Test_Result_Dict[kit1_Test_Result].index] = kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_who_dict[kit1_Test_Result_Dict[kit1_Test_Result].who] = kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_index_keystring_dict[kit1_Test_Result_Dict[kit1_Test_Result].index] = kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_cM_dict[kit1_Test_Result_Dict[kit1_Test_Result].keystring] = int(kit1_Test_Result_Dict[kit1_Test_Result].centimorgans)
        kit1_primary_index[str(kit1_Test_Result_Dict[kit1_Test_Result].index) + "." + kit1_Test_Result_Dict[kit1_Test_Result].who] = \
                kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_key_dict[kit1_Test_Result_Dict[kit1_Test_Result].keystring] = kit1_Test_Result_Dict[kit1_Test_Result].index

#    print(kit1_index_dict)
    even_newer_list_of_lists = swap_in_index(new_list_of_lists, kit1_index_dict)



    kit2_Test_Result_Dict = load_matches(kit2_file_list, 2, duplicate_check_flag, file_path)
    kit2_keystring_list = []
    for kit2_Test_Result in kit2_Test_Result_Dict:
        kit2_keystring_list.append(kit2_Test_Result_Dict[kit2_Test_Result].keystring)
    kit4_Test_Result_Dict = load_matches(kit4_file_list, 4, duplicate_check_flag, file_path)
    kit4_keystring_list = []
    for kit4_Test_Result in kit4_Test_Result_Dict:
        kit4_keystring_list.append(kit4_Test_Result_Dict[kit4_Test_Result].keystring)

    kit5_Test_Result_Dict = load_matches(kit5_file_list, 5, duplicate_check_flag, file_path)
    kit5_keystring_list = []
    for kit5_Test_Result in kit5_Test_Result_Dict:
        kit5_keystring_list.append(kit5_Test_Result_Dict[kit5_Test_Result].keystring)

    kit7_Test_Result_Dict = load_matches(kit7_file_list, 7, duplicate_check_flag, file_path)
    kit7_keystring_list = []
    for kit7_Test_Result in kit7_Test_Result_Dict:
        kit7_keystring_list.append(kit7_Test_Result_Dict[kit7_Test_Result].keystring)

    kit8_Test_Result_Dict = load_matches(kit8_file_list, 8, duplicate_check_flag, file_path)
    kit8_keystring_list = []
    for kit8_Test_Result in kit8_Test_Result_Dict:
        kit8_keystring_list.append(kit8_Test_Result_Dict[kit8_Test_Result].keystring)





    dict_of_sets = {}
    dict_of_shared_matches = {}
    for cousin_set in even_newer_list_of_lists:
        index = cousin_set[0]
        dict_of_sets[index] = set(cousin_set)
        del cousin_set[0]  # dont include key index for shared matches
        dict_of_shared_matches[index] = cousin_set

    dict_of_places = []
    dict_of_places = get_places(kit3_places, kit1_who_dict, file_path)



    print("*********************** Combining now *****************************")
    print("***************************************************************")

    new_cousin_list=[]
    new_dict_of_lists = {}
    for cousin1 in dict_of_sets:
        for cousin2 in dict_of_sets:
            if cousin1 != cousin2:
                if len(list(dict_of_sets[cousin1].intersection(dict_of_sets[cousin2]))) > 0:
                    #print("adding to ", cousin1 ,cousin2, (dict_of_sets[cousin2].intersection(dict_of_sets[cousin1])))
                    dict_of_sets[cousin1] = dict_of_sets[cousin1].union(dict_of_sets[cousin2])
                    dict_of_sets[cousin2] = dict_of_sets[cousin1].union(dict_of_sets[cousin2])

    print("***********************All done *****************************")
    print("****************************************************")
    print("*********************** cousin filters = ", match_filter_list, "*****************************")

    super_set = set()
    for cousin1 in dict_of_sets:
            #Cousin1_index = int(cousin1)
            #print(cousin1, len(dict_of_sets[cousin1]), dict_of_sets[cousin1])
            #print(super_set)
            if len(list(dict_of_sets[cousin1].intersection(super_set))) == 0:
                super_set = super_set.union(dict_of_sets[cousin1])
                new_dict_of_lists[cousin1] = list(dict_of_sets[cousin1])
                new_cousin_list.append(cousin1)

    print("****************************************************")
    print("****************************************************")
    #print(orig_dict_of_sets)
    supertotal = 0
    supergroup = 1
    kit1_supergroup = {}
    #print(super_list)
    #print(new_cousin_list)
    chromo_dict = {}
    for cousin in new_cousin_list:
            punter = 0
            print("****************************************************")
            group_total = len(new_dict_of_lists[cousin])
            banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
            print(supergroup, banner_string,  cousin, group_total,  banner_string)

            temp_cM_dict = {}
            #kit1_supergroup[cousin] = ""
            for cousin4 in new_dict_of_lists[cousin]:
                temp_cM_dict[cousin4] = kit1_cM_dict[cousin4]

            for cousin4 in sorted(temp_cM_dict, key=temp_cM_dict.get, reverse=True):
                    punter += 1

                    for cousin3 in kit1_keystring_list:  # step though all the cousins and match on the shared match group
                        match_kit2 = ""
                        match_kit4 = ""
                        match_kit5 = ""
                        match_kit7 = ""
                        match_kit8 = ""
                        common_string = ""
                        place_list = []
                        filter_flag = False
                        places_string = ""
                        trail_string = ""
                        if cousin3 in dict_of_places:
                            list_of_places = dict_of_places[cousin3]
                            if len(list_of_places) > 0:
                                for place in list_of_places:
                                   places_string = places_string + " " + place

                        no_of_shared_matches = 0
                        if cousin3 == cousin4:
                            if cousin3 in dict_of_shared_matches:
                                no_of_shared_matches = len(dict_of_shared_matches[cousin4])

                            if cousin3 in kit2_keystring_list:
                                match_kit2 = kit2_file_list[0] + "=" + kit2_Test_Result_Dict[cousin4].centimorgans + "cM"
                            if cousin3 in kit4_keystring_list:
                                match_kit4 = kit4_file_list[0] + "=" + kit4_Test_Result_Dict[cousin4].centimorgans + "cM"
                            if cousin3 in kit5_keystring_list:
                                match_kit5 = kit5_file_list[0] + "=" + kit5_Test_Result_Dict[cousin4].centimorgans + "cM"
                            if cousin3 in kit7_keystring_list:
                                match_kit7 = kit7_file_list[0] + "=" + kit7_Test_Result_Dict[cousin4].centimorgans + "cM"
                            if cousin3 in kit8_keystring_list:
                                match_kit8 = kit8_file_list[0] + "=" + kit8_Test_Result_Dict[cousin4].centimorgans + "cM"

                            kit1_index = kit1_key_dict[cousin4]

                            kit1_cM = kit1_Test_Result_Dict[cousin4].centimorgans
                            kit1_seg = kit1_Test_Result_Dict[cousin4].segments

                            print('{0:6} {1:40} {2:3}cM {3:2}seg   {4:11} {5:11} {6:11} {7:11} {8:11}  *{9:1}* {10:30}' \
                          .format(kit1_index, cousin4, kit1_cM, kit1_seg,
                                  match_kit2, match_kit4, match_kit5, match_kit7, match_kit8, str(no_of_shared_matches),
                                  places_string))

            supergroup += 1
            supertotal = supertotal + group_total
    print("************************************************************************************************")
    print("supertotal is ", supertotal)



if __name__ == '__main__':
      main()
