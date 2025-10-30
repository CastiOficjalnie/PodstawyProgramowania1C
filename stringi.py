from zmienne import liczba_calkowita

napis = 'informatyka'

# fragment tekstu
# 1) wycinanie od ..... do
print(napis[2:5]) #czyli tak naprawde od 2 do 4

    # 2) wycinanie od....do co iles
print(napis[2:10:2])

    # 3) wycinanie od poczatku
print(napis[:3])

    # 4) wycinanie od konca
print(napis[7:])

    # 5) czytanie od konca
print(napis[::-1])
# II) zawieranie sie znaku w slowie
if 'a' in napis:
    print('należy')
else:
    print('nie nalezy')

# III. Laczenie napiso(konkatenacja)
napis2 = napis + 'jestnajlepsza'
print(napis2)

# IV. funkcje zmiennych typu string

    # 1. poszukiwanie danego fragmentu w tekscie

napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
index_gdzie_jest4 = napis4.find('xyz', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz nie jest w napisie')
else:
    print('xyz nie jest w napisie')

# 2. podzial tekstu na fragmenty
# piec_liczb = input('podaj piec liczb. oddziel je przecinkiem ')
# piec_liczb_po_podziale =  piec_liczb.split(',')
# print(piec_liczb_po_podziale)
# trzecia_liczba = piec_liczb_po_podziale[2]
# print(trzecia_liczba + 33)

# 3. laczenie napisow
lista_napisow = ['windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie2)

# 4. liczenie danego znaku w tekscie
napis5 = 'prawdopodobienstwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)