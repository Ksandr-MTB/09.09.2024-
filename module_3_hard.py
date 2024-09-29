data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, ['cube', 7, 'drum', 8]), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

sum2_list = []

def list_lvl1(spisok, level=1, sum_list=[]):
    global sum2_list

    # print(spisok, 'level=', level)
    a = spisok

    for i in range(len(a)):
        if type(a[i]) == int:
            sum_list.append(a[i])
        elif type(a[i]) == str:
            sum_list.append(len(a[i]))

        elif type(a[i]) == dict:
            a[i] = list(a[i].items())
            for j in range(len(a[i])):
                if type(a[i][j]) == str:
                    sum_list.append(len(a[i][j]))
                elif type(a[i][j]) == int:
                    sum_list.append(a[i][j])
        elif type(a[i]) == set:
            a[i] = list(a[i])
            for j in range(len(a[i])):
                if type(a[i][j]) == str:
                    sum_list.append(len(a[i][j]))
                elif type(a[i][j]) == int:
                    sum_list.append(a[i][j])
    for i in spisok:
        if type(i) == list:
            list_lvl1(i, level + 1)
        elif type(i) == tuple:
            list_lvl1(i, level + 1)
        elif type(i) == dict:
            list_lvl1(i, level + 1)
        elif type(i) == set:
            list_lvl1(i, level + 1)
    sum2_list = sum_list


list_lvl1(data_structure)

print(sum(sum2_list))
