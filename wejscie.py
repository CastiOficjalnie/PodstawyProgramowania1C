#1. wprowadzanie danych przez uzytkownika do programu
from zmienne import liczba_z_przecinkiem

#   1)utworzenie zmiennej
#   2)na ekranie pojawia sie komunikat z inputa
#   3)program sie zatrzymuje i czeka na podanie i zatwierdzenie(ENTER) dancyh
#   4)po wpisaniu i zatwierdzeniu to co wpiszemy trafia jako string to zmiennej
#   5)program wykonuje sie dalej
dane = input("podaj swoje imie ")

liczba = int(input('podaj liczbe '))
print(type(liczba))

liczba_z_przecinkie = float(input('podaj liczbe z przecinkiem '))
print(type(liczba_z_przecinkie))

cos = list(input('podaj cos'))
print(cos)
print(type(cos))
