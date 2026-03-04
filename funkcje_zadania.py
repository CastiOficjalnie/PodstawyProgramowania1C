# zadanie 0.3
# a)
def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w
u = [2, 7, 3]
v = [-1, 0, 4]
wynik = suma_v(u, v)
print(wynik)

def iloczyn_v(u, v):
    n = []
    for x in range(len(u)):
        iloczyn = v[x] * u[x]
        n.append(iloczyn)
    return sum(n)

# zdanie 2.1
def czy_anagramy(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = 'nosek'
s2 = 'keson'
print(sorted(s1) == sorted(s2))

# 2.2
def rodzaj_trojkata(a, b, c):
    if a ** 2 + b ** 2 + c ** 2 == 2 * max([a, b, c]):
        print('prostokatny')
    elif a ** 2 + b ** 2 + c ** 2 > 2 * max([a, b, c]):
        print('ostrokatny')
    elif a ** 2 + b ** 2 + c ** 2 < 2 * max([a, b, c]):
        print('rozwartokatny')
rodzaj_trojkata(13, 5, 12)


slowo = ('konstantynopolitanczykowianeczka')

def liczby_niezalezne(lista):
    wynik = []
    for e in lista:
        dzielniki = []
        for l in lista:
            if e % l == 0:
                dzielniki.append(l)
        if len(dzielniki) == 1:
            wynik.append(e)
    return wynik
print(liczby_niezalezne([12, 7, 3, 6, 21, 74 ]))

# dom(4, 5, 6, 7, 8)