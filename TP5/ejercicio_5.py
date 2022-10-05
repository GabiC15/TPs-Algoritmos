# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU),
#  desarrollar un algoritmo que contemple lo siguiente:
#   a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica
#   si es un héroe o un villano, True y False respectivamente;
#   b. listar los villanos ordenados alfabéticamente;
#   c. mostrar todos los superhéroes que empiezan con C;
#   d. determinar cuántos superhéroes hay el árbol;
#   e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#   encontrarlo en el árbol y modificar su nombre;
#   f. listar los superhéroes ordenados de manera descendente;
#   g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#   los villanos, luego resolver las siguiente tareas:
#       I. determinar cuántos nodos tiene cada árbol;
#       II. realizar un barrido ordenado alfabéticamente de cada árbol.

from arbol import *


arbol = nodoArbol()

# Punto A
insertar_nodo(arbol, 'Iron Man', {'villano': False})
insertar_nodo(arbol, 'Thanos', {'villano': True})
insertar_nodo(arbol, 'Loki', {'villano': True})
insertar_nodo(arbol, 'Thor', {'villano': False})
insertar_nodo(arbol, 'Capitán América', {'villano': False})
insertar_nodo(arbol, 'Baron Zemo', {'villano': True})
insertar_nodo(arbol, 'Ultron', {'villano': True})
insertar_nodo(arbol, 'Hulk', {'villano': False})
insertar_nodo(arbol, 'Doctor Stranfds', {'villano': False})


# Punto B
inorden_villano(arbol)

print()

# Punto C
inorden_empieza_con(arbol, 'C')

print()

# Punto D
contador = {
    'villanos': 0,
    'heroes': 0
}
contar_heroes_villanos(arbol, contador)
print(contador['heroes'])

print()

# Punto E
buscado = busqueda_proximidad(arbol, 'Doctor')
eliminar_nodo(arbol, buscado['info'])
insertar_nodo(arbol, 'Doctor Strange', buscado['datos'])
inorden(arbol)

# Punto F
postorden(arbol)

# Punto G
arbol_heroes = nodoArbol()
arbol_villanos = nodoArbol()
crear_bosque(arbol, arbol_heroes, arbol_villanos)
print('Cantidad de heroes:', contar_nodos(arbol_heroes))
print()
print('Cantidad de villanos:', contar_nodos(arbol_villanos))
print()
inorden(arbol_heroes)
print()
inorden(arbol_villanos)