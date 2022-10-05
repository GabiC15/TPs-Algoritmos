# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
#   a. listado inorden de las criaturas y quienes la derrotaron;
#   b. se debe permitir cargar una breve descripción sobre cada criatura;
#   c. mostrar toda la información de la criatura Talos;
#   d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#   e. listar las criaturas derrotadas por Heracles;
#   f. listar las criaturas que no han sido derrotadas;
#   g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#   o dios que la capturo;
#   h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#   Erimanto indicando que Heracles las atrapó;
#   i. se debe permitir búsquedas por coincidencia;
#   j. eliminar al Basilisco y a las Sirenas;
#   k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#   derroto a varias;
#   l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#   m. realizar un listado por nivel del árbol;
#   n. muestre las criaturas capturadas por Heracles.

from arbol import *

arbol = nodoArbol()

insertar_nodo(arbol, 'Ceto', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Tifón', {'derrotado_por': 'Zeus', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Equidna', {'derrotado_por': 'Argos Panoptes T', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Dino', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Pefredo', {'derrotado_por': None, 'descripcion': None, 'capturada': 'Heracles'})
insertar_nodo(arbol, 'Enio', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Escila', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Caribdis', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Euríale', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Esteno', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Medusa', {'derrotado_por': 'Perseo', 'descripcion': None, 'capturada': 'Heracles'})
insertar_nodo(arbol, 'Ladón', {'derrotado_por': 'Heracles', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Águila del Cáucaso', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Quimera', {'derrotado_por': 'Belerofonte', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Hidra de Lerna', {'derrotado_por': 'Heracles', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'León de Nemea ', {'derrotado_por': 'Heracles', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Esfinge', {'derrotado_por': 'Edipo', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Dragón de la Cólquida', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Cerbero', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Cerda de Cromión', {'derrotado_por': 'Teseo', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Ortro', {'derrotado_por': 'Heracles', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Toro de Creta', {'derrotado_por': 'Teseo', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Jabalí de Calidón', {'derrotado_por': 'Atalanta', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Carcinos', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Gerión', {'derrotado_por': 'Heracles', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Cloto', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Láquesis', {'derrotado_por': None, 'descripcion': None, 'capturada': 'Heracles'})
insertar_nodo(arbol, 'Átropos', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Minotauro de Creta', {'derrotado_por': 'Teseo', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Harpías', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Argos Panoptes', {'derrotado_por': 'Hermes', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Aves del Estínfalo', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Talos', {'derrotado_por': 'Medea', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Sirenas', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Pitón', {'derrotado_por': 'Apolo', 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Cierva de Cerinea', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Basilisco', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Jabalí de Erimanto', {'derrotado_por': None, 'descripcion': None, 'capturada': None})
insertar_nodo(arbol, 'Cierva Cerinea', {'derrotado_por': None, 'descripcion': None, 'capturada': None})

# Punto A
inorden_criatura(arbol)

print()

# Punto B
# Parametro agregado a los datos

print()

# Punto C
buscado = busqueda(arbol, 'Talos')
if buscado:
    print(buscado['info'], '-', buscado['datos'])

# Punto D
heroes = {}
heroes_derrotas(arbol, heroes)
heroes = dict(sorted(heroes.items(), key=lambda item: item[1]))
heroes = list(reversed(heroes))
for i in range(3):
    print(heroes[i])

print()

# Punto E
inorden_derrotado_por(arbol, 'Heracles')

print()

# Punto F
inorden_no_derrotados(arbol)

print()

# Punto G
# Campo agregado

# Punto H
busqueda(arbol, 'Cerbero')['datos']['capturada'] = 'Heracles'
busqueda(arbol, 'Toro de Creta')['datos']['capturada'] = 'Heracles'
busqueda(arbol, 'Cierva Cerinea')['datos']['capturada'] = 'Heracles'
busqueda(arbol, 'Jabalí de Erimanto')['datos']['capturada'] = 'Heracles'

print()

# Punto I
# Por ejemplo con "Esfinge"
print(busqueda(arbol, 'Esfinge')['info'])

print()

# Punto J
eliminar_nodo(arbol, 'Basilisco')
eliminar_nodo(arbol, 'Sirenas')
inorden(arbol)

print()

# Punto K
aves = busqueda(arbol, 'Aves del Estínfalo')
aves['datos']['derrotado_por'] = 'Heracles'
aves['datos']['descripcion'] = 'Heracles derroto a varias'

print()

# Punto L
buscado = busqueda(arbol, 'Ladón')
eliminar_nodo(arbol, buscado['info'])
insertar_nodo(arbol, 'Dragón Ladón', buscado['datos'])

print()

# Punto M
por_nivel(arbol)

print()

# Punto N
inorden_capturado_por(arbol, 'Heracles')