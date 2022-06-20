lista = [1,3,2,4,6,5,"a","c","b"]
print(lista)
lista[3]=-1
print(lista)
lista.remove("a")
print(lista)

listaLiczbowa=[1,-1,4,2,7,-35,23]
print(listaLiczbowa)
listaLiczbowa.sort()
print(listaLiczbowa)
listaLiczbowa.reverse()
print(listaLiczbowa)

i=0
while True:
    
    
    if i != 8:
        print(listaLiczbowa[i])
        i+=1
    elif i == 8:
        break
print("koniec")
