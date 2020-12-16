
import re


def find_cousin_column(word_list):
    i = 0
    return_value = 0
    for column in word_list:
       match = re.search(r'Cousin',column)
       if match:
           return_value = i
       i += 1
    return return_value


def get_data(word_list,index_offset):
    new_word_dict = {}
    tree_flag = False
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
            #print(new_word_dict["index"])
            new_word_dict[column] = word_list[i-1]
            #new_word_dict["who"] = new_word_dict["who"] + "_" + word_list[i-1]
            new_word_dict["key_string"] = new_word_dict["who"] + "_" + word_list[i - 1]
            tree_flag = True
        if column == "Unlinked":
            #print(new_word_dict["index"])
            new_word_dict["Tree"] = "Unlinked Tree"
            new_word_dict["who"] = new_word_dict["who"] + "_U"
            new_word_dict["key_string"] = new_word_dict["who"] + "_U"
            tree_flag = True
        if column == "Trees":
            #print(new_word_dict["index"])
            new_word_dict["Tree"] = "No Trees"
            new_word_dict["who"] = new_word_dict["who"] + "_N"
            new_word_dict["key_string"] = new_word_dict["who"] + "_N"
            tree_flag = True
        if column == "unavailable":
            new_word_dict["Tree"] = "unavailable"
            new_word_dict["who"] = new_word_dict["who"] + "_u"
            new_word_dict["key_string"] = new_word_dict["who"] + "_u"
            tree_flag = True
        if column == "Common":
            new_word_dict[column] = "Wally"
        if column == "GEDMATCH":
            new_word_dict[column] = word_list[i+1]
        if column == "CHROMOSOMES":
            new_word_dict[column] = word_list[i+1]

        i += 1

    return new_word_dict,tree_flag


def get_cousin_dictY(kit, index_offset):

    kit_who_list = []
    dict_of_lists = {}
    line_no = 1
    for line in open(kit + '.txt'):
        line = line.rstrip()
        line = line.replace('\t',' ')
        line = line.replace(',', '')
        word_list = line.split()
        kit_word_dict = get_data(word_list, index_offset)
        search_duplicate_string = kit_word_dict["who"] + "_" + kit_word_dict["cM"] + "cM"
        if search_duplicate_string in kit_who_list:
            print(kit, kit_who_list.index(search_duplicate_string) + 1, line_no, "duplicate", kit_word_dict["who"], kit_word_dict["cM"], "cM",
                   search_duplicate_string)
        else:
            kit_who_list.append(search_duplicate_string)
        kit_word_dict["index"] = line_no + index_offset
        dict_of_lists[int(line_no + index_offset)] = kit_word_dict
        line_no = line_no + 1
    return dict_of_lists



def get_cousin_dict(kit1, index_offset):

    dict_of_lists = {}
    list_of_lists = []
    line_no = 1
    for line in open(kit1 + '.txt'):
        line = line.rstrip()
        line = line.replace('\t',' ')
        line = line.replace(',', '')
        word_list = line.split()
        kit_word_dict,tree_flag = get_data(word_list, index_offset)
        if not tree_flag :
            exit
        print(kit_word_dict["index"], line_no, kit_word_dict["segments"],kit_word_dict["cM"], word_list)
        dna_kit = kit_word_dict["who"]
        kit_word_dict["index"] = line_no + index_offset
        dict_of_lists[dna_kit] = kit_word_dict
        #print (kit_word_dict["index"], line_no, word_list)
        line_no = line_no + 1
    return dict_of_lists


def main():
    kit1 = 'Glyn'
    #kit1 = 'Wayne'
    #kit1 = 'Helen'
    #kit1 = 'Sally'
    kit1_index_offset = 0
    #kit1a = 'Dad_B'
    #kit1a = 'Wayne_6cM_new'
    #kit1a = 'Sally_L'
    kit1a = 'Dad_B'
    #kit1a = 'Una_L'
    kit1a_index_offset = 10000

    kit1_list = []
    kit1_dict_of_lists = get_cousin_dict(kit1,kit1_index_offset)
    kit1a_dict_of_lists = get_cousin_dict(kit1a, kit1a_index_offset)
    kit1_dict_of_lists.update(kit1a_dict_of_lists)
    for cousin in kit1_dict_of_lists:
        if int(kit1_dict_of_lists[cousin]["index"]) >= 10000:
            print(kit1_dict_of_lists[cousin]["index"],kit1_dict_of_lists[cousin]["segments"], kit1_dict_of_lists[cousin]["key_string"], cousin)
        kit1_list.append(cousin)


if __name__ == '__main__':
      main()
