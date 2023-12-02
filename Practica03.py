import heapq
import time

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}
    
    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)
        self.aristas[vertice] = []
    
    def agregar_arista(self, inicio, fin, peso):
        self.aristas[inicio].append((fin, peso))
    
def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo.vertices}
    
    distancias[inicio] = 0
    
    prioridad = [(0, inicio)]
    
    while prioridad:
        distancia_actual, vertice_actual = heapq.heappop(prioridad)
        
        if distancia_actual > distancias[vertice_actual]:
            continue
        
        for vecino, peso in grafo.aristas[vertice_actual]:
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(prioridad, (distancia, vecino))
    
    return distancias

def medir_tiempo_ejecucion(func, *args):
    inicio_tiempo = time.time()
    resultado = func(*args)
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    return resultado, tiempo_ejecucion

# Ejemplo de uso:
g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_vertice('E')
g.agregar_vertice('F')
g.agregar_vertice('G')
g.agregar_arista('A', 'B', 108)
g.agregar_arista('A', 'C', 432)
g.agregar_arista('B', 'C', 64)
g.agregar_arista('B', 'D', 37)
g.agregar_arista('C', 'D', 256)
g.agregar_arista('D', 'E', 178)
g.agregar_arista('E', 'F', 596)
g.agregar_arista('F', 'G', 10)

vertice_inicio = 'A'
resultado, tiempo = medir_tiempo_ejecucion(dijkstra, g, vertice_inicio)

print(f"Caminos mínimos desde el vértice {vertice_inicio}:")
for vertice, distancia in resultado.items():
    print(f"Vértice {vertice}: Distancia {distancia}")
    print(f"Tiempo de ejecución: {tiempo} segundos")
