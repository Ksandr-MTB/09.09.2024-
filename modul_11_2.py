import inspect
import sys


class My_class:
    def __init__(self, tekst):
        self.tekst = tekst

    def lens(self):
        print(len(self.tekst))

    def atribut_apper(self):
        print(self.tekst.upper)


qwe = My_class('прИВет')


def my_function(n, m):
    my_dickt = {}

    def factorial(a):
        result = 1
        for i in range(1, a + 1):
            result = result * i
        return result

    my_dickt[f'умнежение {n} и {m}'] = n * m
    my_dickt[f'деление {n} и {m}'] = n / m
    my_dickt[f'сложение {n} и {m}'] = n + m
    my_dickt[f'вычетание {n} и {m}'] = n - m
    my_dickt[f'факториалы {n} и {m}'] = [factorial(n), factorial(m)]

    print(my_dickt)


def introspection_info(obj):
    info_dict = {}
    attribut = []
    metod = []
    info_dict['type'] = type(obj).__name__
    for i in list(dir(obj)):
        if i[0] == '_':
            metod.append(i)
        else:
            attribut.append(i)
    info_module = inspect.getmodule(introspection_info).__name__
    info_dict['attributes'] = list(attribut)
    info_dict['methods'] = list(metod)
    info_dict['module'] = info_module
    info_dict['size'] = sys.getsizeof(obj)

    print(info_dict)


introspection_info(43)
introspection_info(qwe)
introspection_info(introspection_info)