#1 в процессе

import random
a = int(input('Число участников'))
b = random.randint(1, a)
c = random.randint(1, a)
print('Пловец', b, '-', 'Пловец', c)

from time import *

#3 тоже самое, что и с 1

print('Удалить с поля?')
seconds = int(input('Введите количество секунд (2 или 10): '))
if (seconds == 2) or (seconds == 10):
    print('Вы удалены с поля на "seconds" секунд')
    sleep(seconds)
    print('Возвращайтесь на поле!')
    

from time import *
from random import *

print('Подбрасываю кубики')
sleep(2)
print(randint(1,6), randint(1,6))