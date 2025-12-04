'''for i in range(1, 21):
    for j in range(1, 21):
        print(i * j, end = '\t')
    print()'''

# choineczka
'''n = int(input('podaj wysokosc trojkata: '))
for x in range(n):
    for y in range(x + 1):
        print('*', end = '')
    print()

n = int(input('wysokosc trojkata: '))
for x in range(n):
    print('*' * (x + 1))'''

#trojkat rownoramienny dowolny
n = int(input('podaj wysokosc trojkata: '))
spacja = n - 1
gwiazdki = 1
for i in range(n):
    print(' ' * spacja, end = '')
    print('*' * gwiazdki)
    spacja = spacja - 1
    gwiazdki = gwiazdki + 2
