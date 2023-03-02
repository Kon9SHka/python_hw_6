#   Задача 32: Определить индексы элементов массива (списка), 
#   значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def check_parameters (array):
    array_2 = []
    for i in range (len(array)):
        if array[i] in range(7,11):                                     #array[i] in range(0,len(array)):
            array_2.append(i)
    return array_2

                                                                        #n = int(input("Введите размер массива: "))
array = [-5, 9, 0, 3, -1, -2, 1, 4,-2,10,2,0,-9,8,10,-9, 0, -5, -5, 7]  #[randint(-25,34) for _ in range(n)]

print(array)
print(check_parameters(array))

