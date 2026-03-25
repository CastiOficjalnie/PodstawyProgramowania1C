'''Dodawanie = lambda x, y: x + y
print(Dodawanie(3, 5))
#                                   robia to samo
def dodwanie(x, y):
    return(x + y)
print(dodwanie(3, 5))

lista = ['abba', 'bcca', 'ghaaaaa', 'khaa']

lista.sort(key = lambda x: x.count('a'))
print(lista)'''
from traceback import print_tb

# zaawansowane sortowanie
'''lista = [6, -9, 3, 0, -12, -1, 7]

# 1) sortowanie po wartosci bezwzglednej
lista.sort(key = lambda x: abs(x))       #abs = wartosc bezwzgledna
print(lista)'''

# 2) sortowanie po dlugosciach napisow
lista2 = ['matematyka', 'filozofia', 'fizyka', 'informatyka']
lista2.sort(key = lambda x: -len(x))
print(lista2)

# 3) sortowanie wielopoziomowe
ludzie = [['Janusz', 'Baca'], ['Bartlomiej', 'Kaca'], ['Janusz', 'Aca'], ['Bartlomiej', "Gaca"]]
ludzie.sort(key = lambda x: (x[0], x[1]))
print(ludzie)

# 4) sortowanie po liczbie dzielnikow
def ile_dzielnikow(x):
    ile = 0
    for r in range(1, x + 1):
        if x % r == 0:
            ile += 1
    return ile

lista3 = [12, 7, 1024, 9, 16]
lista3.sort(key = lambda x: ile_dzielnikow(x))
print(lista3)

# 2. Zaawansowane użycie funkcji map
# 1) proste mapowanie
lista4 = [1, 5, -6, 10, -7]
nowa = list(map(lambda x: x ** 2, lista4))
print(nowa)

# 2) zaawansowane mapowanie
slownik = {'fiz': 'fizyka', 'mat': 'matematyka', 'inf': 'informatyka'}
lista = ['fiz', 'jest', 'najlepsza', 'ale', 'inf', 'tez', 'jednak', 'nic', 'nie', 'zastapi', 'mat']

lista5 = list(map(lambda x: slownik[x] if x in slownik else x, lista))
print(lista5)