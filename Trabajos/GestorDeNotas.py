nombre = input("Ingrese el nombre del estudiante: ")

edad = int(input("Ingrese la edad del estudiante: "))

nota_final = float(input("Ingrese la nota final del estudiante: "))

inasistencias = int(input("Ingrese el número de inasistencias del estudiante: "))

if nota_final  < 3 and inasistencias > 12 :
    print("El estudiante pieder por academico y inasistencias")
elif nota_final < 3:
    print("El estudiante pierde por académico.")
elif inasistencias > 12:
    print("El estudiante pierde por inasistencia.")
else:
    print("El estudiante ha aprobado.")


