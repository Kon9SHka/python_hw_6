# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб количество элементов было четное. 
# Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, 
# причем чтобы каждый гарантированно и только один раз переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.
# from random import randint
from random import randint

def fill_array (cnt_line, cnt_column):
    array = [0]*cnt_line

    for i in range (cnt_line):       
        
        array[i]= [randint(0,35) for _ in range (cnt_column)]    
        print(array[i])
        
    return array

def list_for_index (array):
    array_for_index=[]
    for i in range (len(array)):
        for j in range (len(array[i])):
            array_for_index.append([i,j])
    return array_for_index

def change_places (array,index_array):
    cnt_iteration = int(len(index_array)/2)
    
    for i in range(cnt_iteration):
        
        first_place = index_array.pop(randint(0,len(index_array)-1))
        second_place = index_array.pop(randint(0,len(index_array)-1))
        
        temp_place = array[first_place[0]][first_place[1]]
        
        array[first_place[0]][first_place[1]] = array[second_place[0]][second_place[1]]
        array[second_place[0]][second_place[1]] = temp_place
        
    return array
        
            
    

cnt_line = int(input("Введите кол-во строк: "))
cnt_column = int(input("Введите кол-во столбцов: "))

array = fill_array(cnt_line,cnt_column)
index_array = list_for_index(array)

array = change_places(array, index_array)

print()

for i in range(len(array)):
    print(array[i])
    
# print(index_array)
# print(len(index_array))
# first_place = index_array.pop(randint(0,len(index_array)-1))
# print(first_place)
# print(index_array)
# print(len(index_array))
# second_place = index_array.pop(randint(0,len(index_array)-1))
# print(second_place)
# print(index_array)
# print(len(index_array))


#print(array[index_array[0][0]][index_array[0][1]])
#array[index_array[0][0]][index_array[0][1]]


