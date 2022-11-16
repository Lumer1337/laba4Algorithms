def Task1():
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

# Реализуйте «вручную» стек со стандартными функциями push/pop и
# дополнительной функцией min, возвращающей минимальный элемент стека. Все
# эти функции должны работать за O(1). Память должна быть оптимальна.

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


# _______________________________________________________________________________________________________________________________________________________
def Task3():
    mas = [5, -2, 89, 2, 4, 4, 7, 9, -7]
    print(mas)
    k = 4
    mask = [0] * k

    for i in range(0, k):
        mask[i] = mas[i]
    print(max(mask))
    for i in range(3, len(mas)):
        mask.pop(0)
        mask.append(mas[i])
        print(max(mask))

# _______________________________________________________________________________________________________________________________________________________
def Task4():
    mas = [4, 1, 5, 2, 1, 2, 3]    #n = 6  числа от 1 до 6
    print(mas)

    for i in range(0, len(mas)):
        if mas[abs(mas[i])] > 0:
            mas[abs(mas[i])] = mas[abs(mas[i])] * -1
        else:
            print(abs(mas[i]))

# _______________________________________________________________________________________________________________________________________________________
def Task5():
    mas = [4, 7, -10, 15, -2]
    print(mas)
    merge_sort(mas)
    max_minus = -100000
    max_plus = -100000
    if len(mas) < 3:
        return "Ошибка"
    elif len(mas) == 3:
        return mas[0] * mas[1] * mas[2]
    else:
        if (mas[0] < 0 and mas[1] < 0):
            max_minus = mas[0] * mas[1] * mas[len(mas) - 1]
            max_plus = mas[len(mas) - 3] * mas[len(mas) - 2] * mas[len(mas) - 1]
            if max_minus > max_plus:
                return max_minus
            else:
                return max_plus
        max_plus = mas[len(mas) - 3] * mas[len(mas) - 2] * mas[len(mas) - 1]
        return max_plus

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array

# _______________________________________________________________________________________________________________________________________________________
def Task6():
    matrix = [[1, 6, 3],
              [-5, 4, 0],
              [2, 5, 8],
              [8, 9, 14]]
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

print("Задание 2:")
Task2()

print("Задание 3:")
Task3()

print("Задание 4:")
Task4()

print("Задание 5:")
print(Task5())

print("Задание 6:")
Task6()



