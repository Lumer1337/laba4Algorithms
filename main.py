
def Task1():  #-
    str = input()
    mas = []
    right = True
    for i in range(0, len(str)):
        if str[i] in '({[':
            mas.append(str[i])
        elif str[i] in ')}]':
            if len(mas) == 0:
                right = False
                break
            otcr_skobka = mas.pop()
            if otcr_skobka == '(' and str[i] != ')':
                right = False
                break
            if otcr_skobka == '{' and str[i] != '}':
                right = False
                break
            if otcr_skobka == '[' and str[i] != ']':
                right = False
                break
            right = True
    if right == True and len(mas) == 0:
        print("Скобки раставлены верно")
    else:
        print("Скобки раставлены неверно")
#+_____________________________________________________________________________________________________________________________
def Task2():
    stek = []
    Push(stek, 5)
    Push(stek, -8)
    Push(stek, 4)
    Push(stek, -2)
    Push(stek, -2)
    Push(stek, 9)
    print("Стек после работы функций push [5, -8, 4, -2, -2, 9]:")
    print(stek)
    print("Работа функции min:")
    print(Min(stek))
    Pop(stek)
    print("Стек после pop:")
    print(stek)
def Push(stek, k):
    stek.append(k)

def Pop(stek):
    if len(stek) > 0:
        stek.pop(len(stek) - 1)

def Min(stek):
    if len(stek) > 0:
        return min(stek)
# -______________________________________________________________________________________________________________________________________________________
def Task3():
    mas = [5, -2, 89, 2, 4, 4, 7, 9, -7]
    print(mas)
    k = 4
    mask = [-1] * k
    for i in range(0, k):
        mask[i] = mas[i]
    print ("Данное окно :", mask)
    print("Максимальное число в окне =",max(mask))
    for i in range(k, len(mas)):
        mask.pop(0)
        mask.append(mas[i])
        print("Данное окно :", mask)
        print("Максимальное число в окне =", max(mask))
# +______________________________________________________________________________________________________________________________________________________
def Task4():
    mas = [1, 2, 5, 3, 1, 2, 4]
    print(mas)
    print("Повторяющееся числa: ")

    for i in range(0, len(mas)):
        if mas[abs(mas[i])] > 0:
            mas[abs(mas[i])] = mas[abs(mas[i])] * -1
        else:
            print(abs(mas[i]))
# +______________________________________________________________________________________________________________________________________________________

def Task5():
    a = [5, -3, 10, -7, 2, 1]
    for i in range(0, len(a)):
        if a[i] < 0:
            a[i] = abs(a[i])
    return print("Наибольшее произведение из 3 чисел:", Large3(a, len(a)))

def Large3(arr, arr_size):

    first = second = third = -10000000000

    for i in range(0, arr_size):
        if (arr[i] > first):
            third = second
            second = first
            first = arr[i]
        elif (arr[i] > second):
            third = second
            second = arr[i]
        elif (arr[i] > third):
            third = arr[i]
    return first*second*third
# +______________________________________________________________________________________________________________________________________________________
def Task6():
    matrix = [[2, 1, 1],
              [5, 0, 4],
              [1, 3, 9],
              [3, 3, 1]]
    print("Исходная матрица:")
    print(matrix)
    stroki = [-1] * len(matrix[0])
    stolbcu = [-1] * len(matrix)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                stroki[j] = j
                stolbcu[i] = i
    for i in range(0, len(stolbcu)):
        for j in range(0, len(stroki)):
            if stolbcu[i] != -1 or stroki[j] != -1:
                matrix[i][j] = 0
    print("Результат:")
    print(matrix)
# _______________________________________________________________________________________________________________________________________________________
print("Задание 1:")
print("Введите строку:")
Task1()
print()
print("Задание 2:")
Task2()
print()
print("Задание 3:")
Task3()
print()
print("Задание 4:")
Task4()
print()
print("Задание 5:")
print(Task5())
print()
print("Задание 6:")
Task6()



