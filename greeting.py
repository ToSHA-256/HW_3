while True:
    name = ''
    age = ''
    flag = False
    while not len(name) > 0:
        print('Как Вас зовут?')
        name = input()

        while not flag == True:
            print('Сколько Вам лет?')
            age = input()
            if age.isdigit() and int(age) > 0:
                flag = True
            else:
                print('Ошибка, повторите ввод')
    age = int(age)
    if age < 10:
        print('Привет, шкет {}'.format(name))
    elif age <= 18:
        print(f'Как жизнь, {name}')
    elif age > 100:
        print(name + ', вы лжёте - в нашей стране столько не живут=)')
    else:
        print(f'Как жизнь, {name}')

