plik = open('dane.txt')
wazne_slowo = plik.read()
print(wazne_slowo)

plik2 = open('dane2.txt')
dane2 = plik2.readlines()

for i in range(len(dane2)):
    dane2[i] = int(dane2[i])
print(dane2)

plik3 = open('dane3.txt')
dane3 = plik3.readlines()

for i in range(len(dane3)):
    dane3[i] = dane3[i].strip()

print(' '.join(dane3))

plik4 = open('dane4.txt')
dane4 = plik4.readlines()

for i in range(len(dane4)):
    dane4[i] = dane4[i].split()

print(dane4)

plik5 = open('dane5.txt')
dane5 = plik5.readlines()

'''for i in range(len(dane5)):
    dane5[i] = dane5[i].strip()
    for j in range(len(dane5[i])):
        dane5[i][j] = int(dane5[i][j])'''

dane5_prim = [list(map(int, x.split()))for x in open('dane5.txt')]
print(dane5_prim)