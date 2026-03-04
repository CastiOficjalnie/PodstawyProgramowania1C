slowo = ('konstantynopolitanczykowianeczka')
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
nowe_slowo = ''.join(x for x in list(slowo) if x not in samogloski)
print(nowe_slowo)

plik = open('epstein', 'w')
ilosc = int(input('ile chcesz epstinow     '))

plik.write('epstein burger\n' * ilosc)