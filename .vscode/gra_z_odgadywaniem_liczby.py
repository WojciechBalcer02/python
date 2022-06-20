from random import randint
los = randint(1,10)
odp = -1
i = 0
print("Zgadnij liczbę komputera")
while odp!=los:
    odp = int(input("podaj liczbę: "))
    i+=1
    if odp<los:
        print("podaj większą liczbe")
    elif odp>los:
        print("podaj liczbę mniejszą")
print("wygrałeś, ilość Twoich prób to:", i)