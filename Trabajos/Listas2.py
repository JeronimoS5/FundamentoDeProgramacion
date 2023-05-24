#Leer un numero por teclado y responder las siguientes preguntas:
#1)Si esta o no esta
#2)Cuantas veces se repite y en que posiciones

#Capturar los elementos de la lista
lista=[]
lisPosRep=[]
lisPosNoRep=[]

Valor=int(input("Ingrese Valor (0 para finalizar) :")) 
while Valor!=0:
    lista.append(Valor)
    Valor=int(input("Ingresar valor (0 para finalizar) :"))

print("Tamaño de la lista :")
print(len(lista))
print(lista)

print("Pedir un dato y buscarlo")
ValBus=int(input("Digite el valor a buscar:")) 

posList=0
canEleRep=0
while posList<int(len(lista)):
  if lista[posList]==ValBus:
        canEleRep=canEleRep+1
        lisPosRep.append(posList)
        print("Lo encontro")
  else:
      lisPosNoRep.append(posList)
    
  posList=posList+1

print("El numero se repite : ", canEleRep)
print("Lista de repeticiones :", lisPosRep)
print("Lista de No repeticiones :", lisPosNoRep)


