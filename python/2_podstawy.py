tekst = "Anna, paweł, TomEK"

tab = tekst.split(",") # implode
print(tekst)
print(tab)
imie = tab[0]
print(imie)
print(type(tab)) # sprawdza TYPE

imieDuze = imie.upper() #strtolower
print(imieDuze)
imieMale = imie.lower() #strtoupper
print(imieMale)

#sprawdzanie zawartości
imie = ""
zawartosc = imie.isalpha() #czy w zmiennej jest wartosc
print(zawartosc)
print(type(zawartosc)) #wyswietli bool

imie = "Julia"
print("\nDane użytkownika:\nMasz na imię: " + imie)

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip() #rtrim
print(text1 + text2)

#wyswietlanie łańcuchów znaków

#wszystkie wersje Pythona
text = "%s, Java i %s"%("PHP", "Python")
print(text)

#nowsze wersje Pythona 2.6
text = "{0}, Java i {1}".format("PHP","Python")
print(text)

#help(text.replace)
new = text.replace("PHP","C#") #str_replace
print(new)

#wypisanie danychg
rok = "2019"
miesiac = "marzec"
dzien = "23"

print("Data : ", end="") # nie przechodzi do nastepnej linii
print(dzien,miesiac,rok)

print("Data : ", end="") # nie przechodzi do nastepnej linii
print(dzien,miesiac,rok, sep="-") #ustawia separator

