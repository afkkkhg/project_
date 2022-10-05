def tk_1():
    n = int(input('Введите количество учеников: '))
    for i in range(0, n):
        print('Колледж Сириус')
        print('Имя: _____')
        print('Группа: ____')
    print('Готово! Заберите бейджики.')
    tk_1()

def tk_2():
    n = int(input('Введите количество ваших баллов: '))
    if 0 < n <= 49:
        print('Ваша скидка: 10%')
    if 50 < n <= 99:
        print('Ваша скидка: 15%')
    if n >= 100:
        print('Ваша скидка: 20%')


def tk_3():
    n = int(input('Введите количество учеников: '))
    for i in range(0, n):
        ans = int(input('Введите количество ваших баллов: '))
        if ans > 50:
            print('Вы допущены')
        else:
            print('Вы отчислены')
tk_3()


def count_imb(height, weight):
    return weight / (height ** 2)


def handle_imb():
    index = count_imb(height, weight)
    if index < 18.5:
        print('Недостаточный вес!')
    if 18.5 < index < 25:
        print('ИМТ в нормеф')
    else:
        print('Избыточный вес')

tk_4()

def tk_5():
    while True:
        key = input('Введите команду')
        if key == 'Стоп':
            break
        name = input('Введите число предметов: ')
        subject = int(input('Введите количество предметов: '))
        sum_c = 0
        for i in range(subject):
            point = int(input('Введите количество баллов: '))
            sum_c += point
        if sum_c > 80:
            print('Вы получили диплом')
        if 50 < sum_c <= 80:
            print('Вы получили похвальную грамоту')
        else:
            print('Вы получили грамоту об участии')

tk_5()

