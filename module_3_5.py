def get_multiplied_digits(numder):
    str_numder = str(numder)
    first = int(str_numder[0])
    if len(str_numder)>1:
        return first * get_multiplied_digits(int(str_numder[1:]))
    else:
        return first

print(get_multiplied_digits(40203))






# def summa(n):
#     if n ==0:
#         return 0
#     else:
#         return n + summa(n-1)
# print(summa(5))








