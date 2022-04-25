
file_path = "c:/Users/Wayne/DNA/"
line_no = 1
word_list = []
key_list = []
Surnames = {}
for line in open(file_path + 'Surnames.txt', encoding='latin-1'):
        line = line.rstrip()
        word_list = line.split(',')
        key = word_list[0]
        del word_list[0]
        Surnames[key] = word_list


Surnames2 = {}
EmptySet = set()
for key in Surnames:
    NewSet = set(Surnames[key])
    EmptySet = EmptySet.union(NewSet)
print(EmptySet)
for match_surname in EmptySet:
    Surnames2[match_surname] = []
    for matchkey in Surnames:
        if match_surname in Surnames[matchkey]:
            Surnames2[match_surname].append(matchkey)

for surname in Surnames2:
    if len(Surnames2[surname]) > 1:
        print(surname,Surnames2[surname])

