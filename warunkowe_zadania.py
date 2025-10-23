#rozwiazywanie rownania kwadratowegp

a = float(input('podaj liczne różną od 0 '))
b = float(input('podaj liczbe b '))
c = float(input('podaj liczbe c '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1}, v x2 = {x2}')
elif delta == 0:
    x = (-b) / (2 * a)
    print('x1 = x2 {}'.format(x))
else:
    print('brak rozwiazan')

# dane z matur

pisemny_j_Polski = int(input('pisemny polski'))
pisemny_

