# petla while - przyklady

liczba = 147573952589676412928
licznik = 0

while liczba > 1:
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)

# zadanie 1.

'''x = input('podaj liczbe lub q aby zakonczyc ')
licznik = 0
while x != 'q':
    liczba = float(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('podaj liczbe lub q aby zakonczyc ')
print(licznik)'''

# zadanie 2
popr_haslo = 'informatyka'
haslo = input('podaj haslo:')
proba = 1
while haslo != popr_haslo and proba < 5:
    print('bledne haslo')
    haslo = input('podaj haslo: ')
    proba = proba + 1
if haslo == popr_haslo:
    print('witaj w systemie')
else:
    print('nie ma hasla - nie ma systemu')

#zadanie 3, zadanie 4
