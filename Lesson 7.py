def tk_1():
    # создаем строку, куда сохраняем количество учеников и печатаем количество карточек на них
    n = int(input('Введите количество учеников: '))
    for i in range(0, n):
        print('Колледж Сириус')
        print('Имя: _____')
        print('Группа: ____')
    print('Готово! Заберите бейджики.')


# tk_1()

def tk_2():
    # считаем скидку по баллам
    n = int(input('Введите количество ваших баллов: '))
    if 0 < n <= 49:
        print('Ваша скидка: 10%')
    if 50 < n <= 99:
        print('Ваша скидка: 15%')
    if n >= 100:
        print('Ваша скидка: 20%')


def tk_3():
    n = int(input('Введите количество учеников: '))
    # считываем количество учеников и  спрашиваем количество баллов , если количество баллов меньше указаного выводим Отчислены иначе Допущены
    for i in range(0, n):
        ans = int(input('Введите количество ваших баллов: '))
        if ans > 50:
            #если больше 50, то допущен
            print('Вы допущены')
        else:
            #если меньше 50, то отчислены
            print('Вы отчислены')


tk_3()
