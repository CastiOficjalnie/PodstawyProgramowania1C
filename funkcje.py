''' hurra():

#hurra2 - nazwa funkcji
# n - parametr funkcji
# 6 - argument funkcji
# hurra2(6) - wywolanie funkcji dla argumentu 6

def hurra2(6):
    print('hurra!\n' * n)

hurra2(6)
# n = 10 tzw. parametr z argumentem domyslnym
def hurra3(n = 10)
print('hurra!\n' * n)

hurra3()

#jezeli funkcja pp wykonuje jakas czynnosc i nie mozemy wykorzystac dalej efektow jej pracy to jest to procedura

# pole calkowite graniastoslupa prawidlowego trojkatnego'''
def p_tr_rown(a):
    return a ** 2 * (3 ** 0.5) / 4
Pp = p_tr_rown(3 ** 0.25)
print(Pp)

# pole prostokata
def pole(a, b):
    return a * b

psb = pole(5, 4)

def p_gran(a, b):
    return 2 * p_tr_rown(a) * 4 * pole(a, b)

Pg = p_gran(7, 4)
print(Pg)

