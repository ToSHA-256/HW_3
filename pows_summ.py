from datetime import datetime
import time


def pow_2_cub_fast(n):  #Считаем сумму и возводим в квадрат
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum ** 2


def pow_2_cub_slow(n):  #Возводим в куб и считаем сумму
    sum = 0
    for i in range(n + 1):
        sum += i ** 3
    return sum

def pow_2_cub_while(n):
    sum = 0
    i=1
    while i < n+1:
        sum += i
        i+=1
    return sum**2

while True:
    num = ''
    while not num.isdigit():
        print('Введите БОЛЬШОЕ натуральное число (8-ми значное например): ')
        num = input()

    num = int(num)
    start_time = datetime.now()

    print(f'Сумма кубов: {pow_2_cub_fast(num)}')
    print(f'Время быстрый: {datetime.now() - start_time}')
    

    start_time = datetime.now()
    print(f'Сумма кубов: {pow_2_cub_slow(num)}')
    print(f'Время медленный: {datetime.now() - start_time}')

    print(f'While: {pow_2_cub_while(num)}')