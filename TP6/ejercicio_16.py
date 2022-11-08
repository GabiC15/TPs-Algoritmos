# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
#   a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#   baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
#   b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
#   c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#   para conectar todos los ambientes;
#   d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#   determinar cuántos metros de cable de red se necesitan para conectar el router con el
#   Smart Tv.

from grafo import Grafo

g = Grafo(dirigido=False)

# Punto A
g.insertar_vertice('cocina')
g.insertar_vertice('comedor')
g.insertar_vertice('cochera')
g.insertar_vertice('quincho')
g.insertar_vertice('baño 1')
g.insertar_vertice('baño 2')
g.insertar_vertice('habitación 1')
g.insertar_vertice('habitación 2')
g.insertar_vertice('sala de estar')
g.insertar_vertice('terraza')
g.insertar_vertice('patio')

# Punto B
g.insertar_arista('cocina', 'comedor', 2)
g.insertar_arista('cocina', 'patio', 3)
g.insertar_arista('cocina', 'sala de estar', 1)

g.insertar_arista('comedor', 'sala de estar', 5)
g.insertar_arista('comedor', 'patio', 3)
g.insertar_arista('comedor', 'terraza', 8)

g.insertar_arista('cochera', 'baño 1', 4)
g.insertar_arista('cochera', 'patio', 3)
g.insertar_arista('cochera', 'quincho', 1)

g.insertar_arista('quincho', 'terraza', 2)
g.insertar_arista('quincho', 'comedor', 2)
g.insertar_arista('quincho', 'sala de estar', 5)

g.insertar_arista('baño 1', 'comedor', 5)
g.insertar_arista('baño 1', 'terraza', 4)
g.insertar_arista('baño 1', 'cocina', 2)

g.insertar_arista('baño 2', 'sala de estar', 3)
g.insertar_arista('baño 2', 'patio', 2)
g.insertar_arista('baño 2', 'comedor', 1)

g.insertar_arista('habitación 1', 'baño 2', 6)
g.insertar_arista('habitación 1', 'patio', 4)
g.insertar_arista('habitación 1', 'cocina', 3)

g.insertar_arista('habitación 2', 'comedor', 5)
g.insertar_arista('habitación 2', 'terraza', 2)
g.insertar_arista('habitación 2', 'sala de estar', 3)


# Punto C
expMin = g.kruskal()
cable = 0
for nodo in expMin[0].split('-'):
    cable += int(nodo.split(';')[2])

print('La cantidad de cable necesario es', cable, 'metros')

# Punto D
dijkstra = g.dijkstra('baño 2')
caminoCorto = g.camino(dijkstra, 'habitación 2')
camino, costo = caminoCorto['camino'], caminoCorto['costo']
print('El camino es', camino,
      'Y la cantidad de cable necesaria es', costo, 'metros')
