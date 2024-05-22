
import re

class DNA_Result(object):

    def __init__(self, index=99999, who='wally', centimorgans=2, sharedDNA=".11%", segments=999, cousin="6th Cousin", surnames="Empty" ):

        self.index = index
        self.who = who
        self.centimorgans = centimorgans
        self.sharedDNA = sharedDNA
        self.segments = segments
        self.cousin = cousin
        self.surnames = surnames

    def add_surnames(self, surname_string):
        self.surnames = surname_string


def filter_list(list_to_filter, index_match_filter_list):

    new_filtered_list = []
    for entry in list_to_filter:
        if entry not in index_match_filter_list:
            new_filtered_list.append(entry)
    return new_filtered_list

def get_cousin_dict(kit1):

    file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/23andMe/"
    list_of_dna = []
    dict_of_dna = {}
    kit1_who_to_index_dict = {}
    line_no = 1
    for line in open(file_path + kit1 + '.txt', encoding='latin-1'):
        line = line.rstrip()
        word_list = line.split(',')
        first_column = word_list[0].rstrip()
        first_column_list = first_column.split(' ')
        index = first_column_list[0]
        who = first_column.strip(index + ' ')
        who=who.replace(" ", "")
     #   print(index, who)
        third_column = word_list[2].strip()
        third_column_list = third_column.split(' ')
        dna_per_cent=third_column_list[0]
        no_per_cent=dna_per_cent[:-1]
        CMs="_"+ str(int(float(no_per_cent)*68))
        keystring = who + CMs
        kit1_who_to_index_dict[keystring] = int(index)
        cMs=int(float(no_per_cent)*68)
        fourth_column = word_list[3].strip()
        fourth_column_list = fourth_column.split(' ')
        segments=int(fourth_column_list[0])

        DNA_Relative = DNA_Result(index,keystring, cMs, dna_per_cent, segments, word_list[1].rstrip())
        list_of_dna.append(DNA_Relative)
        dict_of_dna[int(index)] = DNA_Relative
 #       print(kit_word_dict["index"], kit_word_dict["segments"],kit_word_dict["cM"])
        line_no = line_no + 1

    return list_of_dna, kit1_who_to_index_dict, dict_of_dna

def get_cousin_filtered(kit1):

    file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/23andMe/"
    list_of_filtered = []
    dict_of_dna = {}
    kit1_who_to_index_dict = {}
    line_no = 1
    for line in open(file_path + kit1 + '.txt', encoding='latin-1'):
        line = line.rstrip()
        word_list = line.split(',')
        first_column = word_list[0].rstrip()
        first_column_list = first_column.split(' ')
        index = first_column_list[0]
        who = first_column.strip(index + ' ')
        who=who.replace(" ", "")
       # print(index, who)
        third_column = word_list[2].strip()
        third_column_list = third_column.split(' ')
        dna_per_cent=third_column_list[0]
        no_per_cent=dna_per_cent[:-1]
        CMs="_"+ str(int(float(no_per_cent)*68))
        keystring = who + CMs
        kit1_who_to_index_dict[keystring] = index
        cMs=int(float(no_per_cent)*68)
        fourth_column = word_list[3].strip()
        fourth_column_list = fourth_column.split(' ')
        segments=int(fourth_column_list[0])

        list_of_filtered.append(int(index))
        line_no = line_no + 1

    return list_of_filtered

def get_surnames_in_trees(kit4, dict_of_dna, kit1_who_to_index_reverse_dict):

    file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/23andMe/"
    line_no = 1
    for line in open(file_path + kit4 + '.txt', encoding='latin-1'):
        line = line.rstrip()
        word_list = line.split(', ')
        first_column = word_list[0].rstrip()
        first_column_list = first_column.split(' ')
        index = int(first_column_list[0]) # dont care about the name, the index is sufficient
        if "Cousin" not in word_list[1]:
            dna_result=dict_of_dna[index].add_surnames(word_list[1])

    return True


def get_shared_list(kit1, kit1_who_to_index_dict, list_of_filtered):

    file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/23andMe/"
    list_of_shares = []
    line_no = 1
    last_cousin_index = 99999
    temp_list = []
    for line in open(file_path + kit1 + '.txt', encoding='latin-1'):
        line = line.rstrip()
        columns = line.split(',')
        first_column = columns[0].rstrip()
        first_column_list = first_column.split(' ')
        this_cousin_index = int(first_column_list[0])
        fourth_column = columns[3].rstrip()   # (0.43)
        fourth_column = fourth_column.replace('(','')
        no_per_cent = fourth_column.replace(')','') # just the 0.43
        CMs = "_" + str(int(float(no_per_cent) * 68))
        key_string=columns[1].strip()
        key_string=key_string.replace(' ','')
        key_string=key_string + CMs
        shares_with_index=kit1_who_to_index_dict[key_string]

       # print(key_string)
       # print("checkin" , this_cousin_index)
        if this_cousin_index not in list_of_filtered:
       #   print(this_cousin_index, "not in list of filtered")
          if this_cousin_index != last_cousin_index and shares_with_index not in list_of_filtered: # reset or set list
            if last_cousin_index != 99999: # a reset do stash old temp_list
                list_of_shares.append(temp_list)
            temp_list = [this_cousin_index, shares_with_index]
            last_cousin_index = this_cousin_index
          elif this_cousin_index == last_cousin_index and shares_with_index not in list_of_filtered:
                  temp_list.append(shares_with_index)
        #else:
        #          print(this_cousin_index , " is filtered")
  #      print(kit1_who_to_index_dict[columns[1].strip()])
    list_of_shares.append(temp_list) # dont forget the last line of file
   # print(list_of_shares)
    return list_of_shares

def print_cluster(supergroup, cousin, new_dict_of_lists, kit1_who_to_index_dict, kit1_who_to_index_reverse_dict,  dict_of_dna):
    punter = 0
    banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    group_total1 = len(new_dict_of_lists[cousin])
    print(group_total1, banner_string, kit1_who_to_index_reverse_dict[int(cousin)], banner_string)

    print(cousin, new_dict_of_lists[cousin])
    my_list = new_dict_of_lists[cousin]
    my_new_list=[]
    for i in my_list:
        my_new_list.append(i)
    my_new_list.sort()
   # print(kit1_who_to_index_reverse_dict)
    for kit1_index in my_new_list:
        cousin_name=kit1_who_to_index_reverse_dict[kit1_index]
        kit1_shared=dict_of_dna[kit1_index].sharedDNA
        kit1_cM=dict_of_dna[kit1_index].centimorgans
        kit1_seg=dict_of_dna[kit1_index].segments
        kit1_surnames=dict_of_dna[kit1_index].surnames
        if kit1_surnames=="Empty":
            kit1_surnames=""
    #     print(kit1_index, kit1_who_to_index_reverse_dict[kit1_index],cousin,dict_of_dna[kit1_index].centimorgans,"cM")
        print('{0:6} {1:30} {2:3} cM {3:2} seg {4:6} {5:20}'.format(kit1_index, cousin_name, kit1_cM, kit1_seg, kit1_shared , kit1_surnames))

    return True


def main():
    kit1 = '23_And_Me_Relatives'
    kit2 = '23_And_Me_Shared2'
    kit2 = '23_And_Me_InCommon'
    kit3 = '23_And_Me_Filtered'
    kit4 = '23_And_Me_Relatives_Surnames'
    DNA_relatives_list, kit1_who_to_index_dict, dict_of_dna = get_cousin_dict(kit1)
    kit1_who_to_index_reverse_dict = dict((v, k) for k, v in kit1_who_to_index_dict.items())

    dontcare = get_surnames_in_trees(kit4, dict_of_dna, kit1_who_to_index_reverse_dict)
    list_of_filtered = get_cousin_filtered(kit3)
    print(list_of_filtered)

    list_of_shares = get_shared_list(kit2, kit1_who_to_index_dict, list_of_filtered)
   # for cousin in list_of_shares:
   #     print(kit1_who_to_index_reverse_dict[cousin[0]],cousin)

    dict_of_sets = {}
    dict_of_shared_matches = {}
    for cousin_set in list_of_shares:
      #  print(cousin_set)  #debug file not saved eg Wayne_A.txt
        try:
            index = cousin_set[0]
            dict_of_sets[index] = set(cousin_set)
            del cousin_set[0]  # dont include key index for shared matches
            dict_of_shared_matches[index] = cousin_set   # used by print_cluster
        except:
            print(" blank line at end of file ", cousin_set,index)
            exit(1)
    print("*********************** Combining now *****************************")
    print("***************************************************************")
    new_cousin_list=[]
    new_dict_of_lists = {}
    for cousin1 in dict_of_sets:
        for cousin2 in dict_of_sets:
            if cousin1 != cousin2: # ignore the first entry other entries not in any particular order
                if len(list(dict_of_sets[cousin1].intersection(dict_of_sets[cousin2]))) > 0:
                    dict_of_sets[cousin1] = dict_of_sets[cousin1].union(dict_of_sets[cousin2])
                    dict_of_sets[cousin2] = dict_of_sets[cousin1].union(dict_of_sets[cousin2])

    print("***********************All done *****************************")

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
      #      print(cousin, new_dict_of_lists)
            print_cluster(supergroup, cousin, new_dict_of_lists, kit1_who_to_index_dict, kit1_who_to_index_reverse_dict, dict_of_dna)


            new_list.append(supergroup)
            new_dict[supergroup] = cousin

            supergroup += 1
            supertotal = supertotal + group_total

    supertotal = 0
    supergroup = 1
    minibanner=">>>>>>>>>>"
    for cousin in new_cousin_list:
        group_total = len(new_dict_of_lists[cousin])
        supergroup += 1
        supertotal = supertotal + group_total
        print(supergroup, kit1_who_to_index_reverse_dict[int(cousin)], cousin, minibanner, "group_total=", group_total, minibanner, "running_total=",  supertotal)


    print("number of super groups is ", supergroup - 1, "total cousins is ", supertotal)



if __name__ == '__main__':
      main()
