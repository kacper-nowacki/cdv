#Przykładowy plik
"""
print("CDV")
print(2)

#potegowanie
potega = 2 ** 10
print(potega)
tekst = "CDV"
print(tekst *2)

#pobieranie danych z klawiatur
imie = 'Kacper'
print("Twoje imie: " + imie)

nazwisko = 'Nowacki'
print("Twoje dane: " + imie + ' ' + nazwisko)

dlugosc = len(nazwisko) #dlugosc ciagu
print(type(dlugosc)) # wyswietla typ zmiennej
dlugosc = str(dlugosc) #rzutowanie , zamiana na stringa
print('Dlugosc nazwiska:' + dlugosc)
"""



######programik
"""
print("Podaj imie: ")
imie = input()
print("Podaj wiek: ")
wiek = input()

print("Twoje imie: " + imie)
print("Twoj wiek: " + wiek)
"""
nazwisko = "Kowalski"

pierwszyZnak = nazwisko[0] #tablica - 1 znak
print(pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko) -1]
print(ostatniZnak)

#konwersja
x = "5"
print(type(x))
x = int(x)
print(type(x))
x = float(x)
print(type(x))
print(x)

y = 5;
print(type(y))
y = y / 2
print(type(y))
nazwisko = 'Kowalski'
print(nazwisko[0])
print(nazwisko[0:3])
print(nazwisko[-2])
print(nazwisko[-2:])
print(nazwisko[:-2])
