# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n=int(input('Введите количество элементов первого множества: '))
m=int(input('Введите количество элементов второго множества: '))

list1=[]
list2=[]

print('Ввод первого набора.')
for i in range(n):
    list1.append(int(input(f'Введите элемент {i}: ')))

print('Ввод второго набора.')
for i in range(m):
    list2.append(int(input(f'Введите элемент {i}: ')))

print('Введены наборы:')
print(list1)
print(list2)

set1=set(list1)
set2=set(list2)

resultSet=set1.intersection(set2)
resultList=list(resultSet)

for i in range(len(resultList)): #сортировка списка
    for j in range(len(resultList)-1-i):
        if(resultList[j]>resultList[j+1]):
            buf=resultList[j]
            resultList[j]=resultList[j+1]
            resultList[j+1]=buf

print(f'Результат: {resultList}')