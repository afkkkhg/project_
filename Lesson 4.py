meal = input('Прием пищи:')
if meal =='Завтрак':
    print('Каша')
elif meal == 'Обед' or 'Ужин':
    xyu = input('Ты хочешь плотно поесть ?')
    if xyu == 'да':
        print('Плов')
    else:
        print('Пюре с котлетой')



#time = int (input('Введите время(час): '))
#price = int (input('Введите стоимость: '))
if time >=8 and time <= 22:
    if time >= 10 and time <= 12:
        price = price//2
    elif time >= 20 and time <= 22:
        price = price//4
else: print('Магазин закрыт')
print('Вам нужно оплатить: ', price)

a = int(input())
b = int(input())
c = int(input())
d = a + b + c
if b > a and c > b:
    print('Акция', d // 2)
elif a > b and b > a:
    print('Акция', d // 3)
else:
    print('К оплате:', d)
