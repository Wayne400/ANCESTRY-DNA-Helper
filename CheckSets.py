
import re
import sys
import operator




def swap_in_index(list_of_lists,homonym_to_primarykey_dict,kit1_index_keystring_dict):

    new_list_of_lists = []
    for list in list_of_lists:
        new_list = []
        # print(list)
        for homonym in list:
            try:
                primary_key = homonym_to_primarykey_dict[homonym]
                new_list.append(primary_key)
            except:
                print("duplicate key = ", homonym, primary_key)
                print(list)
                exit(1)

        new_list_of_lists.append(new_list)
    return new_list_of_lists


def get_shared_indices(shared_file_path):
    homonym_to_primarykey_dict = {}
    check_all_entry_list = []  # check to find all shared matches are indexed too
    primary_entry_list = []

    for line in open(shared_file_path):  # first parse , only gets keys
        line = line.rstrip()
        orig_word_list = line.split()
     #   print(orig_word_list)  # debug only
        homonym_to_primarykey_dict[orig_word_list[1]] = int(orig_word_list[0])  # will overwrite additional lines
        del orig_word_list[0]
        check_all_entry_list.extend(orig_word_list)
        primary_entry_list.append(orig_word_list[0])
    for entry in check_all_entry_list:
        if entry not in primary_entry_list:
            print(entry, " index is missing in file " + shared_file_path)
            exit(1)
    return homonym_to_primarykey_dict

def get_shared_dict(shared_file_path):
    shared_list_dict = {}
    index_list_dict = {}
    last_cousin = "wally"

    key_to_numeric_dict = {}
    for line in open(shared_file_path):  # first parse , only gets keys
        line = line.rstrip()
        orig_word_list = line.split()
        key_to_numeric_dict[orig_word_list[1]] = int(orig_word_list[0])  # will overwrite additional lines

    for line in open(shared_file_path):
        line = line.rstrip()
        orig_word_list = line.split()
        numeric_index = orig_word_list[0]
        this_cousin = orig_word_list[1]
        del orig_word_list[0]  # remove numerical index
        del orig_word_list[0]  # remove string index but saved above
    
        if (this_cousin != last_cousin):
                new_list = []
                new_list.extend(orig_word_list)
                last_cousin = this_cousin
        elif (this_cousin == last_cousin):
                new_list.extend(orig_word_list)
        shared_list_dict[this_cousin] = new_list  # keep overwriting until this cousin changes
        numeric_list=[]
        for string_index in new_list:
            numeric_list.append(key_to_numeric_dict[string_index])
        index_list_dict[numeric_index] = numeric_list  # ditto
    #print("get shared dict", key_to_numeric_dict)
    return shared_list_dict, index_list_dict, key_to_numeric_dict


  # get_shared_matches(person, match_filter_list, file_path, kit1_index_keystring_dict)
def get_shared_matches(shared_file_path):

    this_cousin = "wally"
    last_cousin = "wally"
    homonym_to_primarykey_dict = get_shared_indices(shared_file_path)
    shared_list_dict, index_list_dict, key_to_numeric_dict = get_shared_dict(shared_file_path)
    for line in open(shared_file_path):
        line = line.rstrip()
        orig_word_list = line.split()
        this_cousin = orig_word_list[1]
        cousin_primary_index =  orig_word_list[0]
        del orig_word_list[0]  # remove index
        #if this_cousin not in match_filter_list:
        if (this_cousin != last_cousin) :
              #  del orig_word_list[0]  # the index number
                last_cousin = this_cousin
        elif (this_cousin == last_cousin):
               # del orig_word_list[0]  # dont add  cousin name again
                del orig_word_list[0]
# made a change was calling in for loop above

    #print("get shared matches", key_to_numeric_dict )
    return  shared_list_dict, index_list_dict , key_to_numeric_dict

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
    person = "Glyn"
    file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/DNA/"

    if len(sys.argv) > 1:
        person = sys.argv[1]
    shared_file_path = file_path + person + "_Shared.txt"
    shared_list_dict, index_list_dict, key_to_numeric_dict = get_shared_matches( shared_file_path)
    print(shared_list_dict)

    go_again = 'y'
    toggle = False   # start in surnames mode
    mode = 1  # info mode
    input_2 = 0
    set_1_id = 'freddy'
    set_1 = set()
    set_2_id = 'willy'
    set_2 = ()
    mode_list = [" default", "info", "Surnames", " keystring", " Places"]
    while input_2 < 2:
        cluster_search = input(person + mode_list[mode] + " : Enter cluster number or q for quit: ")
        if cluster_search in shared_list_dict:
         #  print(shared_list_dict[cluster_search])
           if input_2 == 0:
               set_1 = set(shared_list_dict[cluster_search])
               set_1_id = cluster_search
           if input_2 == 1:
               set_2 = set(shared_list_dict[cluster_search])
               set_2_id = cluster_search
           input_2 += 1
    print(set_1_id,len(set_1),set_2_id,len(set_2))
 #   print(list(set_1.intersection(set_2)))
    print(set_1_id,set_2_id,list(set_1.difference(set_2)))
    print(set_2_id,set_1_id,list(set_2.difference(set_1)))

if __name__ == '__main__':
      main()
