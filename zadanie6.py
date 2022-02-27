#lsta = []
#slownik = {}
#elementy w postaci klucz warotsc, kazdy element oddzielony jest przecinkiem
#sprawdzić różne metody dla słownikó i list
slownik = {"valueError": "to nie jest liczba","divError": "dzielisz przez zero","typeError": "Nie zgadza się typ w liście"}
lista = [1,0,4,'b',3,7,2,0,6,'a']



try:
    lista.sort()
except TypeError:
    print(slownik["typeError"])

print(lista)
print(str(lista.count('a')))

for element in lista:
    if(type(element)!=type(1)):
        lista.remove(element)

lista.sort()
print(lista)
lista.reverse()
print(lista)
print(str(len(lista)))

for element in slownik.keys():
    print(element)
for element in slownik.values():
    print(element)