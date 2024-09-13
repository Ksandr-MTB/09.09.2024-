# numbers = []
# for i in range(1, 16):
#     numbers.append(i)
# primes = []
# not_primes = []
# for i in range(len(numbers)):
#     if numbers[i] != 1:
#         q = 0
#         for j in range(2, numbers[i]):
#             k = numbers[i] % j
#             if k == 0:
#                 q = q + 1
#         if q == 0:
#             primes.append(numbers[i])
#         else:
#             not_primes.append(numbers[i])
#     else:
#         continue
# print(primes)
# print(not_primes)
#
# # Это я написал GitHub
# def get_matrix(n, m, value):
#     matrix = []
#     for i in range(n):
#         matrix.append([])
#         for j in range(m):
#             matrix[i].append(value)
#     print(matrix)
#     # print(get_matrix)
# get_matrix(2, 2, 10)
# get_matrix(3, 5, 42)
# get_matrix(4, 2, 13)
# get_matrix(int(input()), int(input()), int(input()))

def game():
    import random
    n=random.randint(3, 21)
    result=[]
    for i in range(1,21):
        for j in range(i+1,21):
            q=[]
            if n%(i+j)==0:
                q.append(i)
                q.append(j)
                result.append(q)


    print(f"Для числа {n} нужно ввести следующие пары чисел {result}")
game()
game()
game()