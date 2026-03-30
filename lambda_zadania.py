'''lista = {4, 10, 12, 9, 5}
# krotka - lista w nawiasach okraglych
potegi = [(x, x ** 2, x ** 3, x ** 4) for x in lista]
print(potegi)


potegi_map = list(map(lambda x: (x, x ** 2, x ** 3, x ** 4), lista))
print(potegi_map)'''


'''lista_dat = ['20241101', '20231223', '20220711', '20230503']
slownik_dat = list(map(lambda x: {'rok': int(x[:4], 'miesiac': int(x[4:6], 'dzien': int(x[6:])}, lista))'''

# zadanie 2
class Galeria:
    def __init__(self, kraj, miasto, lokale_handlowe):
        initkraj = kraj
        init_miasto = miasto
        init_lokale_handlowe = lokale_handlowe
g1 = Galeria(kraj='PL', miasto='gdansk', lokale_handlowe=[(4, 6), (6, 10), (11, 9)])

print(g1,kraj, g1,miasto, g1,lokale_handlowe)

