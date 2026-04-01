'''lista = {4, 10, 12, 9, 5}
# krotka - lista w nawiasach okraglych
potegi = [(x, x ** 2, x ** 3, x ** 4) for x in lista]
print(potegi)


potegi_map = list(map(lambda x: (x, x ** 2, x ** 3, x ** 4), lista))
print(potegi_map)'''


'''lista_dat = ['20241101', '20231223', '20220711', '20230503']
slownik_dat = list(map(lambda x: {'rok': int(x[:4], 'miesiac': int(x[4:6], 'dzien': int(x[6:])}, lista))'''

# zadanie 2
'''class Galeria:
    def __init__(self, kraj, miasto, lokale_handlowe):
        __init__kra3j = kraj
        __init__miasto = miasto
        __init__lokale_handlowe = lokale_handlowe
g1 = Galeria(kraj='PL', miasto='gdansk', lokale_handlowe=[(4, 6), (6, 10), (11, 9)])
print(g1,kraj, g1,miasto, g1,lokale_handlowe)

plik = open(dane.txt)
dane = plik.readlines()
galerie = []
for x in dane:
    x = x.split()
    kraj = x[0]
    miasto = x[1]
    lokale_handlowe = [(int(d), int(s) for d, s in zip(x[2::2], x[3::2])]
    galerie.append()
    pass
    
for g in galerie:
    print(g.kraj, g.miasto, g.lokale_handlowe)

galerie_sort = list(sorted(galerie, key = lambda x: x.miasto))
for g in galerie_sort:
    print(g.kraj, g.miasto, g.lokale_handlowe)

# zadanie 3
# sortowanie listy galerii wedlug pola powierzchni pierwszego lokalu

galerie.sort2 = list(sorted(galerie, key = lambda x: x.lokale_handlowe[0][0] * lokale_handlowe[0][1]))'''
def powierzchnia_galerii(galeria):
    lista_lokali = galeria.lokale_handlowe
    suma = 0
    for p in lista_lokali:
        pole = p[0] * p[1]
        suma += pole
    return sum(pole)
galerie_sort_powierzhcnia = list(sorted(galerie, key = lambda x: powierzchnia_galerii(x)))

