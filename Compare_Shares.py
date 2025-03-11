

from SharedMatchesSetsV4 import  get_shared_dict

def compare_eggs(index1, index2, index_list_dict, key_to_numeric_dict_reverse ):
      output_list_1 = []
      output_list_2 = []
      list1= index_list_dict[str(index1)]
      list2= index_list_dict[str(index2)]
      list1.append(index1)
      list2.append(index2)
      difference_list = list(set(list1).symmetric_difference(set(list2)))
      intersection_list = list(set(list1).intersection(set(list2)))

      for numeric_key in difference_list:
            if numeric_key in list1:
                where_found=key_to_numeric_dict_reverse[index1]
                output_list_1.append(key_to_numeric_dict_reverse[numeric_key])
            else:
                where_found = key_to_numeric_dict_reverse[index2]
                output_list_2.append(key_to_numeric_dict_reverse[numeric_key])
   #         print('{0:40} {1:40}'.format(key_to_numeric_dict_reverse[numeric_key], where_found))
       #     print(key_to_numeric_dict_reverse[numeric_key], where_found)
      print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      print(key_to_numeric_dict_reverse[index1])
      print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
      for entry in output_list_1:
            print('{0:40} '.format(entry ))
      print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
      print(key_to_numeric_dict_reverse[index2])
      print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
      for entry in output_list_2:
            print('{0:40}'.format(entry))
      print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
      print("intersection of " , key_to_numeric_dict_reverse[index1],key_to_numeric_dict_reverse[index2])
      print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")
      for entry in intersection_list:
            print('{0:40}'.format(key_to_numeric_dict_reverse[entry]))
      print("VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV")



def main():
    file_path = './DNA/'
    share_file = "Glyn_Shared.txt"
    person = "Glyn"
    banner_string = "***************************"
    cluster_king = "walter_67"
    CentiMorgan = 23
    group_total = 56
    shared_file_path = file_path + share_file
    shared_list_dict, index_list_dict, key_to_numeric_dict = get_shared_dict(shared_file_path)
    new_list = [0, 1, 2, 3]
    key_to_numeric_dict_reverse = dict((v, k) for k, v in key_to_numeric_dict.items())
    index1 = 0
    index2 = 0
    go_again = 'y'
    toggle = False  # start in surnames mode
    mode = 1  # info mode
    mode_list = [" default", "info", "Surnames", " keystring", " Places", "common_ancestor", "compare eggs"]
    while go_again != 'n':
        while True:
            cluster_search = input(person + mode_list[mode] + " : Enter cluster number or q for quit: ")
            if cluster_search == 'q':
                go_again = 'n'
                break
            elif cluster_search == 'i':  # info mode
                mode = 1  # Info mode
                print("mode = 1, cluster_no, banner_string, cluster_king, group_total, banner_string, CentiMorgan")
            elif cluster_search == 's':  # surnames mode
                mode = 2  # Surnames mode
                print("mode 2 surnames")
            elif cluster_search == 'k':  # key search mode
                print("mode 3 keys mode")
                mode = 3  # Keys mode
            elif cluster_search == 'kk':  # key search mode
                print("mode 6 compare eggs mode")
                mode = 6  # eggs mode
            elif cluster_search == 'p':  # places mode
                mode = 4  # Places mode
                print("mode 4 places mode")
            elif cluster_search == 'c':  # key search mode
                mode = 5  # common ancestor mode
                print("mode 5 common ancestors mode")
            elif cluster_search[0:2] == 'cM' and len(cluster_search) > 2:  # change cM filter
                print("no mode , just change cM search")
            if cluster_search.isdigit():
                cluster_no = int(cluster_search)

                if (int(cluster_search) in new_list) and (mode == 2):  # Surnames mode
                    print(cluster_search, "change cluster number")
                elif int(cluster_search) in new_list and mode == 4:  # places mode
                    print(cluster_no, banner_string, cluster_king, group_total, banner_string)
                elif int(cluster_search) in new_list and mode == 5:  # common ancestors mode

                    print("cluster_no, banner_string, cluster_king, group_total, common_dict")
                elif int(cluster_search) in new_list and mode == 1:  # info mode
                    print(cluster_search, banner_string, cluster_king, group_total, banner_string, CentiMorgan)
            elif mode == 3:  # keys mode
                if cluster_search in key_to_numeric_dict:
                    found_index = key_to_numeric_dict[cluster_search]
                    print(banner_string, cluster_search, found_index)
            elif mode == 6:  # eggs mode
                if cluster_search in key_to_numeric_dict:
                    if index1 == 0:
                        index1 = key_to_numeric_dict[cluster_search]
                        print(banner_string, cluster_search, index1)
                    else:
                        index2 = key_to_numeric_dict[cluster_search]
                        print(banner_string, cluster_search, index2)
                        compare_eggs(index1, index2, index_list_dict, key_to_numeric_dict_reverse)
                        index1 = 0
                        mode = 3


if __name__ == '__main__':
      main()
