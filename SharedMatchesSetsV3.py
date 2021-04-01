
import re
import operator


class DNA_Result(object):

    def __init__(self, index=99999, offset = 0, who="", centimorgans=0, segments=0, people="", keystring="", tree="", kit_duplicate_check="", kit="wally", kit_number = 99, gedmatch = "", chromosomes=""):


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
        self.gedmatch = gedmatch
        self.chromosomes = chromosomes



def get_data(word_list,index_offset):
    new_word_dict = {}
    new_word_dict["People"] = "zero"
    new_word_dict["Tree"] = ""
    new_word_dict["GEDMATCH"] = ""
    new_word_dict["CHROMOSOMES"] = ""
    i = 0
    new_index = 9999999

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

    return new_word_dict



def load_matches(file_list, kit_number ):
    kit_offset_index = 0
    Test_Result_Dict = {}
    cousin_key_list = []
    dna_list = []
    dna_list_index = []

    for text_file in file_list:
        kit_person = file_list[0]
        #print (text_file, 10000* kit_offset_index)
        print("loading ", text_file)
#        get_cousin_dict(text_file, kit_number, kit_offset_index * 20000,
#                                              dna_list,  dna_list_index, cousin_key_list, Test_Result_Dict )

        dict_of_lists = {}
        old_index = 9999999999
        line_no = 1
        for line in open(text_file + '.txt', encoding='latin-1'):
            line = line.rstrip()
            line = line.replace('\t', ' ')
            line = line.replace(',', '')
            word_list = line.split()
            #        search_duplicate_string = ""
            new_word_dict = get_data(word_list, kit_offset_index * 20000)
#            test_result = "wally"
            test_result = DNA_Result(int(line_no), kit_offset_index * 20000, new_word_dict["who"], new_word_dict["cM"],
                                     new_word_dict["segments"], new_word_dict["People"], new_word_dict["key_string"],
                                     new_word_dict["Tree"], text_file, kit_number,
                                     new_word_dict["GEDMATCH"], new_word_dict["CHROMOSOMES"])

#            dict_of_lists[int(line_no) + int(kit_offset_index * 20000)] = new_word_dict
#            dna_list.append(test_result)

            #        total_dna_list.append(test_result)
            keystring = new_word_dict["key_string"]
#            if keystring not in cousin_key_list:
#                cousin_key_list.append(keystring)
            Test_Result_Dict[keystring] = test_result
                # print(keystring)

#            dna_list_index.append(line_no + kit_offset_index * 20000)
            line_no = line_no + 1

        # def get_cousin_dict(kit, kit_number, index_offset, dna_list, dna_list_index, cousin_key_list):

        kit_offset_index += 1

    return Test_Result_Dict



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
        if orig_word_list[1] not in match_filter_list:
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
    print_filter = False
    places_flag = False
    match_filter_list = [""]
    match_filter_list2 = [""]
    total_dna_list = []

    if person == "Glyn":
        kit1_file_list = ["Glyn"]  # , "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM", "Dad_B"]

        match_filter_list = ["aberlas", "UJonesManagedbySteamerpoint", "SallyAnneGale", "H.H.ManagedbyReesDinbych","gethngethn", \
                             "ArthurMarkGaleManagedbySteamerpoint", "BarbaraParryManagedbyGwendaParfitt", "D.W.ManagedbyWendyMcKenna",\
                              "ElizabethPritchard", "sheree8","AlwenaJames", "LJ"]

        match_filter_list2 = ["EricEngelhard", "NatalieRoberts_53%", "StevenRoberts", "nora_engelhard","JudithBuckle",
                              "patsobocienski","SimonGray"]

        match_filter_list3 = ["G.R.Managedbygemmaroberts50","H.D.Managedbyprenjo","usersam2772",\
                              "IforGlynLloyd","E.G.ManagedbyKarenBracegirdle","JudyJones",\
                              "HenryRobertsManagedbyHollyMonday-Jones", "StevenRoberts_80%"]


        match_filter_list4 = ["ElizabethPritchard",
                               "AdelynEllis" , "CliffordDaviesManagedbyAnnDavies",
                              "DewiPugh", "ElwynDavies",  "GlynParry", "ElenLewis",
                              "gwendahumphries", "InaBlancheParry"]

        match_filter_list5 = ["JaredDeWittie"]

        match_filter_list6 = [ "PaulDay", "LKevinKelly11", "tchester200166", "ADavis0214",
                              "ErinWilson", "ColleenOLeary","AnnStoddard", "RebeccaBailey","arwelwjones51",
                               "JuneMcLachlinManagedbyoschean"]
        match_filter_list7 = ["GillianandGlynEvans", "D.H.ManagedbySEANALLEN"]

        match_filter_list8 = ["stevemcgarry189", "RayRutland65", "slbrooks311"]


        match_filter_list.extend(match_filter_list2)
        match_filter_list.extend(match_filter_list3)
        match_filter_list.extend(match_filter_list4)
        match_filter_list.extend(match_filter_list5)
        match_filter_list.extend(match_filter_list6)
        match_filter_list.extend(match_filter_list7)
        match_filter_list.extend(match_filter_list8)

        kit3 = 'Top60_Dad_X_Bee_Bridle'
        kit3_places = 'places_in_trees'
        kit2_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM", "Wayne_8cM", "Wayne_7cM", "Wayne_6cM_new", "Wayne_A"]
#        kit2_file_list = ["Wayne", "Wayne_10cM"]

        kit4_file_list = ["Helen", "Helen_B"]
        kit5_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM", "Sally_L"]
 #       kit5_file_list = ["Sally", "Sally_10cM"]

        kit6 = 'Glyn_Common2'
        kit7_file_list = ["Una", "Una_11cM", "Una_10cM", "Una_9cM", "Una_8cM", "Una_7cM", "Una_6cM", "Una_L" ]
#        kit7_file_list = ["Una", "Una_11cM"]

        kit8_file_list = ["Gary", "Gary_14cM", "Gary_13cM", "Gary_12cM", "Gary_11cM", "Gary_10cM", "Gary_9cM", "Gary_8cM", "Gary_A"]
#        kit8_file_list = ["Gary", "Gary_14cM"]

    if person == "Wayne":
        kit1_file_list = ["Wayne"]
        match_filter_list = ["SandraDavis","DavidLarsen","PaulineWilliams","LindaEvans","sheilaroberts","susanwhiskin","BarbaraParryManagedbyGwendaParfitt"]
        #match_filter_list = ["SandraDavis","DavidLarsen","PaulineWilliams","LindaEvans","sheilaroberts","susanwhiskin"]
        match_filter_list2 = ["nogoodboyoManagedbyRhiannonWilliams"]
        match_filter_list.extend(match_filter_list2)
        kit3 = 'Top60_ag3754'
        kit3_places = 'Top60_ag3754'
        kit2_file_list = ["Glyn" , "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM", "Dad_B"]
        kit4_file_list = ["Helen", "Helen_B"]
        kit5_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM", "Sally_L"]
        kit6 = 'Wayne_Common'
        kit7_file_list = ["Una", "Una_11cM", "Una_10cM", "Una_9cM", "Una_8cM", "Una_7cM", "Una_6cM", "Una_L"]
        kit8_file_list = ["Gary", "Gary_14cM", "Gary_13cM", "Gary_12cM", "Gary_11cM", "Gary_10cM", "Gary_9cM", "Gary_8cM", "Gary_A"]
    if person == "Sally":
        kit1_file_list = ["Sally" ]
        match_filter_list = ["UJonesManagedbySteamerpoint", "RobertFort", "LaurenRoberts", "DavidRobertsManagedbyLaurenRoberts","WynneOwens"]
        match_filter_list2 = ["JenniferNydahl", "aberlas", "gpb444", "reina155", "uklancsbabe"]
        match_filter_list.extend(match_filter_list2)
        match_filter_list3 = [ "lambbhuna","MyfanwyWilliams-Owen", "AnnaLouiseYoud", "WilliamBarhydt"] # "LeanneHodgeon"
        match_filter_list.extend(match_filter_list3)
        kit3 = 'Sally_Shared'
        kit3_places = 'Sally_Shared'
        kit2_file_list = ["Glyn" , "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM", "Dad_B"]
        kit4_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM", "Wayne_8cM", "Wayne_7cM", "Wayne_6cM_new", "Wayne_A"]
        kit5_file_list = ["Helen", "Helen_B"]
        kit6 = 'Sally_Common'
        kit7_file_list = ["Una", "Una_11cM", "Una_10cM", "Una_9cM", "Una_8cM", "Una_7cM", "Una_6cM", "Una_L"]
        kit8_file_list = ["Gary", "Gary_14cM", "Gary_13cM", "Gary_12cM", "Gary_11cM", "Gary_10cM", "Gary_9cM", "Gary_8cM", "Gary_A"]

    duplicate_check_flag = False
    dict_of_places = []


#    kit1_dict_of_lists = load_matches(kit1_file_list, duplicate_check_flag)
    kit1_Test_Result_Dict = load_matches(kit1_file_list, 1)
    kit1_key_dict = {}
    kit1_who_dict = {}
    kit1_index_dict = {}
    kit1_index_keystring_dict = {}
    kit1_cM_dict = {}
    kit1_primary_index = {}
    kit1_keystring_list = []
    for kit1_Test_Result in kit1_Test_Result_Dict:
        kit1_keystring_list.append(kit1_Test_Result_Dict[kit1_Test_Result].keystring)
    for cousin in kit1_keystring_list:
#        print("cousin", cousin)
#        print( kit1_Test_Result_Dict[cousin].index, cousin)
#        print("keystring", kit1_Test_Result_Dict[cousin].keystring)
        kit1_who_dict[kit1_Test_Result_Dict[cousin].who] = kit1_Test_Result_Dict[cousin].keystring
        kit1_index_dict[kit1_Test_Result_Dict[cousin].keystring] = kit1_Test_Result_Dict[cousin].index
        kit1_index_keystring_dict[kit1_Test_Result_Dict[cousin].index] = kit1_Test_Result_Dict[cousin].keystring
        kit1_cM_dict[kit1_Test_Result_Dict[cousin].keystring] = int(kit1_Test_Result_Dict[cousin].centimorgans)
        kit1_primary_index[str(kit1_Test_Result_Dict[cousin].index) + "." + kit1_Test_Result_Dict[cousin].who] = \
                kit1_Test_Result_Dict[cousin].keystring

    common_dict = get_common_ancestor(kit6, kit1_index_keystring_dict)

#    dict_of_sets, dict_of_shared_matches = get_shared_match2(kit3, match_filter_list, kit1_primary_index, kit1_index_keystring_dict, kit1_Test_Result_Dict)
    dict_of_sets, dict_of_shared_matches = get_shared_match2(kit3, match_filter_list, kit1_primary_index, kit1_index_keystring_dict)

    dict_of_places = get_places(kit3_places, kit1_who_dict)

    kit2_Test_Result_Dict = load_matches(kit2_file_list, 2)
    kit2_keystring_list = []
    for kit2_Test_Result in kit2_Test_Result_Dict:
        kit2_keystring_list.append(kit2_Test_Result_Dict[kit2_Test_Result].keystring)

    kit4_Test_Result_Dict = load_matches(kit4_file_list, 4)
    kit4_keystring_list = []
    for kit4_Test_Result in kit4_Test_Result_Dict:
        kit4_keystring_list.append(kit4_Test_Result_Dict[kit4_Test_Result].keystring)

    kit5_Test_Result_Dict = load_matches(kit5_file_list, 5)
    kit5_keystring_list = []
    for kit5_Test_Result in kit5_Test_Result_Dict:
        kit5_keystring_list.append(kit5_Test_Result_Dict[kit5_Test_Result].keystring)

    kit7_Test_Result_Dict = load_matches(kit7_file_list, 7)
    kit7_keystring_list = []
    for kit7_Test_Result in kit7_Test_Result_Dict:
        kit7_keystring_list.append(kit7_Test_Result_Dict[kit7_Test_Result].keystring)

    kit8_Test_Result_Dict = load_matches(kit8_file_list, 8)
    kit8_keystring_list = []
    for kit8_Test_Result in kit8_Test_Result_Dict:
        kit8_keystring_list.append(kit8_Test_Result_Dict[kit8_Test_Result].keystring)




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
            #print(supergroup, cousin ,group_total,new_dict_of_lists[cousin] )
            banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
            print(supergroup, banner_string,  cousin, group_total,  banner_string)
            new_index = 1
            temp_dict = {}
            #kit1_supergroup[cousin] = ""

            for cousin4 in new_dict_of_lists[cousin]:
                temp_dict[cousin4] = kit1_cM_dict[cousin4]

            #for cousin4 in sorted(temp_dict, key=temp_dict.get):
            for cousin4 in sorted(temp_dict, key=temp_dict.get, reverse=True):
                    cousin4_index = kit1_index_dict[cousin4]
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
#                            if "GEDMATCH" in kit1_dict_of_lists[kit1_index_dict[cousin4]]:
#                               trail_string = trail_string + "GEDMATCH " + kit1_dict_of_lists[kit1_index_dict[cousin4]]["GEDMATCH"]
                            if kit1_Test_Result_Dict[cousin4].gedmatch != "":
                                trail_string = trail_string + "GEDMATCH " + kit1_Test_Result_Dict[cousin4].gedmatch
                            if kit1_Test_Result_Dict[cousin4].chromosomes != "":
#                            if "CHROMOSOMES" in kit1_dict_of_lists[kit1_index_dict[cousin4]]:
                                kit1_supergroup[cousin3] = supergroup
                                chromo_string = kit1_Test_Result_Dict[cousin4].chromosomes
                                chromo_string = chromo_string.replace('(', ' ')
                                chromo_string = chromo_string.replace(')', ' ')
                                chromo_string = chromo_string.replace('-', ' ')
                                chromo_list = chromo_string.split()
                                chromo_dict[cousin3] = chromo_list
                            if cousin3 in dict_of_shared_matches:
                                no_of_shared_matches =    len(dict_of_shared_matches[cousin4])


                            if cousin3 in kit2_keystring_list:
                                match_kit2 = kit2_file_list[0] + "=" + kit2_Test_Result_Dict[cousin4].centimorgans  + "cM"
                            if cousin3 in kit4_keystring_list:
                                match_kit4 = kit4_file_list[0] + "=" + kit4_Test_Result_Dict[cousin4].centimorgans  + "cM"

                            if cousin3 in kit5_keystring_list:
                                match_kit5 = kit5_file_list[0] + "=" + kit5_Test_Result_Dict[cousin4].centimorgans  + "cM"

                            if cousin3 in kit7_keystring_list:
                                match_kit7 = kit7_file_list[0] + "=" + kit7_Test_Result_Dict[cousin4].centimorgans  + "cM"

                            if cousin3 in kit8_keystring_list:
                                match_kit8 = kit8_file_list[0] + "=" + kit8_Test_Result_Dict[cousin4].centimorgans  + "cM"


                            kit1_index = kit1_index_dict[cousin4]
#                            kit1_cM = kit1_dict_of_lists[kit1_index]["cM"]
                            kit1_cM = kit1_Test_Result_Dict[cousin4].centimorgans
                            kit1_seg = kit1_Test_Result_Dict[cousin4].segments
#                            kit1_seg = kit1_dict_of_lists[kit1_index]["segments"]
                            #print( kit1_index, kit1_cM + "cM", kit1_seg + " seg",cousin4, "*" + str(no_of_shared_matches) + "*",match_kit2, match_kit4 , match_kit5, trail_string)
                            if not places_flag:
                              print('{0:40} {1:3}cM {2:2}seg   {3:11} {4:11} {5:11} {6:11} {7:11}  {8:4} *{9:1}* {10:30}' \
                                  .format( cousin4, kit1_cM, kit1_seg,
                                          match_kit2, match_kit4, match_kit5, match_kit7, match_kit8, kit1_index, str(no_of_shared_matches), common_string))
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
              if kit1_Test_Result_Dict[cousin_chromo].gedmatch != "":
                  trail_string = trail_string + "GEDMATCH " + kit1_Test_Result_Dict[cousin_chromo].gedmatch
#              if "GEDMATCH" in kit1_dict_of_lists[kit1_index_dict[cousin_chromo]]:
#                  trail_string = trail_string + "GEDMATCH " + kit1_dict_of_lists[kit1_index_dict[cousin_chromo]]["GEDMATCH"]
              #if cousin_chromo in common_dict:
              #    trail_string = common_dict[cousin_chromo]
              if cousin_chromo in kit2_keystring_list:
                  cousin_string = kit2_file_list[0]
              if cousin_chromo in kit4_keystring_list:
                  cousin_string = cousin_string + " " + kit4_file_list[0]
              if cousin_chromo in kit5_keystring_list:
                  cousin_string = cousin_string + " " + kit5_file_list[0]
              if cousin_chromo in kit7_keystring_list:
                  cousin_string = cousin_string + " " + kit7_file_list[0]
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
