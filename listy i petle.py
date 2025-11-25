# jak nie powtarzac wiele razy tego samego

# x = float(input('podaj liczbe'))
# y = float(input('podaj liczbe'))
# z = float(input('podaj liczbe'))
# k = float(input('podaj liczbe'))
# l = float(input('podaj liczbe'))
#
# suma = (x + y + z + k + l)

# print(suma)'''

# liczba = 0
# suma = 0
#
# # for i in range(5):
#     liczba = float(input('podaj liczbe '))
#     suma = suma + liczba

# print(suma)

# 1. listy
lista = ['qwerty', 56, [6, 7], 4.56, [[5,8], 1]]
print(lista[2][1])
print(lista[4][0][1])

# 2. listy i petle
lista2 = ['kot', 'pies', 'owca', 'lama']

for z in lista2:
    print(z)
# pętla for:
# -> wyciaga dane z listy (jedna po drugiej)
# -> wykonuje sie tyle razy ile elementow ma lista

# petla ktora wykona sie 3 razy
lista3 = [1410, 15 ,7]
for g in lista3:
    print('OK')

# petla ktora wykona sie 1000 razy
lista4 = [0] * 1000

for i in lista4:
    print('czesc')

# 3. generatory i petle
# przedzial = range(1, 10) #liczby od 1 do 9
#
# for i in przedzial:
#     print(i)

# petla ktora wykona sie 10 razy
# for i in range(10):
#     print(i)

'''lista5 = [5]
lista.append(0)
print(lista5)'''

# lista = [0]
#
# for i in lista:
#     print('czesc')
#     lista.append(0)

# 4. petla while

# liczba = 5
#
# while liczba > 0:
#     print(liczba)
#     liczba = liczba - 1

'''X = list(range(0, 103, 3))
print(f'x\ty')
for x in X:
    y = 0.5 * x + 3
    # print(x, y)
    print(f'{x}\t{y}')'''

X = list(range(-30, 61, 1))
print(f'x\ty')
for x in range(-30, 61):
    x = x / 10
    y = 0.5 * x + 3
    # print(x, y)
    print(f'{x}\t{y}\n')

# zadanie 67

lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))

print(f'x\ty\tz')

# sposob 1
'''for x, y, z in zip(lista1, lista2, lista3):
    print(f'{x}\t{y}\t{z}')'''

# sposob 2
for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')
