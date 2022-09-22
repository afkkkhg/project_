'''
a = '456 7899'
print(a[::-1])

a = '765 3409'
b = a.split()
print(b)
new_str = str(b[1])+" "+ str(b[0])
print(new_str)
'''

a = 'abc'
b ='mng'
print(a+b)

a = 'r'
print(a*50)

a = '5678'
print(a[::-1])

a = '9898 098'
c = a.split()
print(c[1]+" "+c[0])

a = 'pfpfp@mail.ru'
c = a.split('@')
print(c[0])

a = '+79535940775'
print(a[2:5])

a = 'Гагарин Юрий Алексеевич'
c = a.split()
print(c[0]+" "+c[1][0:1]+"."+c[2][0:1]+".")

a = 'Экономический рост тесно связан с ростом общего благостояния.'
c = a.split()
print(c[0][0:6]+". "+c[1]+" "+c[2]+" "+c[3]+" "+c[4]+" "+c[5]+" "+c[6]+" "+c[7])

a = '+7 (812) 134-12-324'
import string
for sym in string.punctuation:
    a= a.replace(sym,'')
a = a.replace(' ','')
print('+'+a)
