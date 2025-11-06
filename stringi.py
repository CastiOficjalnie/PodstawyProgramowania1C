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

# 5. mutowalnosc stringow
napis6 = "fiwyka"
# napis6[2] = 'z'
# print(napis6)
# stringi sa niemutowalne, czyli nie mozna podmieniac pojednyczych liter

# sposob na zmutowanie stringa
napis6_lista = list(napis6)
napis6_lista[2] = 'z'
print(napis6_lista)
napis6_gotowy = ''.join(napis6_lista)
print(napis6_gotowy)

# 6. funckja len

napis7 = 'jezykpolski'
print(len(napis7))

# 7. powielanie stringa
napis8 = 'informatyka'
print(napis * 3)

# 8. funkcje testujace cyfry i litery
napis9 = 'qwerty'
if napis9.isalpha() == True:
    print('sklada sie z liter')
else:
    print('slowo nie sklada sie z liter')

napis10 = '1410w'
if napis10.isdigit() == True:
    print('slowo sklada sie tylko z cyfr')
else:
    print('slowo sklada sie nie tylko z cyfr')

napis11 = '1410w'
# if napis11.isalnum() == True:





# 9.kody ASCII

# 9.1. ze znaku na kod ASCII
print(ord("A"))

# 9.2 z kodu ASCII na znak
print(chr(66))

 # 10. funkcje

# funkcja translate
slownik = str.maketrans('ąęćóżśźłń', "aecozszln")
napis12 = 'infórmątyką'
napis12_poprawny = napis12.translate(slownik)
print(napis12_poprawny)

# 10.2 funkcje duzych i malych literek
napis13 = 'KoNGo'
napis13_tylko_duze = napis13.upper()
print(napis13_tylko_duze)

# 11.podstawianie ciagu znakow
napis14 = 'chleb kosztuje 15 zl a bulka 5 zl'
napis14_w_euro = napis14.replace('zl', '€')
print(napis14_w_euro)

# 12. sortowanie i odwracanie napisow
# 12.1 odwracanie
napis15 = "kemot"
napis15_odwrotnie = napis15[::-1]

# 12.2 sortowanie napisow
napis16 = 'dbca'
napis16_posortowany_lista = sorted(napis16)
napis16_posortowany_ciag = ''.join(napis16_posortowany_lista)
print(napis16_posortowany_ciag)