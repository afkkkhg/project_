number = int(input('Введите значение'))


def tk_1():
    d = {'Олег':33,'Кирилл':22}
    d['Антон'] = 27
    (d.values)
    print(sum(d.values()))

def tk_2():
    day = {'Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье'}
    for

      def task_7(s):
            lst = list()
            count = 0
            for letter in s:
                if letter == '(':
                    lst.append(letter)
                if letter == ')':
                    lst.pop()
                    count += 2
            return count

        print(task_7('(()()'))


def task_8(string):
    s = ''
    lst = list()
    for letter in string:
        if letter in lst:
            continue
        else:
            lst.append(letter)
            dig = string.count(letter)
            s += str(dig) + letter

    return s


print(task_8('AAAABBBCC'))

