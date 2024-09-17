def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list=[25, 'I love MTB', [1, 23.5]]
values_dict={'a':15, 'b':'MTB', 'c':True}

print_params()
print_params(*values_list)
print_params(**values_dict)

values_list_2=['I love ROK!!!', 'I love MTB!!!']
print_params(*values_list_2, 'Urban TOP!!!')