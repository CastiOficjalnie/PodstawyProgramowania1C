plik = open('ruch.txt')
dane = plik. readlines()
for i in range(len(dane)):
    dane[i] = dane[i].split()
    dane[i] = list(map(float, dane[i]))
print(dane)

def t(i):
    return (i - 1) / 100

def Vsr(rv, rp, dt):
    return [rk[0] - rp[0] / dt, rk[1] - rp[1] / dt]

def szyb_sr(Vsr):
    return (Vsr[0] +


