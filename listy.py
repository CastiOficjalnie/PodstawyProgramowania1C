# listy a napisy
napis = "informatyka"
print(napis[2])

lista = []
for l in napis:
    lista.append(l)
print(lista)

lista = list(napis)  #zmiana stringa na liste
print(lista)

# zakres i lista
zakres = range(3, 10, 2)
# print(zakres)  zle!!!
print(list(zakres)) #dobrze

#indeksowanie elementow
lista2 = ['osa', 99, 3.14, [5, 7, 8, 9]]
print(lista2[1:3]) #wycinanie fragmentow listy
print(lista2[3][2]) #obslouga listy zagniezdzonej
print(lista2[3][::2])

# 4. powielanie listy
# dodawanie list
lista4 = ['a', 35, 70]
lista5 = [[4, 0], 56, 12]
lista6 = lista4 + lista5
print(lista6)
# dodawanie list 2
lista7 = ['a', 45, 70]
lista8 = [[4, 0], 56, 12]
lista7.extend(lista8)
print(lista7)

# 5. mnozenie listy przez liczbe
lista9 = [0] * 1000
print(lista9)
'''lista10 = [[0] * 10] * 10 #dana ilosc list
lista10[0][0] = 5
print(lista10)'''

'''# sortowanie i odwracani listy
lista10 = {4, -1, 0, 5, 2, 9, 3}
print(sorted(lista10))'''

#wyrazenia listowe(listy skladane)
lista11 = list(range(1, 11))
lista11_kwadraty = [x ** 2 for x in lista11 if x % 2 == 0]
print(lista11_kwadraty)

# usuwanie elementu na bazie jego wartosci:
lista12 = [4, 7, 4, 8, 2, 1]
while 4 in lista12:
    lista12.remove(4)
print(lista12)
#usuwanie elementu na bazie indeksu:
lista13 = [5, 1, 8, 3, 9, 10]
del.lista13[2] #usuwanie elementu o indeksie 2