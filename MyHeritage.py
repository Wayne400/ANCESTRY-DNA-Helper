
import re
import sys
from collections import defaultdict
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

def triangulate(this_cousin_tuple_list, shares_with_tuple_list):
    overlap = False
    triangulate_chromo_list = []
    for this_cousin_tuple in this_cousin_tuple_list:
        for shares_with_tuple in shares_with_tuple_list:
           # overlap=False
            if this_cousin_tuple[0] == int(shares_with_tuple[0]):  # check correct chromosome
                if int(this_cousin_tuple[2]) >= int(shares_with_tuple[2]):
                    Higher=[this_cousin_tuple[1],this_cousin_tuple[2]]
                    Lower=[shares_with_tuple[1],shares_with_tuple[2]]
                else:
                    Lower=[this_cousin_tuple[1],this_cousin_tuple[2]]
                    Higher=[shares_with_tuple[1],shares_with_tuple[2]]
#                print(int(Lower[1]), int(Higher[0]))
                if int(Lower[1]) > int(Higher[0]):
                    overlap=True
                    triangulate_chromo_list.append(this_cousin_tuple[0])
               #     print("triangulate on chromo", this_cousin_tuple[0], this_cousin_tuple[1], this_cousin_tuple[2],
               #           shares_with_tuple[1], shares_with_tuple[2])
          #      else:
          #          print("unlucky on chromo", this_cousin_tuple[0], this_cousin_tuple[1], this_cousin_tuple[2],
          #                shares_with_tuple[1], shares_with_tuple[2])


        # else:
           #     print("wrong chromosome we need ", this_cousin_tuple[0])
    return overlap, triangulate_chromo_list

class triangulated_segment(object):

    def __init__(self, chromosome=999, start_location=1, end_location=99999, start_rsid="rs11", end_rsid="rs99", centimorgans=22.2222, snps=99999999 ):

        self.chromosome = chromosome
        self.start_location = start_location
        self.end_location = end_location
        self.start_rsid = start_rsid
        self.end_rsid = end_rsid
        self.centimorgans = centimorgans
        self.snps = snps



def filter_list(list_to_filter, index_match_filter_list):

    new_filtered_list = []
    for entry in list_to_filter:
        if entry not in index_match_filter_list:
            new_filtered_list.append(entry)
    return new_filtered_list

def get_cousin_dict(kit1, file_path):

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
        try:
    #    print(index, who)
          second_column = word_list[1].strip()
          second_column_list = second_column.split(' ')
          dna_per_cent=second_column_list[0]
          cMs_float=second_column_list[1]
          cMs_float = cMs_float.replace(")", "")
          cMs_float = cMs_float.replace("(", "")
          no_per_cent=dna_per_cent[:-1]
    #     print(no_per_cent)
          CMs="_"+ str(int(float(no_per_cent)*68))
          keystring = who + CMs
          name_part=first_column.strip(index)
          keystring=get_key_string_MyHeritage(name_part, second_column)
#          print(keystring)
          kit1_who_to_index_dict[keystring] = int(index)
          #cMs=int(float(no_per_cent)*68)
          cMs=float(cMs_float)
          third_column = word_list[2].strip()
          third_column_list = third_column.split(' ')
          segments=int(third_column_list[0])
#          print(index, who, keystring, cMs, cMs_float )
          DNA_Relative = DNA_Result(index,keystring, cMs, dna_per_cent, segments, word_list[1].rstrip())
          list_of_dna.append(DNA_Relative)
          dict_of_dna[int(index)] = DNA_Relative
 #         print(kit_word_dict["index"], kit_word_dict["segments"],kit_word_dict["cM"])
          line_no = line_no + 1
        except:
          print("ERROR *********   ERROR *********" , index, who)

    return list_of_dna, kit1_who_to_index_dict, dict_of_dna

def get_cousin_filtered(kit1, file_path):

    list_of_filtered = []
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

        list_of_filtered.append(int(index))
        line_no = line_no + 1

    return list_of_filtered

def get_key_string_MyHeritage(name_part, third_column):
    third_column = third_column.replace('(', '')
    third_column = third_column.replace(')', '')  # just the 0.43
    third_column_list = third_column.split(' ')
    try:
        this_cousin_cm = float(third_column_list[1])
 #   print(name_part)
        CMs = "_" + str(int(this_cousin_cm * 10))
        key_string = name_part.strip()
        key_string = key_string.replace(' ', '')
        key_string = key_string + CMs
    except:
        print(name_part)
        key_string = "ERROR wrong file again" + name_part + third_column

    return key_string


def get_surnames_in_trees(kit4, dict_of_dna, kit1_who_to_index_reverse_dict, file_path, fmp_dict, ancestry_tree_dict):

    line_no = 1
    for line in open(file_path + kit4 + '.txt', encoding='latin-1'):
        line = line.rstrip()
        word_list = line.split(', ')
        first_column = word_list[0].rstrip()
        first_column_list = first_column.split(' ')
        index = int(first_column_list[0]) # dont care about the name, the index is sufficient
        if "Cousin" not in word_list[1]:
            if word_list[1] in fmp_dict:
                dna_result = dict_of_dna[index].add_surnames(fmp_dict[word_list[1]])
            elif word_list[1] in ancestry_tree_dict:
                dna_result = dict_of_dna[index].add_surnames(ancestry_tree_dict[word_list[1]])
            else:
                dna_result = dict_of_dna[index].add_surnames(word_list[1])

    return True

def get_fmp_all_trees(file_path):
    dict_of_fmp = {}
    line_no = 1
    for line in open(file_path, encoding='latin-1'):
      #  print(line)
        line = line.rstrip()
        word_list = line.split(' : ')
        fourth_column = word_list[3].rstrip()
        fourth_column_list = fourth_column.split(',')
        index = word_list[0] # dont care about the name, the index is sufficient
        csv_string = word_list[0] + "," + word_list[3]
        dict_of_fmp[index] = csv_string

    return dict_of_fmp

def get_ancestryDNA_trees(file_path):
    dict_of_trees = {}
    line_no = 1
    for line in open(file_path, encoding='latin-1'):
      #  print(line)
        line = line.rstrip()
        word_list = line.split(',')
        index = word_list[0]
        word_list.pop(0)
        dict_of_trees[index] = line

    return dict_of_trees


def get_shared_list(kit1, kit1_who_to_index_dict, list_of_filtered, file_path,  chromo_tuple_list, kit1_who_to_index_reverse_dict, dict_of_dna):
    # Initialize a defaultdict with list as the default type
    my_silly_string = defaultdict(list)
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
        name_part = columns[1].strip()
        cM_part = columns[2].strip()   # (0.43)
        key_string = get_key_string_MyHeritage(name_part, cM_part)
        shares_with_index=kit1_who_to_index_dict[key_string]
        kit1_seg = dict_of_dna[shares_with_index].segments
   #     if shares_with_index not in list_of_filtered and kit1_seg > 1:
   #         list_of_filtered.append(shares_with_index)

        overlap = False
        if shares_with_index in chromo_tuple_list and this_cousin_index in chromo_tuple_list:
            #     print(this_cousin_index ,kit1_who_to_index_reverse_dict[this_cousin_index], chromo_tuple_list[this_cousin_index], shares_with_index, kit1_who_to_index_reverse_dict[shares_with_index], chromo_tuple_list[shares_with_index])
            #    print(kit1_who_to_index_reverse_dict[this_cousin_index],  kit1_who_to_index_reverse_dict[shares_with_index])
            overlap, triang_chromo_list = triangulate(chromo_tuple_list[this_cousin_index],
                                                      chromo_tuple_list[shares_with_index])
            if overlap and  sys.argv[2] == "triangulate":
                print(this_cousin_index, kit1_who_to_index_reverse_dict[this_cousin_index],shares_with_index,
                      kit1_who_to_index_reverse_dict[shares_with_index], "triangulate=>", triang_chromo_list)
                my_silly_string[this_cousin_index].append(shares_with_index)
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
    return list_of_shares,my_silly_string

def print_clusterMH(supergroup, cousin, new_dict_of_lists, kit1_who_to_index_dict, kit1_who_to_index_reverse_dict,  dict_of_dna, dict_of_lists):
    punter = 0
    banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    group_total1 = len(new_dict_of_lists[cousin])
    print(group_total1, banner_string, kit1_who_to_index_reverse_dict[int(cousin)], banner_string)

 #   print(cousin, new_dict_of_lists[cousin])
    my_list = new_dict_of_lists[cousin]
    my_new_list=[]
    for i in my_list:
        my_new_list.append(dict_of_dna[i].centimorgans)
       # print(dict_of_dna[i].centimorgans)
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
        if kit1_index in dict_of_lists:
            my_new_list = dict_of_lists[kit1_index]
            for tuple in my_new_list:
                print(tuple)
                #for item in tuple:
                 #   print(item)


    return True

def print_cluster23(supergroup, cousin, new_dict_of_lists, kit1_who_to_index_dict, kit1_who_to_index_reverse_dict,  dict_of_dna, chromo_tuple_dict, my_silly_dict):
    punter = 0
    banner_string = " >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    group_total1 = len(new_dict_of_lists[cousin])
    banner_string2 = " supergroup = " + str(supergroup) + " group total = " + str(group_total1)
    print( banner_string, kit1_who_to_index_reverse_dict[int(cousin)], banner_string2)

  #  print(cousin, new_dict_of_lists[cousin])
    my_list = new_dict_of_lists[cousin]
#    my_new_list=[]
    my_very_new_list=[]
    my_new_dict={}
    silly_string = ""
    for i in my_list:
        my_new_dict[i] = dict_of_dna[i].centimorgans
    data_sorted = {k: v for k, v in sorted(my_new_dict.items(), key=lambda x: x[1], reverse=True)}
    for kit1_index in data_sorted:
        seg_string=""
        cousin_name=kit1_who_to_index_reverse_dict[kit1_index]
        kit1_shared=dict_of_dna[kit1_index].sharedDNA
        kit1_cM=dict_of_dna[kit1_index].centimorgans
        kit1_seg=dict_of_dna[kit1_index].segments
        kit1_surnames=dict_of_dna[kit1_index].surnames
        if kit1_surnames=="Empty":
            kit1_surnames=""
        silly_string = ""
        if kit1_index in chromo_tuple_dict:
            my_very_new_list = chromo_tuple_dict[kit1_index]
            my_really_silly_list = my_silly_dict[kit1_index]
            seg_string = ""
            silly_string = ""
            for tuple in my_very_new_list:
                seg_string = seg_string + "-" + str(tuple[0])
            for silly in my_really_silly_list:
                silly_string = silly_string + "-" + str(silly)

              #  print(tuple[0])
    #     print(kit1_index, kit1_who_to_index_reverse_dict[kit1_index],cousin,dict_of_dna[kit1_index].centimorgans,"cM")
        if sys.argv[2]  == "tree":
            print('{0:6} {1:30} {2:3} cM {3:2} seg {4:6} {5:20} {6:30}'.format(kit1_index, cousin_name, kit1_cM, kit1_seg, kit1_shared ,seg_string, kit1_surnames))
        elif sys.argv[2]  == "triangulate":
            print('{0:6} {1:30} {2:3} cM {3:2} seg {4:6} {5:20} {6:30}'.format(kit1_index, cousin_name, kit1_cM, kit1_seg, kit1_shared ,seg_string, silly_string))

    return True

def get_chromo_list(kit4, kit1_who_to_index_dict,  file_path):
    chromo_file_type = 0
    if "23andMe" in file_path:
        chromo_file_type = 2
      #  print("23 and Me")
    elif "MyHeritage" in file_path:
        chromo_file_type = 1
    seventh_column = "seventh column dummy"
    eigth_column = "eigth eigth dummy"
    dict_of_lists={}
    last_cousin_index = 8989898
    list_of_lists = []
    for line in open(file_path + kit4 + '.txt', encoding='latin-1'):
        line = line.rstrip()
        try:
  #      print(line)
          columns = line.split(',')
     #   print(columns, len(columns))
          first_column = columns[0].rstrip()
          second_column = columns[1].rstrip()
          third_column = columns[2].rstrip()
          fourth_column = columns[3].rstrip()
          fifth_column = columns[4].rstrip()
          sixth_column = columns[5].rstrip()
          if chromo_file_type == 1:
            seventh_column = columns[6].rstrip()
            eigth_column = columns[7].rstrip()
          first_column_list = first_column.split(' ')
          this_cousin_index = int(first_column_list[0])
          chromosome = int(second_column)
          start_location = int(third_column)
          end_location = int(fourth_column)
          if chromo_file_type == 1:
            start_rsid = fifth_column
            end_rsid = sixth_column
            centimorgans = float(seventh_column)
            snps = int(eigth_column)
            my_tuple = chromosome, start_location, end_location, start_rsid, end_rsid, centimorgans, snps
          elif chromo_file_type == 2:
            centimorgans = float(fifth_column)
            snps = int(sixth_column)
            my_tuple = chromosome, start_location, end_location, centimorgans, snps
          else:
            my_tuple = chromosome, start_location, end_location,

        #my_tuple=(first_column,second_column,third_column,fourth_column,fifth_column,sixth_column,seventh_column,eigth_column)
   #     my_tuple= chromosome,start_location,end_location,start_rsid,end_rsid,centimorgans,snps
   #     my_match=triangulated_segment(  chromosome, start_location, end_location, start_rsid, end_rsid, centimorgans, snps)
    #    current_list = [chromosome,start_location,end_location,start_rsid,end_rsid,centimorgans,snps]
          if this_cousin_index == last_cousin_index:
            list_of_lists.append(my_tuple)
            dict_of_lists[this_cousin_index] = list_of_lists
          else:
            last_cousin_index = this_cousin_index
            list_of_lists = [my_tuple]
            dict_of_lists[this_cousin_index] = list_of_lists
        except:
           print("ERROR",line)
 #       print( this_cousin_index, chromosome, start_location, end_location, start_rsid, end_rsid, centimorgans, snps)
    return dict_of_lists

def main():
    if sys.argv[1] == "Wayne":
        kit1 = 'MyHeritage_Cousins_Wayne'
        kit2 = 'MyHeritage_InCommon_Wayne'
        kit3 = 'MyHeritage_Filtered_Wayne'
        kit4 = 'MyHeritage_Chromosomes_Wayne'
        kit5 = 'MyHeritage_Trees_Wayne'
    else:
        kit1 = 'MyHeritage_Cousins_Glyn'
        kit2 = 'MyHeritage_InCommon_Glyn'
        kit3 = 'MyHeritage_Filtered_Glyn'
        kit4 = 'MyHeritage_Chromosomes_Glyn'
        kit5 = 'MyHeritage_Trees_Glyn'




    file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/MyHeritage/"

    DNA_relatives_list, kit1_who_to_index_dict, dict_of_dna = get_cousin_dict(kit1, file_path)
    kit1_who_to_index_reverse_dict = dict((v, k) for k, v in kit1_who_to_index_dict.items())
    fmp_dict = get_fmp_all_trees("/home/waynew/git_environment/ANCESTRY-DNA-Helper/DNA/FMP_all_trees.txt")
    ancestry_tree_dict = get_ancestryDNA_trees("/home/waynew/git_environment/ANCESTRY-DNA-Helper/DNA/Surnames.txt")
    dontcare = get_surnames_in_trees(kit5, dict_of_dna, kit1_who_to_index_reverse_dict, file_path, fmp_dict, ancestry_tree_dict)
    list_of_filtered = get_cousin_filtered(kit3, file_path)
 #   print(list_of_filtered)
    chromo_tuple_dict = get_chromo_list(kit4, kit1_who_to_index_dict, file_path)
 #   print(len(list_of_filtered))
    my_silly_dict={}
    list_of_shares, my_silly_dict = get_shared_list(kit2, kit1_who_to_index_dict, list_of_filtered, file_path,  chromo_tuple_dict, kit1_who_to_index_reverse_dict, dict_of_dna)
 #   print(len(list_of_filtered))
    chromo_list = get_chromo_list(kit4, kit1_who_to_index_dict, file_path)
  #  print(dont_care)
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
       #     print(supergroup, banner_string,  cousin, group_total,  banner_string, CentiMorgan)
      #      print(cousin, new_dict_of_lists)
            print_cluster23(supergroup, cousin, new_dict_of_lists, kit1_who_to_index_dict, kit1_who_to_index_reverse_dict, dict_of_dna, chromo_list, my_silly_dict)
        #    print_clusterMH(supergroup, cousin, new_dict_of_lists, kit1_who_to_index_dict, kit1_who_to_index_reverse_dict, dict_of_dna, chromo_list)


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
#    print(dont_care)


if __name__ == '__main__':
      main()
