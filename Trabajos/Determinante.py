import numpy as np

# Creamos una matriz de 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculamos el determinante
determinante = np.linalg.det(matriz)

# Imprimimos el resultado
print("El determinante de la matriz es:", determinante)
