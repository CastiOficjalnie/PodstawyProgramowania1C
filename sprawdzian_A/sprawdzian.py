'''plik = open('prostokaty.txt')
dane = plik.readlines()

prostokaty = []

for w in dane:
    para = w.split()
    prostokat = list(map(int, para))
    prostokaty.append(prostokat)
pola = [a * b for a, b in prostokaty]

pola_mm = f'najwieksze pole = {max(pola)}, najmniejsze pole = {min(pola)}'

print(pola_mm)

obwody = [2 * a + 2 * b for a, b in prostokaty]
ile_roznych = len(set(obwody))
print(ile_roznych)'''