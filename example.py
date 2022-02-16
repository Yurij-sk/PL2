#Задачи на циклы и оператор условия------
#----------------------------------------

print('Задача 1')
print('Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')
print()
print('Решение:')
for i in range(1, 6):
    print(i, '0')
print('--------------------')


print('Задача 2')
print('Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.')
'''
    Это оказалась самая трудная задача, потому что я решил ограничить пользователя
вводить: только число, только целое, только в заданном диапазоне.
    В уроках многое опускается, например, что input выводит только str.
Я из-за этого вообще ничего понять не мог - вчера весь вечер просидел над этим.
Сегодня гуглил и как-то случайно нашёл про это.
    В итоге нашёл и алгоритм, который может отследить, что за число вводится,
но так как я его пока вообще не понял, решил сюда не вставлять.
    А так, в целом, очень занимательная штука)))
'''
print()
print('Решение:')
a = 0
for i in range(10):
    b = int(input('Введите целое число от 0 до 100: '))
    if b < 0 or b > 100:
        print('Вне диапазона.')
    else:
        print('Принято. Дальше.')
    if b == 5:
        a += 1
print(a)
print('--------------------')


print('Задача 3')
print('Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')
print('')
print('Решение:')
sum = 0
for i in range(1,101):
    sum+=i
print(sum)
print('--------------------')


print('Задача 4')
print('Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.')
print('')
print('Решение:')
m = 1
for i in range(1,11):
    m = m * i
print(m)
print('--------------------')


print('Задача 5')
print('Вывести цифры числа на каждой строчке.')
print('')
print('Решение:')
integer_number = 2129
print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10
print('--------------------')


print('Задача 6')
print('Найти сумму цифр числа.')
print('')
print('Решение:')
a = 0
integer_number = int(input('Введите любое целое число: '))
while integer_number>0:
    a += integer_number%10
    integer_number = integer_number//10
print(a)
print('--------------------')


print('Задача 7')
print('Найти произведение цифр числа.')
print('')
print('Решение:')
m = 1
integer_number = int(input('Введите любое целое число: '))
while integer_number>0:
    m = m * (integer_number%10)
    integer_number = integer_number//10
print(m)
print('--------------------')


print('Задача 8')
print('Дать ответ на вопрос: есть ли среди цифр числа 5?')
print('')
print('Решение:')
integer_number = int(input('Введите любое целое число: '))
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
print('--------------------')


print('Задача 9')
print('Найти максимальную цифру в числе.')
print('')
print('Решение:')
integer_number = int(input('Введите любое целое число: '))
m = 0
while integer_number>0:
    if integer_number%10 > m:
        m = integer_number%10
    integer_number = integer_number//10
print('Mmaximum digit =', m)
print('--------------------')


print('Задача 10')
print('Найти количество цифр 5 в числе.')
print('')
print('Решение:')
i = int(input('Введите любое целое число: '))
a = 0
while i > 0:
    if i%10 == 5:
        a += 1
    i = i // 10
print(a)
print('--------------------')