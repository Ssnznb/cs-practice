#1й коммит - сложение
a, b = int(input('a: ')), int(input('b: '))
print(a+b)

#2й коммит - вычитание
print(a-b)

#3й коммит - умножение
print(a*b)

#4й коммит - деление с проверкой нуля
if b != 0:
    print(a/b)
else:
    print('b is zero')