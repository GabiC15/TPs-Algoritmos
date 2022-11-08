# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
#   a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#   uno en las naturales) y tipo (natural o arquitectónica);
#   b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
#   la distancia que las separa;
#   c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#   d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#   e. determinar si algún país tiene más de una maravilla del mismo tipo;
#   f. deberá utilizar un grafo no dirigido.


from grafo import Grafo

g = Grafo(dirigido=False)


# Punto A
g.insertar_vertice('Petra', datos={
    'paises': ['Jordania'],
    'tipo': 'arquitectónica'
})
g.insertar_vertice('Taj Mahal', datos={
    'paises': ['India'],
    'tipo': 'arquitectónica'
})
g.insertar_vertice('Machu Picchu', datos={
    'paises': ['Perú'],
    'tipo': 'arquitectónica'
})
g.insertar_vertice('Chichén Itzá', datos={
    'paises': ['México'],
    'tipo': 'arquitectónica'
})
g.insertar_vertice('El Coliseo', datos={
    'paises': ['Roma'],
    'tipo': 'arquitectónica'
})
g.insertar_vertice('La Gran Muralla china', datos={
    'paises': ['China'],
    'tipo': 'arquitectónica'
})

g.insertar_vertice('Parque Nacional del río subterráneo de Puerto Princesa', datos={
    'paises': ['Filipinas'],
    'tipo': 'natural'
})
g.insertar_vertice('Montaña de la Mesa', datos={
    'paises': ['Sudáfrica'],
    'tipo': 'natural'
})
g.insertar_vertice('Cataratas del Iguazú', datos={
    'paises': ['Argentina', 'Brasil', 'Paraguay'],
    'tipo': 'natural'
})
g.insertar_vertice('Amazonia', datos={
    'paises': ['Bolivia', 'Brasil', 'Colombia', 'Ecuador', 'Guayana Francesa', 'Guyana', 'Perú', 'Surinam', 'Venezuela'],
    'tipo': 'natural'
})
g.insertar_vertice('Bahía de HaLong', datos={
    'paises': ['Vietnam'],
    'tipo': 'natural'
})
g.insertar_vertice('Isla Jeju', datos={
    'paises': ['Corea del Sur'],
    'tipo': 'natural'
})

# Punto B
g.insertar_arista('Petra', 'Taj Mahal', 1)
g.insertar_arista('Petra', 'Machu Picchu', 2)
g.insertar_arista('Petra', 'Chichén Itzá', 3)
g.insertar_arista('Petra', 'El Coliseo', 4)
g.insertar_arista('Petra', 'La Gran Muralla china', 5)
g.insertar_arista('Taj Mahal', 'Machu Picchu', 6)
g.insertar_arista('Taj Mahal', 'Chichén Itzá', 7)
g.insertar_arista('Taj Mahal', 'El Coliseo', 8)
g.insertar_arista('Taj Mahal', 'La Gran Muralla china', 9)
g.insertar_arista('Machu Picchu', 'Chichén Itzá', 10)
g.insertar_arista('Machu Picchu', 'El Coliseo', 11)
g.insertar_arista('Machu Picchu', 'La Gran Muralla china', 12)
g.insertar_arista('Chichén Itzá', 'El Coliseo', 13)
g.insertar_arista('Chichén Itzá', 'La Gran Muralla china', 14)
g.insertar_arista('El Coliseo', 'La Gran Muralla china', 15)

g.insertar_arista(
    'Parque Nacional del río subterráneo de Puerto Princesa', 'Montaña de la Mesa', 1)
g.insertar_arista(
    'Parque Nacional del río subterráneo de Puerto Princesa', 'Cataratas del Iguazú', 2)
g.insertar_arista(
    'Parque Nacional del río subterráneo de Puerto Princesa', 'Amazonia', 3)
g.insertar_arista(
    'Parque Nacional del río subterráneo de Puerto Princesa', 'Bahía de HaLong', 4)
g.insertar_arista(
    'Parque Nacional del río subterráneo de Puerto Princesa', 'Isla Jeju', 5)
g.insertar_arista(
    'Montaña de la Mesa', 'Cataratas del Iguazú', 6)
g.insertar_arista(
    'Montaña de la Mesa', 'Amazonia', 7)
g.insertar_arista(
    'Montaña de la Mesa', 'Bahía de HaLong', 8)
g.insertar_arista(
    'Montaña de la Mesa', 'Isla Jeju', 9)
g.insertar_arista(
    'Cataratas del Iguazú', 'Amazonia', 10)
g.insertar_arista(
    'Cataratas del Iguazú', 'Bahía de HaLong', 11)
g.insertar_arista(
    'Cataratas del Iguazú', 'Isla Jeju', 12)
g.insertar_arista(
    'Amazonia', 'Bahía de HaLong', 13)
g.insertar_arista(
    'Amazonia', 'Isla Jeju', 14)
g.insertar_arista(
    'Bahía de HaLong', 'Isla Jeju', 15)

# Punto C
arbolExp = g.kruskal()

for line in arbolExp:
    print()
    if 'natural' in line:
        print('Arbol de expansion minimo de maravillas naturales:')
    else:
        print('Arbol de expansion minimo de maravillas arquitectonicas:')
    print(line)

print()

# Punto D
maravillas = g.contar_maravillas()
paises_dobles = []
for k, v in maravillas.items():
    if (v['arq'] & v['nat']):
        paises_dobles.append(k)
if (paises_dobles):
    print('Los paises con maravillas naturales y arquitectónicas son:', paises_dobles)
else:
    print('No hay paises con maravillas naturales y arquitectónicas')

print()

# Punto E
paises_repetidos = []
for k, v in maravillas.items():
    if ((v['arq'] > 1) | (v['nat'] > 1)):
        paises_repetidos.append(k)

if (paises_repetidos):
    print('Los paises con maravillas del mismo tipo son:', paises_repetidos)
else:
    print('No hay paises con maravillas del mismo tipo')
