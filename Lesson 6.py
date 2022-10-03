def task_1():
    dct = dict()
    # создаем словарь и заполняем его числами от 1 до 10 в качестве ключей, а в качестве значений их квадраты
    for i in range(1, 11):
        dct[i] = i ** 2
    return dct


print(task_1())


def task_2():
    dct = dict()
    numbers = "0139412831055230677798"
    # создаем словарь в который сохраняем под ключом цифру , а под значением количество этой цифры в строке
    for i in range(1, 10):
        dct[i] = numbers.count(str(i))
    return dct


print(task_2())


def task_3():
    dct = dict()
    # создаем словарь
    while True:
        # создаем бесконечный цикл если пользователь ввел off завершаем, иначе сохраняем его ввод и выводим в формате место певец и его имя 
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
    # идём по ключам и значения в словаре
    for key, value in dct.items():
        #идем по списку значений в значенях
        for name in value:
            # сохраняем и выводим домен и имя пользователя
            s = name + '@' + key
            print(s)


task_5(emails)

4

dictionary = {'1':1,'2':2,'3':3,'4':4,'5':5}
dictionary['1'],dictionary['5'] = dictionary['5'],dictionary['1']
del dictionary['2']
dictionary['new_key'] = 'new_value'
print(dictionary)

