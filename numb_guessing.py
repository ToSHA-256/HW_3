import random
import hashlib

while True:
    max_num = ''
    while not max_num.isdigit():
        print('Введите число N до которого будет производиться розыгрыш:')
        max_num = input()
    max_num = int(max_num)
    rand_num = random.randint(1, max_num)
    hash_object = hashlib.md5(str(rand_num).encode())

    print(f'Система уже выбрала число! \n Вот его хеш: {hash_object.hexdigest()} \nПопробуешь угадать?')
    guess_num = ''
    while not guess_num.isdigit():
        print('Введи число:')
        guess_num = input()
    guess_num = int(guess_num)

    if guess_num == rand_num:
        print('Ты угадал!!!')
    else:
        print(f'Это фиаско, братан. Число {rand_num}. Можешь сверить md5 хеш если не веришь...')
