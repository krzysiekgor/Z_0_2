#instrukcja for
#for licznik in sekwencja
#   -instrukcja lub blok instrukcji
#else:
#   -instrukcja lub blok instrukcji
#else jest zbędny

#range(start,stop,step)

# for a in range(0,7,1):
#    print(a)

# lista = ['a',3,4,5,6.7]
# for element in lista:
#     print(element)

#while warunek:
#   -instrukcja lub blok instrukcji
#else:
#   -instrukcja lub blok instrukcji
#else jest zbędny

# licznik =0
# while licznik!=11:
#     print(licznik)
#     licznik+=1
# else:
#     print ("zostalo wyswietlonych " + str(licznik) + " liczb")

#break - przerywa petle
#continue - konczy obecna iteracje i leci dalej

lista = [4,5,6,7,8,9]
liczba = input("wpisz liczbę: ")

licznik=0
while licznik !=len(lista):
    if int(liczba)-lista[licznik]==0:
        print("liczba "+ str(lista[licznik]) + " - "+str(liczba) +" = 0")
        break
    else:
        licznik+=1
else:
    print("żaden element nie dał porządanego wyniku")