
import re
import operator
from Load_Ancestry2 import get_data , get_cousin_dict , load_matches

def swap_in_key_string(old_list, match_filter_list,homonym_to_primarykey_dict,primarykey_to_keystring ):

    new_list = []
    for entry in old_list:
        if entry not in match_filter_list:
            primarykey = homonym_to_primarykey_dict[entry]
            new_entry = primarykey_to_keystring[primarykey]
            new_list.append(new_entry)
    return new_list

def get_shared_match2(kit3, match_filter_list, kit1_primary_index,kit1_index_keystring_dict):
    print(match_filter_list)
    cousin_list = []
    list_of_lists = []
    homonym_to_primarykey_dict = {}
    primarykey_to_keystring = {}
    line_no = 1
    last_cousin = "wally"
    for line in open(kit3 + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        primary_index = orig_word_list[0]  + "." + orig_word_list[1]
        homonym = orig_word_list[1]
        keystring = kit1_index_keystring_dict[int(orig_word_list[0])]   # use the index to get keystring
        this_cousin = kit1_primary_index[primary_index]
        homonym_to_primarykey_dict[homonym] = this_cousin  # will go homonym >> primarykey >> matchstring_245
        primarykey_to_keystring[this_cousin] = keystring
        #print(match_filter_list)
        #print(this_cousin, homonym)
        if (this_cousin != last_cousin) and (homonym not in match_filter_list) :
            if orig_word_list[1] in cousin_list:
                print("ouch", orig_word_list[1])
            else:
                del orig_word_list[0]  # the index number
                list_of_lists.append(orig_word_list)
                cousin_list.append(orig_word_list[0])
                last_cousin = this_cousin
        elif (this_cousin == last_cousin) and (homonym not in match_filter_list):
            del orig_word_list[0]  # dont add  cousin name again
            del orig_word_list[0]
            list_of_lists[-1].extend(orig_word_list)
        line_no += 1

    dict_of_sets = {}
    dict_of_shared_matches = {}
    for cousin_set in list_of_lists:
        cousin_set = swap_in_key_string(cousin_set, match_filter_list,homonym_to_primarykey_dict,primarykey_to_keystring )
        index = cousin_set[0]
        dict_of_sets[index] = set(cousin_set)
        del cousin_set[0]  # dont include key index for shared matches
        dict_of_shared_matches[index] = cousin_set
    return dict_of_sets, dict_of_shared_matches

def get_common_ancestor(kit6, kit1_index_keystring_dict):
    cousin_list = []
    new_dict = {}
    for line in open(kit6 + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        this_cousin = orig_word_list[1]
        key_string = kit1_index_keystring_dict[int(orig_word_list[0])]
        #print(orig_word_list[0], orig_word_list[1], key_string)
        new_dict[key_string] = orig_word_list[2]
        #cousin_list.append(key_string)
    return new_dict

def get_places(kit3_places, kit1_who_dict):
    dict_of_places = {}
    line_no = 1
    for line in open(kit3_places + '.txt'):
        line = line.rstrip()
        orig_word_list = line.split()
        this_cousin = kit1_who_dict[orig_word_list[1]]
        del orig_word_list[0]  # the index number
        del orig_word_list[0]  # cousin
        dict_of_places[this_cousin] = orig_word_list
        line_no += 1

    return dict_of_places


def main():
    person = "Glyn"
    print_filter = True
    match_filter_list = [""]
    match_filter_list2 = [""]
    #match_filter_list = ["aberlas", "SallyAnneGale", "H.H.ManagedbyReesDinbych","gethngethn", \
    #                     "ArthurMarkGaleManagedbySteamerpoint", "BarbaraParryManagedbyGwendaParfitt", "D.W.ManagedbyWendyMcKenna",\
    #                     "G.R.Managedbygemmaroberts50", "ElizabethPritchard", "sheree8","ajones296","AlwenaJames"]
    #match_filter_list = ["SimonGray", "JudithBuckle" ,"MalcolmSlade", "EricEngelhard"]


    if person == "Glyn":
        kit1_file_list = ["Glyn"]  # , "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM", "Dad_B"]
        kit2_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM", "Wayne_8cM", "Wayne_7cM", "Wayne_6cM", "Wayne_A"]
        match_filter_list = ["EricEngelhard"]
        kit3 = 'Top60_Dad_X_Bee_Bridle'
        kit3_places = 'places_in_trees'
        kit6 = 'Glyn_Common2'
    elif person == "Wayne":
        kit2_file_list = ["Glyn" , "Dad_9cM", "Dad_8cM", "Dad_7cM","Dad_6cM", "Dad_B"]
        kit1_file_list = ["Wayne"]
        match_filter_list = ["SandraDavis","DavidLarsen","PaulineWilliams","LindaEvans","sheilaroberts","susanwhiskin","BarbaraParryManagedbyGwendaParfitt"]
        #match_filter_list = ["SandraDavis","DavidLarsen","PaulineWilliams","LindaEvans","sheilaroberts","susanwhiskin"]
        match_filter_list2 = ["nogoodboyoManagedbyRhiannonWilliams"]
        match_filter_list.extend(match_filter_list2)
        kit3 = 'Top60_ag3754'
        kit3_places = 'Top60_ag3754'
        kit6 = 'Wayne_Common'

    kit4_file_list = ["Helen", "Helen_B"]
    kit5_file_list = ["Sally", "Sally_10cM", "Sally_9cM","Sally_8cM", "Sally_7cM", "Sally_6cM", "Sally_6cM_A", "Sally_L" ]
    duplicate_check_flag = False
    dict_of_places = []


    kit1_dict_of_lists = load_matches(kit1_file_list, duplicate_check_flag)
    kit1_list = []
    kit1_key_dict = {}
    kit1_who_dict = {}
    kit1_index_dict = {}
    kit1_index_keystring_dict = {}
    kit1_cM_dict = {}
    kit1_primary_index = {}
    for cousin in kit1_dict_of_lists:
        #print(cousin)
        kit1_list.append(kit1_dict_of_lists[int(cousin)]["key_string"])
        kit1_who_dict[kit1_dict_of_lists[int(cousin)]["who"]] = kit1_dict_of_lists[int(cousin)]["key_string"]
        kit1_index_dict[kit1_dict_of_lists[int(cousin)]["key_string"]] = kit1_dict_of_lists[int(cousin)]["index"]
        kit1_index_keystring_dict[kit1_dict_of_lists[int(cousin)]["index"]] = kit1_dict_of_lists[int(cousin)]["key_string"]
        kit1_cM_dict[kit1_dict_of_lists[int(cousin)]["key_string"]] = int(kit1_dict_of_lists[int(cousin)]["cM"])
        kit1_primary_index[str(kit1_dict_of_lists[int(cousin)]["index"]) + "." + kit1_dict_of_lists[int(cousin)]["who"]] = \
            kit1_dict_of_lists[int(cousin)]["key_string"]

    common_dict = get_common_ancestor(kit6, kit1_index_keystring_dict)

    dict_of_sets, dict_of_shared_matches = get_shared_match2(kit3, match_filter_list, kit1_primary_index, kit1_index_keystring_dict)
    dict_of_places = get_places(kit3_places, kit1_who_dict)



    kit2_dict_of_lists = load_matches(kit2_file_list, duplicate_check_flag)
    kit2_list = []
    kit2_index_dict = {}
    for cousin in kit2_dict_of_lists:
        kit2_index_dict[kit2_dict_of_lists[int(cousin)]["key_string"]] = kit2_dict_of_lists[int(cousin)]["index"]
        kit2_list.append(kit2_dict_of_lists[int(cousin)]["key_string"])



    kit4_dict_of_lists = load_matches(kit4_file_list, duplicate_check_flag)
    kit4_list = []
    kit4_index_dict = {}
    for cousin in kit4_dict_of_lists:
        #print (cousin)
        kit4_index_dict[kit4_dict_of_lists[int(cousin)]["key_string"]] = kit4_dict_of_lists[int(cousin)]["index"]
        kit4_list.append(kit4_dict_of_lists[int(cousin)]["key_string"])



    kit5_dict_of_lists = load_matches(kit5_file_list, duplicate_check_flag)
    kit5_list = []
    kit5_index_dict = {}
    for cousin in kit5_dict_of_lists:
        kit5_index_dict[kit5_dict_of_lists[int(cousin)]["key_string"]] = kit5_dict_of_lists[int(cousin)]["index"]
        kit5_list.append(kit5_dict_of_lists[int(cousin)]["key_string"])




    print("***********************Combing now*****************************")
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
    dad_string = "help"
    chromo_dict = {}
    for cousin in new_cousin_list:
            punter = 0
            print("****************************************************")
            group_total = len(new_dict_of_lists[cousin])
            #print(supergroup, cousin ,group_total,new_dict_of_lists[cousin] )
            dad_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
            print(supergroup, dad_string,  cousin, group_total,  dad_string)
            new_index = 1
            temp_dict = {}
            #kit1_supergroup[cousin] = ""

            for cousin4 in new_dict_of_lists[cousin]:
                temp_dict[cousin4] = kit1_cM_dict[cousin4]

            #for cousin4 in sorted(temp_dict, key=temp_dict.get):
            for cousin4 in sorted(temp_dict, key=temp_dict.get, reverse=True):
                    cousin4_index = kit1_index_dict[cousin4]
                    punter += 1
                    for cousin3 in kit1_list:  # step though all the cousins and match on the shared match group
                        match_kit2 = ""
                        match_kit4 = ""
                        match_kit5 = ""
                        common_string = ""
                        places_string = ""
                        place_list = []
                        filter_flag = False
                        if cousin3 in common_dict:
                            common_string = common_dict[cousin3]
                        if cousin3 in dict_of_places:
                            list_of_places = dict_of_places[cousin3]
                            if len(list_of_places) > 0:
                                for place in list_of_places:
                                   places_string = places_string + " " + place

                        trail_string = ""
                        no_of_shared_matches = 0
                        if cousin3 == cousin4:
                            if "GEDMATCH" in kit1_dict_of_lists[kit1_index_dict[cousin4]]:
                                trail_string = trail_string + "GEDMATCH " + kit1_dict_of_lists[kit1_index_dict[cousin4]]["GEDMATCH"]
                            if "CHROMOSOMES" in kit1_dict_of_lists[kit1_index_dict[cousin4]]:
                                kit1_supergroup[cousin3] = supergroup
                                trail_string = trail_string + " chr " + kit1_dict_of_lists[kit1_index_dict[cousin4]]["CHROMOSOMES"]
                                #chromo_dict[cousin3] = kit1_dict_of_lists[kit1_index_dict[cousin4]]["CHROMOSOMES"]
                                chromo_string = kit1_dict_of_lists[kit1_index_dict[cousin4]]["CHROMOSOMES"]
                                chromo_string_1 = kit1_dict_of_lists[kit1_index_dict[cousin4]]["CHROMOSOMES"]
                                chromo_string = chromo_string.replace('(', ' ')
                                chromo_string = chromo_string.replace(')', ' ')
                                chromo_string = chromo_string.replace('-', ' ')
                                chromo_list = chromo_string.split()
                                chromo_dict[cousin3] = chromo_list
                            if cousin3 in dict_of_shared_matches:
                                no_of_shared_matches =    len(dict_of_shared_matches[cousin4])


                            if cousin3 in kit2_list:
                                match_kit2 = kit2_file_list[0] + "=" + kit2_dict_of_lists[kit2_index_dict[cousin4]]["cM"] + "cM"
                            if cousin3 in kit4_list:
                                match_kit4 = kit4_file_list[0] + "=" + kit4_dict_of_lists[kit4_index_dict[cousin4]]["cM"] + "cM"
                            if cousin3 in kit5_list:
                                match_kit5 = kit5_file_list[0] + "=" + kit5_dict_of_lists[kit5_index_dict[cousin4]]["cM"] + "cM"
                            kit1_index = kit1_index_dict[cousin4]
                            kit1_cM = kit1_dict_of_lists[kit1_index]["cM"]
                            kit1_seg = kit1_dict_of_lists[kit1_index]["segments"]
                            #print( kit1_index, kit1_cM + "cM", kit1_seg + " seg",cousin4, "*" + str(no_of_shared_matches) + "*",match_kit2, match_kit4 , match_kit5, trail_string)
                            print_flag = True
                            if print_flag:
                              print('{0:40} {1:3}cM {2:2}seg   {3:11} {4:11} {5:11}    {6:4} *{7:1}* {8:30}' \
                                  .format( cousin4, kit1_cM, kit1_seg,
                                          match_kit2, match_kit4, match_kit5, kit1_index, str(no_of_shared_matches), common_string))
                            else:
                               print('{0:4} {1:40} {2:3}cM {3:2}seg {4:30}' \
                                  .format( kit1_index, cousin4, kit1_cM, kit1_seg,
                                          places_string))

            supergroup += 1
            supertotal = supertotal + group_total
    print("************************************************************************************************")
    print("supertotal is ", supertotal)
    print("****************************************************")
    cousin_string = ""
    match_kit2 = kit2_file_list[0]
    match_kit4 = ""
    match_kit5 = ""

    for chromosome in range(1,23):
      chromosome_string = str(chromosome)
      print("chromosome = >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   "  + chromosome_string)
      for cousin_chromo in chromo_dict:  # chrom_dict is keyed by cousin keystring
          if chromosome_string in chromo_dict[cousin_chromo]:
              cousin_string = ""
              trail_string = ""
              if "GEDMATCH" in kit1_dict_of_lists[kit1_index_dict[cousin_chromo]]:
                  trail_string = trail_string + "GEDMATCH " + kit1_dict_of_lists[kit1_index_dict[cousin_chromo]]["GEDMATCH"]
              #if cousin_chromo in common_dict:
              #    trail_string = common_dict[cousin_chromo]
              if cousin_chromo in kit2_list:
                  cousin_string = kit2_file_list[0]
              if cousin_chromo in kit4_list:
                  cousin_string = cousin_string + " " + kit4_file_list[0]
              if cousin_chromo in kit5_list:
                  cousin_string = cousin_string + " " + kit5_file_list[0]
              if chromosome_string in chromo_dict[cousin_chromo]:
                  print('{0:50} {1:20} {2:20} {3:3}'.format(cousin_chromo, cousin_string, trail_string, kit1_supergroup[cousin_chromo]))

#    for cousin3 in sorted(kit1_cM_dict, key=kit1_cM_dict.get, reverse=True):
#         print(cousin3, kit1_cM_dict[cousin3]  )
              #cousin_string = ""
   # print(len(new_cousin_list), new_cousin_list)
#    for cuz in common_list:
#        print(cuz)
#print('{0:6} {1:3} {2:10} {3:35} {4:16} {5:7} {6:11} {7:20}' \
#      .format(self.title, self.month[0:3], self.ad_date, description, self.colour, \
#              self.price, self.phone1, self.suburb))



if __name__ == '__main__':
      main()
