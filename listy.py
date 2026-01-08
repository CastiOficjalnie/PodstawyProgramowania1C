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
lista10 = [[0] * 10] * 10 #dana ilosc list
lista10[0][0] = 5
print(lista10)