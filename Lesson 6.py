def task_1():
    dct = dict()
    for i in range(1, 11):
        dct[i] = i ** 2
    return dct


print(task_1())


def task_2():
    dct = dict()
    numbers = "0139412831055230677798"
    for i in range(1, 10):
        dct[i] = numbers.count(str(i))
    return dct


print(task_2())


def task_3():
    dct = dict()
    while True:
        command = input('Введите задачу: ')
        place = input('Введите место: ')
        singer = input('Введите певца: ')
        name = input('Введите песню: ')
        if command == 'off':
            break
        else:
            dct[(place, singer)] = name
            print(dct)


task_3()

emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
          'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
          'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
          'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
          'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
          'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}


def task_5(dct):
    for key, value in dct.items():
        for name in value:
            s = name + '@' + key
            print(s)


task_5(emails)