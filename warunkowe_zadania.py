#rozwiazywanie rownania kwadratowegp

a = float(input('podaj liczne różną od 0 '))
b = float(input('podaj liczbe b '))
c = float(input('podaj liczbe c '))

if b == 0 and c == 0:
    if -c/a > 0:
        x1 = (-c/a) ** 0.5
        x2 = -((-c/a )) ** 0.5
        print(f'x1 = {x1} v x2 = {x2}')
    if -c/a < 0:
        print('brak rozwiazan')
if b != 0 and c != 0:
    delta = b ** 2 - 4 * a * b
    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print(f'x1 = {x1} v x2 = {x2}')
    if delta == 0:
        x = (-b) / (2 * a)
        print(f'x = {x}')
else:
    print('brak rozwiazan')


