
import re
import sys

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



def get_data(word_list,index_offset , line_no, kit, kit_number, duplicate_check_flag):
    new_word_dict = {}
    new_word_dict["People"] = "zero"
    new_word_dict["Tree"] = ""
    new_word_dict["GEDMATCH"] = ""
    new_word_dict["CHROMOSOMES"] = ""
    i = 0
    new_index = 9999999

    for column in word_list:
      if "Shared" or "DNA:" in word_list:
        if column == "Cousin" and (index_offset == 0 or index_offset == 150000 or index_offset == 140000 or index_offset == 130000):
#            print(index_offset, word_list)
            new_word_dict["index"] = str(int(word_list[0]) + index_offset)
#            print(new_word_dict["index"] , word_list)
#            new_index = word_list[0]
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
        elif column == "Cousin" and (index_offset != 0 and index_offset != 130000 and index_offset != 140000 and index_offset != 150000):
            new_index = line_no + index_offset
            new_word_dict["index"] = new_index
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
            if i == 13:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8] + word_list[9] + word_list[10] + word_list[11]
            if i == 14:
                new_word_dict["who"] = word_list[0] + word_list[1] + word_list[2] + word_list[3] + word_list[4] + word_list[5] + word_list[6] + word_list[7] + word_list[8] + word_list[9] + word_list[10] + word_list[11] + word_list[12]
        if column == "cM":
            new_word_dict[column] = word_list[i-1]
            # new_word_dict["who"] = new_word_dict["who"] + word_list[i-1] + "cM"
        if column == "segments":
            new_word_dict[column] = word_list[i-1]
        if column == "People":
            try:
                new_word_dict[column] = word_list[i-1]
                #new_word_dict["People"] = new_word_dict["People"].replace(',', '')
                new_word_dict["key_string"] = new_word_dict["who"] + "_" + word_list[i-1]
            except:
                print(word_list, column, i, index_offset, new_word_dict)
                exit(1)
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
      else:
          print ("Shared or DNA: is missing",word_list, line_no, kit)
          exit(1)

    #print(int(line_no) , new_word_dict["who"])  # debug iso format text
    kit_duplicate_check = "none"
    if duplicate_check_flag:
        kit_duplicate_check = new_word_dict["who"] + "_" + new_word_dict["cM"] + "_" + new_word_dict["segments"]  # allow for recent tree changes

#    test_result = DNA_Result(int(line_no) , index_offset, new_word_dict["who"] , new_word_dict["cM"] ,
    try:
        test_result = DNA_Result(int(new_word_dict["index"]) , index_offset, new_word_dict["who"] , new_word_dict["cM"] ,
                             new_word_dict["segments"], new_word_dict["People"], new_word_dict["key_string"],
                             new_word_dict["Tree"], kit_duplicate_check , kit, kit_number,
                             new_word_dict["GEDMATCH"], new_word_dict["CHROMOSOMES"])
    except:
        print(int(line_no), new_word_dict["who"])  # debug iso format text

    return new_word_dict, test_result, kit_duplicate_check


def get_cousin_dict(kit,kit_number, kit_key_list,duplicate_key_list, kit_who_list,kit_who_dict, dna_list, dna_list_index, duplicate_dict, cousin_key_list, Test_Result_Dict, duplicate_check_flag, file_path):
    index_offset = 0
    dict_of_lists = {}
    #file_path = '/mnt/c/Users/Wayne/DNA/'
    #file_path = "c:/Users/Wayne/DNA/"
    old_index=9999999999
    pattern = re.compile(".+_(.*)cM")  # looking for pre-indexed files eg Gary_14cM
    patternA = re.compile(".+_A")  #
    patternB = re.compile(".+_B")  #
    patternL = re.compile(".+_L")  #
    mobj = pattern.match(kit)
    mobjA = patternA.match(kit)
    mobjB = patternB.match(kit)
    mobjL = patternL.match(kit)
    if mobj:
        if int(mobj.group(1)) == 6:
            index_offset = 200000
        if int(mobj.group(1)) == 7:
            index_offset = 300000
        if int(mobj.group(1)) == 8:
            index_offset = 10000
        if int(mobj.group(1)) == 9:
            index_offset = 30000
        if int(mobj.group(1)) == 10:
            index_offset = 40000
        if int(mobj.group(1)) == 11:
            index_offset = 50000
        if int(mobj.group(1)) == 12:
            index_offset = 60000
        if int(mobj.group(1)) == 13:
            index_offset = 70000
        if int(mobj.group(1)) == 14:
            index_offset = 80000
        if int(mobj.group(1)) == 15:
            index_offset = 90000
    if mobjA or mobjB:
        index_offset = 500000
    if mobjL:
        index_offset = 510000
    print("loading ", kit + " offset = " + str(index_offset))
    line_no = 1
    for line in open(file_path + kit + '.txt', encoding='latin-1'):
        error_string = ''
        duplicate_found = False
        line = line.rstrip()
        line = line.replace('\t',' ')
        line = line.replace(',', '')
        word_list = line.split()
#        search_duplicate_string = ""
        if (line_no == 1) and word_list[0] == "1":
            mobj = pattern.match(kit)
            if mobj:
                  index_offset = int(mobj.group(1)) * 10000  # start at 130000 for 13cM
                  #index_offset = int(mobj.group(1)) * 1000  # start at 160000 for 14cM
                  print("file is indexed already", mobj.group(1) , index_offset, kit)

        kit_word_dict, test_result, kit_duplicate_check = get_data(word_list, index_offset , line_no, kit, kit_number, duplicate_check_flag)
#        search_duplicate_string = kit_duplicate_check
        #print(test_result.keystring)
        if duplicate_check_flag:
          search_duplicate_string = kit_duplicate_check
          if kit_word_dict["key_string"] not in kit_key_list:
              kit_key_list.append(kit_word_dict["key_string"])
          else:
            error_string = kit + " " + str(test_result.index) + " " + kit_word_dict["key_string"]
            duplicate_key_list.append(error_string)
          if search_duplicate_string in kit_who_list:
            old_index = kit_who_dict[search_duplicate_string]
            print(old_index, search_duplicate_string , "!!!!" , "posible duplicate", kit, line_no, test_result.keystring)
            duplicate_found = True
            old_index2 = dna_list_index.index(old_index)
            old_test = dna_list[old_index2]
#            print(old_index, search_duplicate_string , "!!!!" , old_test.kit, old_test.index, old_test.keystring , "posible duplicate", kit, line_no, test_result.keystring)
            if search_duplicate_string in duplicate_dict:
                duplicate_dict[search_duplicate_string].append(test_result.index)
#                print("in LIST ", test_result.index)
     #       else:
#                print("not in LIST ", test_result.mega_index, test_result.index)
#                duplicate_dict[search_duplicate_string] = [old_test.mega_index, test_result.mega_index]
    #            duplicate_dict[search_duplicate_string] = [old_test.index, test_result.index]

          else:
            kit_who_list.append(search_duplicate_string)
 #           kit_who_dict[search_duplicate_string] = line_no + index_offset
            kit_who_dict[search_duplicate_string] = test_result.index

        if not duplicate_found:
          kit_word_dict["index"] = test_result.index + index_offset
         #kit_person_dict[int(line_no) + int(index_offset)] = test_result
          dict_of_lists[int(test_result.index) + int(index_offset)] = kit_word_dict
          dna_list.append(test_result)
#         total_dna_list.append(test_result)
          keystring = test_result.keystring
#         if keystring in cousin_key_list:   # useful debug
#            print(keystring, kit, line_no)
#            exit(1)
          if error_string == '':
            Test_Result_Dict[keystring] = test_result
            #print(keystring)
          cousin_key_list.append(keystring)
#         dna_list_index.append(test_result.index + index_offset)
          dna_list_index.append(test_result.index)
        line_no = line_no + 1
    return


def load_matches(file_list, kit_number, duplicate_check_flag, file_path):
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

    for text_file in file_list:
        kit_person = file_list[0]
        #print (text_file, 10000* kit_offset_index)
        get_cousin_dict(text_file, kit_number, kit_key_list, duplicate_key_list, kit_who_list,
                                             kit_who_dict, dna_list, dna_list_index, duplicate_dict, cousin_key_list, Test_Result_Dict, duplicate_check_flag, file_path)
        kit_offset_index += 1
    duplicate_index = 1
    if duplicate_check_flag:
      for error in duplicate_key_list:
        print(duplicate_index, "duplicate key >>>>>", error)
        duplicate_index += 1
      duplicate_index = 1
      for duplo in duplicate_dict:
        new_index = 0
        print("--------------------" , duplicate_index , "------------------------------------")
        for mega_index1 in duplicate_dict[duplo]:
#              print (mega_index1,dna_list_index)
              old_index2 = dna_list_index.index(mega_index1)
              test = dna_list[old_index2]
              kitname = test.kit
              line_no = test.index
              keystring = test.keystring
              check = test.kit_duplicate_check
              print( check, kitname, line_no, keystring, mega_index1)
        duplicate_index += 1

    return Test_Result_Dict

def main():
    duplicate_check_flag = True
    # file_path = "/mnt/c/Users/Wayne/DNA/"
    file_path = "//wsl$/Ubuntu-20.04/home/waynew/git_environment/ANCESTRY-DNA-Helper/DNA/"
    if len(sys.argv) > 1:
      if sys.argv[1] == "ubuntu":
        file_path = "/home/waynew/git_environment/ANCESTRY-DNA-Helper/DNA/"
      elif sys.argv[1] == "aws":
        file_path = "/home/ec2-user/"
      else:
        file_path = "c:/Users/Wayne/DNA/"



    kit1_keystring_list = []
    kit2_keystring_list = []
#    kit1_file_list = ["Glyn", "Glyn_9cM", "Glyn_8cM", "Glyn_7cM", "Glyn_6cM","Glyn_B"]
 #   kit1_file_list = ["Glyn", "Glyn_15cM", "Glyn_14cM","Glyn_13cM", "Glyn_12cM", "Glyn_11cM", "Glyn_10cM", "Glyn_9cM", "Glyn_8cM", "Glyn_7cM", "Glyn_6cM", "Glyn_B"]
 #   kit1_file_list = ["Glyn"]
    #kit1_file_list = ["Sally"]
    kit1_file_list = ["Wayne", "Wayne_11cM" , "Wayne_10cM" , "Wayne_9cM", "Wayne_8cM" , "Wayne_7cM","Wayne_6cM","Wayne_A"]
 #   kit1_file_list = ["Wayne",  "Wayne_A"]
#  kit1_file_list = ["Wayne", "Wayne_15cM", "Wayne_14cM", "Wayne_13cM", "Wayne_12cM", "Wayne_11cM",
 #                     "Wayne_10cM", "Wayne_9cM", "Wayne_8cM", "Wayne_7cM", "Wayne_6cM"]
  #  kit1_file_list = ["Gary", "Gary_15cM", "Gary_14cM", "Gary_13cM", "Gary_12cM","Gary_11cM", "Gary_10cM","Gary_9cM", "Gary_8cM"]
    kit2_file_list = ["Elwyn", "Elwyn_15cM", "Elwyn_14cM", "Elwyn_13cM", "Elwyn_12cM","Elwyn_11cM",
        "Elwyn_10cM", "Elwyn_9cM"]


    #kit1_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM","Sally_L"]
    #kit1_file_list = ["Una", "Una_11cM", "Una_10cM", "Una_9cM", "Una_8cM", "Una_7cM", "Una_6cM", "Una_L"]


    #kit2_file_list = ["Glyn", "Dad_9cM", "Dad_8cM", "Dad_7cM", "Dad_6cM","Dad_B"]
    #kit2_file_list = ["Wayne", "Wayne_10cM", "Wayne_9cM" , "Wayne_8cM", "Wayne_7cM","Wayne_6cM_new","Wayne_A"]
#    kit1_file_list = ["Anji", "Anji_15cM", "Anji_14cM", "Anji_13cM", "Anji_12cM", "Anji_11cM", "Anji_10cM", "Anji_9cM", "Anji_8cM" ]
#    kit2_file_list = ["Marg", "Marg_15cM", "Marg_14cM", "Marg_13cM", "Marg_12cM", "Marg_11cM"]
    #kit2_file_list = ["Sally", "Sally_10cM", "Sally_9cM", "Sally_8cM", "Sally_7cM", "Sally_6cM","Sally_L"]
    #kit2_file_list = ["Helen", "Helen_B"]
#    kit2_file_list = ["Una", "Una_15cM","Una_14cM","Una_13cM","Una_12cM", "Una_11cM", "Una_10cM",
#         "Una_9cM", "Una_8cM", "Una_7cM", "Una_6cM", "Una_L"]
#    kit2_file_list = ["Gary", "Gary_14cM", "Gary_13cM", "Gary_12cM","Gary_11cM", "Gary_10cM","Gary_9cM", "Gary_8cM"]

    kit1_Test_Result_Dict = load_matches(kit1_file_list, 1, duplicate_check_flag, file_path)
    kit2_Test_Result_Dict = load_matches(kit2_file_list, 2, duplicate_check_flag, file_path)
    for kit1_Test_Result in kit1_Test_Result_Dict:
        kit1_keystring_list.append(kit1_Test_Result_Dict[kit1_Test_Result].keystring)
    for kit2_Test_Result in kit2_Test_Result_Dict:
        kit2_keystring_list.append(kit2_Test_Result_Dict[kit2_Test_Result].keystring)


    intersection_list = list(set(kit1_keystring_list).intersection(set(kit2_keystring_list)))

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

        try:
            print('{0:4} | {1:36}  {2:6} | {3:4}cM | {4:2}seg | {5:13}|***| {6:4}cM | {7:2}seg | {8:13}| {9:6} |'\
                   .format(intersectcount, kit1_cousin, kit1_index, kit1_cousin_cM, kit1_cousin_seg, kit1_people, kit2_cousin_cM, kit2_cousin_seg, kit2_people,kit2_index))
        except UnicodeEncodeError:
            print("error with ASCII UnicodeEncodeError " , kit1_Test_Result_Dict[cousin_key].kit,"=", kit1_Test_Result_Dict[cousin_key].index, kit2_Test_Result_Dict[cousin_key].kit, "=" ,  kit2_Test_Result_Dict[cousin_key].index )
            exit(1)
        intersectcount += 1

    difference_list = list(set(kit1_keystring_list).symmetric_difference(set(kit2_keystring_list)))
    difference_count = 1
    cousin1_list = []
    cousin2_list = []
    cousin1_shadow_list = []
    cousin2_shadow_list = []

    for cousin_key in difference_list:
        if cousin_key in kit1_keystring_list:
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
    print("********************************** Mismatches ???? *************************************************")
    for cousin_who in mismatch_list:
        index1 = cousin1_list.index(cousin_who)
        index2 = cousin2_list.index(cousin_who)
        key1 = cousin1_shadow_list[index1]
        key2 = cousin2_shadow_list[index2]
        cm1 = kit1_Test_Result_Dict[key1].centimorgans
        cm2 = kit2_Test_Result_Dict[key2].centimorgans
        #print(mismatch_index, cousin_who, key1, key2)
        try:
         #    print( key1, key2, cm1, cm2, cousin_who)
          #  print('{0:4} | {1:36} | {2:4} cM | {3:36 } | {4:4} cM | {5:32} ' .format(mismatch_index, key1, cm1, key2, cm2, cousin_who))
            print('{0:4} | {1:36} {2:3}cM | {3:36} {4:3}cM | {5:32} '
                   .format(mismatch_index, key1, cm1, key2, cm2, cousin_who))
        except UnicodeEncodeError:
            print("error with mismatch ASCII UnicodeEncodeError " , kit1_Test_Result_Dict[key1].kit,"=", kit1_Test_Result_Dict[key1].index, kit2_Test_Result_Dict[key2].kit, "=" ,  kit2_Test_Result_Dict[key2].index )
            exit(1)

        mismatch_index += 1




 #   for everbody in total_dna_list:
  #      print (everbody.who, everbody.kit, everbody.keystring)



if __name__ == '__main__':
      main()
