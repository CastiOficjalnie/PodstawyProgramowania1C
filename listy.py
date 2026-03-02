# listy a napisy
'''napis = "informatyka"
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

# sortowanie i odwracani listy
lista10 = {4, -1, 0, 5, 2, 9, 3}
print(sorted(lista10))

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
del.lista13[2]'''


# zadanie 1.
lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'sledz', 'pstrag']]
'''print(lista2[1][2])
print(list(lista2[3]))
print(lista1[2::3])
lista3 = lista2[1] * 3
print(lista3)
lista4 = lista2 + [lista3]
print(lista4)'''

'''lista3 = [9, 6, 16, -8, 7]
print(lista1 + lista3)'''

print(sorted(lista1))

print(f'najmniejsza liczba - {min(lista1)}\nnajwieksza liczba - {max(lista1)}')

'''del lista1[4]
print(lista1)'''

'''del lista1[4:9]
print(lista1)'''

'''while 2 in lista1:
    lista1.remove(2)
print(lista1)'''

'''lista3 = [x ** 2for x in lista1]
print(lista3)'''

'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

lista_norm = [(x - min(lista)) / (max(lista) - min(lista)) for x in lista]
print(lista_norm)'''

'''lista = [123, 89, 5600, 432, 11, 45, 900, 12450, 1410, 390, 9999]

cztery_cyfry = [[] for x in lista if x > 999 and x < 10000 else x]
print(cztery_cyfry)'''

inwokacja = 'LITWOOJCZYZNOMOJATYJESTESZJAKZDROWIEILECIETRZEBACENICTENTYLKOSIEDOWIEKTOCIESTRACILDZISPIEKNOSCTWACALEJOZDOBIEWIDZEIOPISUJEBOTESKNIEPOTOBIEPANNOSWIETACOJASNEJBRONISZCZESTOCHOWYIOSTREJSWIECISZBRAMIETYCOGRODZAMKOWYNOWOGRODZKIOCHRANIASZZJEGOWIERNMLUDEMJAKMNIEDZIECKODOZDROWIAPOWROCILASCUDYMGDYODPLACZACEJMATKIPODTWOJAOPIEKEOFIAROWANYMARTWAPODNIOSELMOJEPOWIEKEIZARAZMOGLEMPIESZODOTWYCZSWIATYNPROGUISTZAWROCONEZYCIEPODZIEKOWACBOGUTAKNASPOWROCISCUDYMNADOJCZYZNYLONOTYMCZASEMPRENOSMOJADUSZEUTESKNIONADOTYCHPAGORKOWLESNYCHDOTYCHLAKZIELONYCHSZEROKONADBLEKITNYMNIEMNEMROZCIAGNIONYCHDOTYCHPOLMALOWANYCHZBOZEMROZMAITEMWYZLACANYCHPSZENICAPOSREBRZANYCHZYTEMGDZIEBURSZTYNOWYSWIERZOPGRYKAJAKSNIEGBIALAGDZIEPANIENSKIMRUMIENCEMDZIECIELINAPALAAWSZYSTKOPRZEPASANEJAKBYWSTEGAMIEDZAZIELONANANIJZZADKACICHEGRUSZESIEDZA'

lista = list(inwokacja)

suma = 0


for x in lista:
    suma = suma + ord(x)

print(suma)

x = map(ord, list(inwokacja))

print(x)

