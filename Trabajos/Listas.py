lista=[]

for x in range (10,60,10) :
 valor= int(input("Ingrese un valor entero: "))
 lista.append(valor)

print(lista)


Valor=int(input("Ingrese Valor (0 para finalizar) :")) 
while valor!=0:
  lista.append(valor)
  valor=int(input("Ingresar valor (0 para finalizar) :"))

print("Tamaño de la lista: ")
print(len(lista))

mayor=lista[0]
for x in range (1,5) :
  if lista[x]>mayor:
     mayor=lista[x]

print("Lista Completa")
print(lista)
print("Mayor de la lista")
print(mayor)
