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
przedzial = range(1, 10) #liczby od 1 do 9

for i in przedzial:
    print(i)

# petla ktora wykona sie 10 razy
# for i in range(10):
#     print(i)

'''lista5 = [5]
lista.append(0)
print(lista5)'''

lista = [0]

for i in lista:
    print('czesc')
    lista.append(0)

# 4. petla while

liczba = 5

while liczba > 0:
    print(liczba)
    liczba = liczba - 1

