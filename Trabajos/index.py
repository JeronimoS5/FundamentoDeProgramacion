import random

# Lista de equipos de la liga Colombiana
equipos = ["Atlético Nacional", "Deportivo Cali", "Millonarios", "América de Cali",
           "Independiente Medellín", "Junior", "Santa Fe", "Once Caldas"]

# Generar las listas de equipos, goles de local y goles de visitante
partidos = []
for equipo_local in equipos:
    for equipo_visitante in equipos:
        if equipo_local != equipo_visitante:
            goles_local = random.randint(0, 5)
            goles_visitante = random.randint(0, 3)
            partido = (equipo_local, equipo_visitante, goles_local, goles_visitante)
            partidos.append(partido)

# Funciones de ayuda
def calcular_partidos_por_equipo(equipo, partidos):
    partidos_jugados = 0
    for partido in partidos:
        if equipo in partido[:2]:
            partidos_jugados += 1
    return partidos_jugados

def calcular_partidos_ganados(equipo, partidos):
    partidos_ganados = 0
    for partido in partidos:
        if equipo == partido[0] and partido[2] > partido[3]:
            partidos_ganados += 1
        elif equipo == partido[1] and partido[3] > partido[2]:
            partidos_ganados += 1
    return partidos_ganados

def calcular_partidos_perdidos(equipo, partidos):
    partidos_perdidos = 0
    for partido in partidos:
        if equipo == partido[0] and partido[2] < partido[3]:
            partidos_perdidos += 1
        elif equipo == partido[1] and partido[3] < partido[2]:
            partidos_perdidos += 1
    return partidos_perdidos

def calcular_partidos_empatados(equipo, partidos):
    partidos_empatados = 0
    for partido in partidos:
        if (equipo == partido[0] or equipo == partido[1]) and partido[2] == partido[3]:
            partidos_empatados += 1
    return partidos_empatados

# Calcular la cantidad de partidos por equipo
partidos_por_equipo = {}
for equipo in equipos:
    partidos_por_equipo[equipo] = calcular_partidos_por_equipo(equipo, partidos)

# Calcular la cantidad de partidos ganados por equipo
partidos_ganados_por_equipo = {}
for equipo in equipos:
    partidos_ganados_por_equipo[equipo] = calcular_partidos_ganados(equipo, partidos)

# Calcular la cantidad de partidos perdidos por equipo
partidos_perdidos_por_equipo = {}
for equipo in equipos:
    partidos_perdidos_por_equipo[equipo] = calcular_partidos_perdidos(equipo, partidos)

# Calcular la cantidad de partidos empatados por equipo
partidos_empatados_por_equipo = {}
for equipo in equipos:
    partidos_empatados_por_equipo[equipo] = calcular_partidos_empatados(equipo, partidos)

def calcular_partidos_empatados(equipo, partidos):
    partidos_empatados = 0
    for partido in partidos:
        if (equipo == partido[0] or equipo == partido[1]) and partido[2] == partido[3]:
            partidos_empatados += 1
    return partidos_empatados



def calcular_puntos(equipo, partidos):
    puntos = 0
    for partido in partidos:
        if equipo == partido[0] and partido[2] > partido[3]:
            puntos += 3
        elif equipo == partido[1] and partido[3] > partido[2]:
            puntos += 3
        elif (equipo == partido[0] or equipo == partido[1]) and partido[2] == partido[3]:
            puntos += 1
    return puntos

def generar_tabla_posiciones(equipos, partidos):
    tabla = []
    for equipo in equipos:
        puntos = calcular_puntos(equipo, partidos)
        partidos_jugados = calcular_partidos_por_equipo(equipo, partidos)
        partidos_ganados = calcular_partidos_ganados(equipo, partidos)
        partidos_perdidos = calcular_partidos_perdidos(equipo, partidos)
        partidos_empatados = calcular_partidos_empatados(equipo, partidos)
        dif_goles = sum([partido[2] - partido[3] if equipo == partido[0] else partido[3] - partido[2] for partido in partidos if equipo in partido[:2]])
        tabla.append([equipo, puntos, partidos_jugados, partidos_ganados, partidos_empatados, partidos_perdidos, dif_goles])
    tabla_ordenada = sorted(tabla, key=lambda x: (-x[1], -x[6], -x[3]))
    tabla_posiciones = []
    for i, equipo in enumerate(tabla_ordenada):
        tabla_posiciones.append([i+1, equipo[0], equipo[1], equipo[2], equipo[3], equipo[4], equipo[5], equipo[6]])
    return tabla_posiciones


print(tabla_posiciones)