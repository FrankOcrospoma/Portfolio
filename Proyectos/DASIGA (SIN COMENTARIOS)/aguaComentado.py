import numpy as np  # Importa la librería NumPy para trabajar con matrices y arreglos.

demanda_agua = np.array([  # Crea un arreglo NumPy con las demandas mensuales de agua de los distritos.
    8400, 7140, 6300, 5310, 5280, 5100, 5070, 4680, 4680, 4650, 4470, 
    4290, 4200, 4080, 3750, 3630, 3540, 3330, 3120, 3090, 3060, 3060, 3000 
])

nombres_distritos_lima = [  # Lista de nombres de los distritos de Lima.
    "San Isidro", "Miraflores", "La Molina", "Barranco", "San Borja", "Magdalena del Mar", "Lince", "Surquillo", 
    "Jesús María", "Pueblo Libre", "San Miguel", "Santiago de Surco", "Lima", "San Luis", "San Bartolo", "Los Olivos",
    "Breña", "San Martín de Porres", "La Victoria", "Chorrillos", "Rimac", "San Juan de Miraflores", "El Agustino"
]

agua_disponible = 90000  # Cantidad de agua disponible.

num_distritos = len(nombres_distritos_lima)  # Calcula el número de distritos.

soluciones_por_poblacion = 100  # Número de soluciones en la población inicial.

num_padres_apareamiento = 10  # Número de padres para la reproducción.

tamaño_poblacion = (soluciones_por_poblacion, num_distritos)  # Tamaño de la población inicial.
# Función para calcular la aptitud de cada solución en la población.

def calcular_aptitud_poblacion(demanda_agua, poblacion, agua_disponible):
    aptitud = np.zeros(poblacion.shape[0])  # Inicializa un arreglo de aptitud.

    for i in range(poblacion.shape[0]):
        total_agua_asignada = np.sum(poblacion[i])  # Calcula la asignación total de agua.

        # Verifica si la asignación supera la disponibilidad de agua.
        if total_agua_asignada > agua_disponible:
            aptitud[i] = -1  # Asigna aptitud negativa si se excede la disponibilidad.
        else:
            desviacion = total_agua_asignada - np.sum(demanda_agua)  # Calcula la desviación.
            aptitud[i] = 1 / (1 + abs(desviacion))  # Calcula la aptitud en función de la desviación.

    return aptitud

# Función para seleccionar a los padres para la reproducción.
def seleccionar_poblacion_apareamiento(poblacion, aptitud, num_padres):
    padres = np.empty((num_padres, poblacion.shape[1]))  # Crea un arreglo para los padres.

    for num_padre in range(num_padres):
        # Encuentra el índice de la solución con la mayor aptitud.
        indice_max_aptitud = np.where(aptitud == np.max(aptitud))
        indice_max_aptitud = indice_max_aptitud[0][0]
        padres[num_padre, :] = poblacion[indice_max_aptitud, :]  # Selecciona el padre de mayor aptitud.
        aptitud[indice_max_aptitud] = float('-inf')  # Marca al padre seleccionado para evitar ser seleccionado de nuevo.

    return padres

# Función para realizar la cruza de los padres y crear la descendencia.
def cruza(padres, tamaño_descendencia):
    descendencia = np.empty(tamaño_descendencia)  # Crea un arreglo para la descendencia.
    punto_cruza = np.uint8(tamaño_descendencia[1] / 2)  # Punto de cruza en el medio.

    for k in range(tamaño_descendencia[0]):
        indice_padre1 = k % padres.shape[0]  # Índice del primer padre.
        indice_padre2 = (k + 1) % padres.shape[0]  # Índice del segundo padre.
        descendencia[k, 0:punto_cruza] = padres[indice_padre1, 0:punto_cruza]  # Primer segmento del padre 1.
        descendencia[k, punto_cruza:] = padres[indice_padre2, punto_cruza:]  # Segundo segmento del padre 2.

    return descendencia


# Función para aplicar mutaciones a la descendencia.
def mutacion(descendencia_cruza, num_mutaciones=1):
    for indice in range(descendencia_cruza.shape[0]):
        indices_genes = np.random.choice(descendencia_cruza.shape[1], num_mutaciones, replace=False)  # Selecciona genes a mutar.
        valores_aleatorios = np.random.uniform(-1, 1, num_mutaciones)  # Genera valores aleatorios de mutación.
        descendencia_cruza[indice, indices_genes] += valores_aleatorios  # Aplica las mutaciones.

    return descendencia_cruza

# Función para normalizar la solución para que no se exceda la demanda de agua.
def normalizar_solucion(solucion, agua_disponible):
    for i in range(len(solucion)):
        if solucion[i] > demanda_agua[i]:
            solucion[i] = demanda_agua[i]  # Asegura que la asignación no exceda la demanda de agua.
    total_agua_asignada = np.sum(solucion)

    if total_agua_asignada > agua_disponible:
        solucion = (solucion / total_agua_asignada) * agua_disponible  # Ajusta la asignación si supera la disponibilidad.
    return solucion

# Función principal para ejecutar el algoritmo genético.
def ejecutar_algoritmo_genetico():
    poblacion_inicial = np.random.uniform(low=0.9 * demanda_agua, high=1.1 * demanda_agua, size=tamaño_poblacion)
    # Crea una población inicial con asignaciones de agua aleatorias cercanas a la demanda.

    num_generaciones = 100  # Número de generaciones del algoritmo.

    for generacion in range(num_generaciones):
        # Calcula la aptitud de cada solución en la población, teniendo en cuenta la demanda y la disponibilidad de agua.
        aptitud = calcular_aptitud_poblacion(demanda_agua, poblacion_inicial, agua_disponible)
        
        # Selecciona a los padres de la población actual en función de su aptitud.
        padres = seleccionar_poblacion_apareamiento(poblacion_inicial, aptitud, num_padres_apareamiento)
        
        # Calcula el tamaño necesario para la descendencia (nueva población) después de la selección de padres.
        tamaño_descendencia = (tamaño_poblacion[0] - padres.shape[0], num_distritos)
        
        # Realiza la cruza de los padres seleccionados para crear una nueva descendencia.
        descendencia_cruza = cruza(padres, tamaño_descendencia)
        
        # Aplica mutación a la descendencia recién generada.
        descendencia_mutacion = mutacion(descendencia_cruza)

        poblacion_inicial[0:padres.shape[0], :] = padres  # Reemplaza la parte de la población anterior con los padres seleccionados.
        poblacion_inicial[padres.shape[0]:, :] = descendencia_mutacion  # Agrega la descendencia generada por la cruza y la mutación.

    mejor_solucion = poblacion_inicial[np.argmax(aptitud)]  # Encuentra la mejor solución en la población.
    mejor_solucion = normalizar_solucion(mejor_solucion, agua_disponible)  # Normaliza la mejor solución.
    mejor_solucion_final = {}  # Crea un diccionario para almacenar las asignaciones finales.

    # Recorre la lista de nombres de distritos y obtiene tanto el índice (i) como el nombre del distrito (nombre_distrito).
    for i, nombre_distrito in enumerate(nombres_distritos_lima):
        
        # Accede a la asignación de recursos en la mejor solución encontrada para el distrito actual (i) y redondea el valor a 2 decimales.
        asignacion_recursos = round(mejor_solucion[i], 2)

        # Almacena la asignación de recursos para el distrito actual en un diccionario llamado mejor_solucion_final, utilizando el nombre del distrito como clave.
        mejor_solucion_final[nombre_distrito] = asignacion_recursos

    # Devuelve el diccionario que contiene las asignaciones finales de recursos para cada distrito.
    return mejor_solucion_final
