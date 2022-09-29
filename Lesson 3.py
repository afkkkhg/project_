def task_1():
    str_1 = input('Введите ваше музыкальное предпочтение: ')
    print('Предпочтение учтено! ')
    str_2 = input('Введите ваше музыкальное предпочтение: ')
    print('Предпочтение учтено! ')
    str_3 = input('Введите ваше музыкальное предпочтение: ')
    print('Предпочтение учтено! ')
    print('Система рекомендаций настроена! ')

#
# task_1()


def task_2():
    while True:
        str_1 = input('Введите команду: ')
        if str_1 == 'off':
            break
        if str_1 == 'game':
            k = 0
            while k < 3:
                str_2 = int(input('Введите целое число '))
                if str_2 == 5:
                    print("Вы выиграли билет на концерт")
                    break
                else:
                    k += 1
                    continue


def task_3():
    str_1 = input('Введите ваш пароль')
    for letter in str_1:
        if letter in '=?^$№@_ ':
            print('Запрещенный символ - %s' % letter)


def task_4():
    while True:
        str_1 = input('Введите отзыв: ')
        if str_1 == 'off':
            print('Система предпочтений настроена!')
            break
        else:
            print('Спасибо за ваш отзыв! ')


def task_5():
    while True:
        number = int(input('Введите целое число: '))
        if number == 0:
            break
        else:
            print('Число до скидки %d', number)
            print('Число после скидки %d', number * 0.5)
task_5()




