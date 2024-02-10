import numpy as np

demanda_agua = np.array([
    8400, 7140, 6300, 5310, 5280, 5100, 5070, 4680, 4680, 4650, 4470, 
    4290, 4200, 4080, 3750, 3630, 3540, 3330, 3120, 3090, 3060, 3060, 3000 
])

nombres_distritos_lima = [
    "San Isidro", "Miraflores", "La Molina", "Barranco", "San Borja", "Magdalena del Mar", "Lince", "Surquillo", 
    "Jesús María", "Pueblo Libre", "San Miguel", "Santiago de Surco", "Lima", "San Luis", "San Bartolo", "Los Olivos",
    "Breña", "San Martín de Porres", "La Victoria", "Chorrillos", "Rimac", "San Juan de Miraflores", "El Agustino"
]

agua_disponible = 90000

num_distritos = len(nombres_distritos_lima)

soluciones_por_poblacion = 100

num_padres_apareamiento = 10

tamaño_poblacion = (soluciones_por_poblacion, num_distritos)

def calcular_aptitud_poblacion(demanda_agua, poblacion, agua_disponible):
    aptitud = np.zeros(poblacion.shape[0])
    for i in range(poblacion.shape[0]):
        total_agua_asignada = np.sum(poblacion[i])
        if total_agua_asignada > agua_disponible:
            aptitud[i] = -1 
        else:
            desviacion = total_agua_asignada - np.sum(demanda_agua)
            aptitud[i] = 1 / (1 + abs(desviacion))
    return aptitud

def seleccionar_poblacion_apareamiento(poblacion, aptitud, num_padres):
    padres = np.empty((num_padres, poblacion.shape[1]))
    for num_padre in range(num_padres):
        indice_max_aptitud = np.where(aptitud == np.max(aptitud))
        indice_max_aptitud = indice_max_aptitud[0][0]
        padres[num_padre, :] = poblacion[indice_max_aptitud, :]
        aptitud[indice_max_aptitud] = float('-inf')
    return padres

def cruza(padres, tamaño_descendencia):
    descendencia = np.empty(tamaño_descendencia)
    punto_cruza = np.uint8(tamaño_descendencia[1] / 2)

    for k in range(tamaño_descendencia[0]):
        indice_padre1 = k % padres.shape[0]
        indice_padre2 = (k + 1) % padres.shape[0]
        descendencia[k, 0:punto_cruza] = padres[indice_padre1, 0:punto_cruza]
        descendencia[k, punto_cruza:] = padres[indice_padre2, punto_cruza:]
    return descendencia

def mutacion(descendencia_cruza, num_mutaciones=1):
    for indice in range(descendencia_cruza.shape[0]):
        indices_genes = np.random.choice(descendencia_cruza.shape[1], num_mutaciones, replace=False)
        valores_aleatorios = np.random.uniform(-1, 1, num_mutaciones)
        descendencia_cruza[indice, indices_genes] += valores_aleatorios
    return descendencia_cruza

def normalizar_solucion(solucion, agua_disponible):
    for i in range(len(solucion)):
        if solucion[i] > demanda_agua[i]:
            solucion[i] = demanda_agua[i]
    total_agua_asignada = np.sum(solucion)
    if total_agua_asignada > agua_disponible:
        solucion = (solucion / total_agua_asignada) * agua_disponible
    return solucion

def ejecutar_algoritmo_genetico():
    poblacion_inicial = np.random.uniform(low=0.9 * demanda_agua, high=1.1 * demanda_agua, size=tamaño_poblacion)
    
    num_generaciones = 100
    
    for generacion in range(num_generaciones):
        aptitud = calcular_aptitud_poblacion(demanda_agua, poblacion_inicial, agua_disponible)
        padres = seleccionar_poblacion_apareamiento(poblacion_inicial, aptitud, num_padres_apareamiento)       
        tamaño_descendencia = (tamaño_poblacion[0] - padres.shape[0], num_distritos)       
        descendencia_cruza = cruza(padres, tamaño_descendencia)    
        descendencia_mutacion = mutacion(descendencia_cruza)
            
        poblacion_inicial[0:padres.shape[0], :] = padres
        poblacion_inicial[padres.shape[0]:, :] = descendencia_mutacion

    mejor_solucion = poblacion_inicial[np.argmax(aptitud)]
    mejor_solucion = normalizar_solucion(mejor_solucion, agua_disponible)
    mejor_solucion_final = {}        

    for i, nombre_distrito in enumerate(nombres_distritos_lima):
        asignacion_recursos = round(mejor_solucion[i], 2)
        mejor_solucion_final[nombre_distrito] = asignacion_recursos
    
    return mejor_solucion_final
