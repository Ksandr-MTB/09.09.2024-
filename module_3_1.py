calls = 0

def count_calls():
    global calls
    calls=calls+1


def string_info():
    count_calls()
    a = input('Введите строку: ')
    qw = []
    qw.append(len(a))
    qw.append(a.upper())
    qw.append(a.lower())
    qw = tuple(qw)
    print(qw)

def is_contains():
    count_calls()
    a = input('Введите строку: ')
    b = list((input('Введите слова через пробел ')).split())
    r = 0
    for i in range(len(b)):
        q = b[i]
        if a.upper() == q.upper():
            r += 1
    if r > 0:
        print(True)
    else:
        print(False)


string_info()
string_info()
is_contains()
is_contains()
print(calls)

