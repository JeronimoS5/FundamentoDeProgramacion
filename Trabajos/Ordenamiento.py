sueldos=[]

for x in range (5) :
    valor=int(input("Ingrese SUeldo:"))
    sueldos.append(valor)   

print("Lista sin ordenar")
print(sueldos)
canInt=0
print(sueldos.sort()) 

for k in range (4) :
     for x in range (4) :
          if sueldos [x] > sueldos [x+1]:
           aux=sueldos[x]
           sueldos[x]=sueldos[x+1] 
           sueldos[x+1]= aux
           canInt=canInt+1


print("Lista con el ultimo elemento ordenado")
print(sueldos)
print("Numeros de intercambios:",canInt)

sueldos=[]

for x in range (5) :
    valor=int(input("Ingrese SUeldo:"))
    sueldos.append(valor)   

print("Lista sin ordenar")
print(sueldos)

