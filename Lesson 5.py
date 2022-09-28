number = []
while True:
    a = input()
    b = input()
    c = int(input())
    print('Следущий преподаватель?')
    d = input()
    number.insert(0, [a, b, c])
    if d == 'да':
        True
    else:
        break
print(number)

number = []
while True:
    a = int(input())
    b = number.count(5)
    c = number.count(4)
    d = number.count(3)
    v = len(number)
    if a != 0:
        number.append(a)
    else:
        break
print(((b + c + d + v) / v) * 100)

numb = []
while True:
    a = input()
    b = input()
    c = int(input())
    print('След. преподаватель ?')
    d = input()
    numb.insert(0, [a, b, c])
    if d == 'да':
        True
    else:
        break
print(numb)


strk = input()
d = dict()
for i in range(0, 10):
    d[i] = strk.count(str(i))
print(d)


s = dict()
while True:
    place = input()

    if place == "off":
        print(s)
        break
    else:
        place = int(place)
        print(s)



