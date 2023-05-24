def mostrar_mayor(v1,v2,v3):
    print("El valor mayor de los tres numeros es")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def mostrar_menor(v1,v2,v3):
    print("El valor menor de los tres numeros es")
    if v1<v2 and v1<v3:
        print(v1)
    else:
        if v2<v3:
            print(v2)
        else:
            print(v3)


def  cargar():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor valor:"))
    valor3=int(input("Ingrese el tercer valor:"))
    mostrar_mayor(valor1,valor2,valor3)
    mostrar_menor(valor1,valor2,valor3)

sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for x in range (4) :
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux
        
print("Lista con el ultimo elemento ordenado")
print(sueldos)

#programa principal

cargar()