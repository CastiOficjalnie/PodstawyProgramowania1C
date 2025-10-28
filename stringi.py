napis = 'raggin'

# fragment tekstu
# 1) wycinanie od ..... do
print(napis[2:5]) #czyli tak naprawde od 2 do 4

    # 2) wycinanie od....do co iles
print(napis[2:10:2])

    # 3) wycinanie od poczatku
print(napis[:3])

    # 4) wycinanie od konca
print(napis[7:])

    # 5) czytanie od konca
print(napis[::-1])
# II) zawieranie sie znaku w slowie
if 'a' in napis:
    print('należy')