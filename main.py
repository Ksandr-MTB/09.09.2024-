# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

numbers=[]
for i in range(1,16):
    numbers.append(i)
primes=[]
not_primes=[]
for i in range(len(numbers)):
    if numbers[i]!=1:
        q=0
        for j in range(2,numbers[i]):
            k=numbers[i]%j
            if k==0:
                q=q+1
        if q==0:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
    else:
        continue
print(primes)
print(not_primes)
