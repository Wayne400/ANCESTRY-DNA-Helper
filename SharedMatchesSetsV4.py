
import re
import sys
import operator
from Load_Ancestry_V5 import  load_matches
from Profiles import load_profile


def load_surnames(file_path, filename):
    #  file_path = "c:/Users/Wayne/DNA/"
    word_list = []
    surnames = {}
    for line in open(file_path + filename + '.txt', encoding='latin-1'):
        line = line.rstrip()
        word_list = line.split(',')
        key = word_list[0]
        del word_list[0]
        surnames[key] = word_list
    return surnames


def swap_in_index(list_of_lists,homonym_to_primarykey_dict):

    new_list_of_lists = []
    for list in list_of_lists:
        new_list = []
        # print(list)
        for homonym in list:
            try:
                primary_key = homonym_to_primarykey_dict[homonym]
                new_list.append(primary_key)
            except:
                print("duplicate key = ", homonym)
                print(list)
                exit(1)

        new_list_of_lists.append(new_list)
    return new_list_of_lists

def filter_list(list_to_filter, index_match_filter_list):

    new_filtered_list = []
    for entry in list_to_filter:
        if entry not in index_match_filter_list:
            new_filtered_list.append(entry)
    return new_filtered_list



def get_shared_matches(person, match_filter_list, file_path):
    list_of_lists = []
    new_list_of_lists = []
    homonym_to_primarykey_dict = {}
    check_all_entry_list = []  # check to find all shared matches are indexed too
    primary_entry_list = []
    print("here", match_filter_list)

    for line in open(file_path + person + '_Shared.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
     #   print(orig_word_list)  # debug only
        homonym_to_primarykey_dict[orig_word_list[1]] = int(orig_word_list[0])  # will overwrite additonal lines
        del orig_word_list[0]
        check_all_entry_list.extend(orig_word_list)
        primary_entry_list.append(orig_word_list[0])
    for entry in check_all_entry_list:
        if entry not in primary_entry_list:
            print(entry, " index is missing in file " + person + "_Shared")
            exit(1)
    index_match_filter_list = []
    for entry in match_filter_list:
            index_match_filter_list.append(homonym_to_primarykey_dict[entry])
    #print(index_match_filter_list)
    last_cousin = "wally"
    for line in open(file_path + person + '_Shared.txt'):
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

    return list_of_lists, new_list_of_lists #, homonym_to_primarykey_dict


def get_places(kit1_places, file_path, kit1_index_keystring_dict):
    dict_of_places = {}
    line_no = 1
#    print(kit1_index_keystring_dict)
    for line in open(file_path + kit1_places + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        this_cousin = kit1_index_keystring_dict[int(orig_word_list[0])]
        del orig_word_list[0]  # the index number
        del orig_word_list[0]  # cousin
        dict_of_places[this_cousin] = orig_word_list
        line_no += 1

    return dict_of_places


def print_cluster(supergroup, cousin, new_dict_of_lists,kit1_cM_dict, kit1_keystring_list,
                  dict_of_places, dict_of_shared_matches,kit1_key_dict, kit2_keystring_list, kit3_keystring_list,
                  kit4_keystring_list, kit5_keystring_list, kit6_keystring_list, punters_list, Test_Result_Dict,mode,centimorgan ):
    punter = 0
    banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    #print(new_dict[int(cluster_search)])
    #cousin = new_dict[int(cluster_search)]
    group_total1 = len(new_dict_of_lists[cousin])
#    print(group_total1, banner_string, cousin, banner_string)
    temp_cM_dict = {}
    for cousin4 in new_dict_of_lists[cousin]:
        temp_cM_dict[cousin4] = kit1_cM_dict[cousin4]

    for cousin4 in sorted(temp_cM_dict, key=temp_cM_dict.get, reverse=True):
        punter += 1

        for cousin3 in kit1_keystring_list:  # step though all the cousins and match on the shared match group
            match_kit2 = ""
            match_kit3 = ""
            match_kit4 = ""
            match_kit5 = ""
            match_kit6 = ""
            places_string = ""
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
                    match_kit2 = punters_list[0] + "=" + Test_Result_Dict[1][cousin4].centimorgans + "cM"
                if cousin3 in kit3_keystring_list:
                    match_kit3 = punters_list[1] + "=" + Test_Result_Dict[2][cousin4].centimorgans + "cM"
                if cousin3 in kit4_keystring_list:
                    match_kit4 = punters_list[2] + "=" + Test_Result_Dict[3][cousin4].centimorgans + "cM"
                if cousin3 in kit5_keystring_list:
                    match_kit5 = punters_list[3] + "=" + Test_Result_Dict[4][cousin4].centimorgans + "cM"
                if cousin3 in kit6_keystring_list:
                    match_kit6 = punters_list[4] + "=" + Test_Result_Dict[5][cousin4].centimorgans + "cM"

                kit1_index = kit1_key_dict[cousin4]

                kit1_cM = Test_Result_Dict[0][cousin4].centimorgans
                kit1_seg = Test_Result_Dict[0][cousin4].segments
                if int(kit1_cM) == centimorgan or centimorgan == 0:
                  print('{0:6} {1:40} {2:3}cM {3:2}seg   {4:11} {5:11} {6:11} {7:11} {8:11}  *{9:1}* *{10:1}* {11:30}' \
                      .format(kit1_index, cousin4, kit1_cM, kit1_seg,
                              match_kit2, match_kit3, match_kit4, match_kit5, match_kit6,
                              str(no_of_shared_matches), supergroup,
                              places_string))

    return True


def print_cluster2(cousin, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                  surnames, kit1_key_dict, Test_Result_Dict, centimorgan ):
    punter = 0
    temp_cM_dict = {}
    cousin_list = new_dict_of_lists[cousin]
    surnames_keys_list = surnames.keys()
    temp_surnames = {}
    surname_found = False
    for surname in cousin_list:  # this is a pre-check to see if its worth doing the analysis at the enf
        if surname in surnames_keys_list:
            temp_surnames[surname] = surnames[surname]
            surname_found = True

    for cousin4 in new_dict_of_lists[cousin]:
        temp_cM_dict[cousin4] = kit1_cM_dict[cousin4]

    for cousin4 in sorted(temp_cM_dict, key=temp_cM_dict.get, reverse=True):
        punter += 1

 #       for cousin3 in kit1_keystring_list:  # step though all the cousins and match on the shared match group
        places_string = ""
        if cousin4 in surnames:
            list_of_places = surnames[cousin4]
            if len(list_of_places) > 0:
                for place in list_of_places:
                    places_string = places_string + " " + place


        kit1_index = kit1_key_dict[cousin4]
        kit1_cM = Test_Result_Dict[0][cousin4].centimorgans
        if int(kit1_cM) == centimorgan or centimorgan == 0:
          print('{0:6} {1:40} {2:3}cM {3:60}'.format(kit1_index, cousin4, kit1_cM, places_string))

    if surname_found:
        Surnames2 = {}
        EmptySet = set()
        for key in temp_surnames:
            NewSet = set(temp_surnames[key])
            EmptySet = EmptySet.union(NewSet)
        #    print(EmptySet)
        for match_surname in EmptySet:
            Surnames2[match_surname] = []
            for matchkey in temp_surnames:
                if match_surname in temp_surnames[matchkey]:
                    Surnames2[match_surname].append(matchkey)

        # for surname in Surnames2:
        for surname in sorted(Surnames2):
            if len(Surnames2[surname]) > 1:
                print(surname, Surnames2[surname])

    return True

def main():
    person = "Wayne"
    #file_path = "c:/Users/Wayne/DNA/"
    file_path = "//wsl$/Ubuntu-20.04/home/waynew/git_environment/ANCESTRY-DNA-Helper/DNA/"

    if len(sys.argv) > 1:
      if sys.argv[1] == "ubuntu":
       # file_path = '/mnt/c/Users/Wayne/DNA/'
        file_path = './DNA/'
      elif sys.argv[1] == "aws":
        file_path = "/home/ec2-user/DNA/"
      else:
         #file_path = "c:/Users/Wayne/DNA/"
        file_path = "./DNA/"
    if len(sys.argv) == 3:
        person = sys.argv[2]
    duplicate_check_flag = False


    kit1_file_list, kit2_file_list, kit3_file_list, kit4_file_list, kit5_file_list, kit6_file_list, match_filter_list = load_profile(
        person)


    punters_list = [kit2_file_list[0], kit3_file_list[0], kit4_file_list[0], kit5_file_list[0],kit6_file_list[0]]

    kit1_Test_Result_Dict = load_matches(kit1_file_list, 1, duplicate_check_flag, file_path)
    kit1_key_dict = {}
    kit1_who_dict = {}
    kit1_index_dict = {}
    kit1_index_keystring_dict = {}
    kit1_cM_dict = {}
    kit1_primary_index = {}
    kit1_keystring_list = []
    kit1_who_to_index_dict = {}
    kit1_index_to_cM_dict = {}
    for kit1_Test_Result in kit1_Test_Result_Dict:
        kit1_keystring_list.append(kit1_Test_Result_Dict[kit1_Test_Result].keystring)
    for kit1_Test_Result in kit1_Test_Result_Dict:
        kit1_index_dict[kit1_Test_Result_Dict[kit1_Test_Result].index] = kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_who_to_index_dict[kit1_Test_Result_Dict[kit1_Test_Result].who] = kit1_Test_Result_Dict[kit1_Test_Result].index
        kit1_who_dict[kit1_Test_Result_Dict[kit1_Test_Result].who] = kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_index_keystring_dict[kit1_Test_Result_Dict[kit1_Test_Result].index] = kit1_Test_Result_Dict[kit1_Test_Result].keystring
        kit1_key_dict[kit1_Test_Result_Dict[kit1_Test_Result].keystring] = kit1_Test_Result_Dict[kit1_Test_Result].index
        kit1_cM_dict[kit1_Test_Result_Dict[kit1_Test_Result].keystring] = int(kit1_Test_Result_Dict[kit1_Test_Result].centimorgans)
        kit1_index_to_cM_dict[kit1_Test_Result_Dict[kit1_Test_Result].index] = int(kit1_Test_Result_Dict[kit1_Test_Result].centimorgans)
        kit1_primary_index[str(kit1_Test_Result_Dict[kit1_Test_Result].index) + "." + kit1_Test_Result_Dict[kit1_Test_Result].who] = \
                kit1_Test_Result_Dict[kit1_Test_Result].keystring

#    print(kit1_index_dict)
    list_of_lists, new_list_of_lists = get_shared_matches(person, match_filter_list, file_path)

    even_newer_list_of_lists = swap_in_index(new_list_of_lists, kit1_index_dict)



    kit2_Test_Result_Dict = load_matches(kit2_file_list, 2, duplicate_check_flag, file_path)
    kit2_keystring_list = []
    for kit2_Test_Result in kit2_Test_Result_Dict:
        kit2_keystring_list.append(kit2_Test_Result_Dict[kit2_Test_Result].keystring)
    kit3_Test_Result_Dict = load_matches(kit3_file_list, 4, duplicate_check_flag, file_path)
    kit3_keystring_list = []
    for kit3_Test_Result in kit3_Test_Result_Dict:
        kit3_keystring_list.append(kit3_Test_Result_Dict[kit3_Test_Result].keystring)

    kit4_Test_Result_Dict = load_matches(kit4_file_list, 5, duplicate_check_flag, file_path)
    kit4_keystring_list = []
    for kit4_Test_Result in kit4_Test_Result_Dict:
        kit4_keystring_list.append(kit4_Test_Result_Dict[kit4_Test_Result].keystring)

    kit5_Test_Result_Dict = load_matches(kit5_file_list, 7, duplicate_check_flag, file_path)
    kit5_keystring_list = []
    for kit5_Test_Result in kit5_Test_Result_Dict:
        kit5_keystring_list.append(kit5_Test_Result_Dict[kit5_Test_Result].keystring)

    kit6_Test_Result_Dict = load_matches(kit6_file_list, 8, duplicate_check_flag, file_path)
    kit6_keystring_list = []
    for kit6_Test_Result in kit6_Test_Result_Dict:
        kit6_keystring_list.append(kit6_Test_Result_Dict[kit6_Test_Result].keystring)


    Test_Result_Dict = [kit1_Test_Result_Dict, kit2_Test_Result_Dict, kit3_Test_Result_Dict, kit4_Test_Result_Dict,
                        kit5_Test_Result_Dict, kit6_Test_Result_Dict]


    dict_of_sets = {}
    dict_of_shared_matches = {}
    for cousin_set in even_newer_list_of_lists:
      #  print(cousin_set)  #debug file not saved eg Wayne_A.txt
        try:
            index = cousin_set[0]
            dict_of_sets[index] = set(cousin_set)
            del cousin_set[0]  # dont include key index for shared matches
            dict_of_shared_matches[index] = cousin_set
        except:
            print(person," blank line at end of file ", cousin_set,index)
            exit(1)
    dict_of_places = []
    person_places = person + '_Places'
    dict_of_places = get_places(person_places, file_path, kit1_index_keystring_dict)



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
            if len(list(dict_of_sets[cousin1].intersection(super_set))) == 0:
                super_set = super_set.union(dict_of_sets[cousin1])
                new_dict_of_lists[cousin1] = list(dict_of_sets[cousin1])
                new_cousin_list.append(cousin1)
    banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    print("****************************************************")
    print("****************************************************")
    supertotal = 0
    supergroup = 1
    new_list = []
    new_dict = {}
    mode = 0
    CentiMorgan = 0
    no_of_clusters = 0
    for cousin in new_cousin_list:
            print("****************************************************")
            group_total = len(new_dict_of_lists[cousin])
            if group_total > 1:
                no_of_clusters += 1
            print(supergroup, banner_string,  cousin, group_total,  banner_string, CentiMorgan)
            print_cluster(supergroup, cousin, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                          dict_of_places, dict_of_shared_matches, kit1_key_dict, kit2_keystring_list,
                          kit3_keystring_list,
                          kit4_keystring_list, kit5_keystring_list, kit6_keystring_list, punters_list,
                          Test_Result_Dict,mode, CentiMorgan)

            new_list.append(supergroup)
            new_dict[supergroup] = cousin

            supergroup += 1
            supertotal = supertotal + group_total
    print("************************************************************************************************")
    print("supertotal is ", supertotal, "no of cluster is", no_of_clusters)

    Surnames = load_surnames(file_path,"Surnames")
    CityTownVillage = load_surnames(file_path,"Places")
    print(new_list)
    go_again = 'y'
    toggle = False   # start in surnames mode
    mode = 1  # info mode
    cluster_no = 1
    cluster_king = new_dict[1]
    mode_list = [" default", "info", "Surnames", " keystring", " Places"]
    while go_again != 'n':
        while True:
            cluster_search = input(person + mode_list[mode] + " : Enter cluster number or q for quit: ")
            if cluster_search == 'q':
              go_again = 'n'
              break
            elif cluster_search == 'i':  #  info mode
              mode = 1  # Info mode
              group_total = len(new_dict_of_lists[cluster_king])
              print(cluster_no, banner_string, cluster_king, group_total, banner_string, CentiMorgan)
              print_cluster(cluster_no, cluster_king, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                            dict_of_places, dict_of_shared_matches, kit1_key_dict, kit2_keystring_list,
                            kit3_keystring_list, kit4_keystring_list, kit5_keystring_list, kit6_keystring_list,
                            punters_list,
                            Test_Result_Dict, mode, CentiMorgan)
            elif cluster_search == 's':  #  surnames mode
              mode = 2  # Surnames mode
              group_total = len(new_dict_of_lists[cluster_king])
              print(cluster_no, banner_string, cluster_king, group_total, banner_string)
              print_cluster2(cluster_king, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                             Surnames, kit1_key_dict,
                             Test_Result_Dict, CentiMorgan)
            elif cluster_search == 'k':  # key search mode
              mode = 3  # Keys mode
            elif cluster_search == 'p':  # places mode
              mode = 4  # Places mode
              group_total = len(new_dict_of_lists[cluster_king])
              print(cluster_no, banner_string, cluster_king, group_total, banner_string)
              print_cluster2(cluster_king, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                             CityTownVillage, kit1_key_dict,
                             Test_Result_Dict, CentiMorgan)
            elif cluster_search[0:2] == 'cM' and len(cluster_search) > 2:  # change cM filter
              cM_string = cluster_search[2:]
              if cM_string.isdigit():
                  CentiMorgan = int(cM_string)
              else:
                  print("try again")
                  CentiMorgan = 0
            if cluster_search.isdigit():
              cluster_no = int(cluster_search)
              cluster_king = new_dict[cluster_no]
              if (int(cluster_search) in new_list) and (mode == 2):  # Surnames mode
                group_total = len(new_dict_of_lists[cluster_king])
                print( cluster_search, banner_string, cluster_king, banner_string)
                print_cluster2(cluster_king, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                                Surnames, kit1_key_dict, Test_Result_Dict, CentiMorgan)
              elif int(cluster_search) in new_list and mode == 4:     # places mode
                group_total = len(new_dict_of_lists[cluster_king])
                print(cluster_no,  banner_string, cluster_king, group_total, banner_string)
                print_cluster2(cluster_king, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                                 CityTownVillage, kit1_key_dict,
                                 Test_Result_Dict, CentiMorgan)
              elif int(cluster_search) in new_list and mode == 1:  # info mode
                group_total = len(new_dict_of_lists[cluster_king])
                print(cluster_search, banner_string, cluster_king, group_total, banner_string, CentiMorgan)
                print_cluster(int(cluster_search),cluster_king, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                                dict_of_places, dict_of_shared_matches, kit1_key_dict, kit2_keystring_list,
                                kit3_keystring_list, kit4_keystring_list, kit5_keystring_list, kit6_keystring_list, punters_list,
                                Test_Result_Dict,mode, CentiMorgan)
            elif cluster_search in kit1_who_to_index_dict and mode == 3:  # keys mode
                found_index = kit1_who_to_index_dict[cluster_search]
                cluster_search_key = kit1_index_keystring_dict[found_index]
                print("keystring = ", cluster_search_key, ", index = ", found_index, ", cM = ", kit1_index_to_cM_dict[found_index] )
                supergroup = 1
                for cousin in new_cousin_list:  # go back and find the original cluster again
                    if cluster_search_key in new_dict_of_lists[cousin]:  # found
                        cluster_king = cousin
                        cluster_no = supergroup
                        group_total = len(new_dict_of_lists[cousin])
                        print(supergroup, banner_string, cousin, group_total, banner_string, kit1_index_keystring_dict[found_index])
                        print_cluster(supergroup, cousin, new_dict_of_lists, kit1_cM_dict, kit1_keystring_list,
                                      dict_of_places, dict_of_shared_matches, kit1_key_dict, kit2_keystring_list,
                                      kit3_keystring_list, kit4_keystring_list, kit5_keystring_list,
                                      kit6_keystring_list, punters_list,
                                      Test_Result_Dict,mode,CentiMorgan)
                        print("keystring = ", cluster_search_key, ", index = ", found_index, ", cM = ",
                              kit1_index_to_cM_dict[found_index])
                        break
                    supergroup += 1


if __name__ == '__main__':
      main()
