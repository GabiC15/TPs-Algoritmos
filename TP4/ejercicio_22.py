# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:

from lista import Lista

class Jedi:
    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"

lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('TPs-Algoritmos\TP4\jedis.txt')
lineas = file.readlines()

lineas.pop(0)
for linea in lineas:
    datos = linea.split(';')
    sables = Lista()
    maestros = Lista()
    for maestro in datos[3].split('/'):
        maestros.insertar(maestro)
    for sable in datos[4].split('/'):
        sables.insertar(sable)
    lista_jedi.insertar(Jedi(datos[0], datos[2], maestros, sables), campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0], datos[2], maestros, sables), campo='especie')

# a. listado ordenado por nombre y por especie
lista_jedi.barrido()
print()
lista_jedi2.barrido()

print()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto
kit = lista_jedi.busqueda('kit fisto', 'nombre')
if(kit):
    print(kit.info)
print()
ahsoka = lista_jedi.busqueda('ahsoka tano', 'nombre')
if(ahsoka):
    print(ahsoka.info)

print()

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices
lista_jedi.barrido_jedi_master()

print()

# d. mostrar los Jedi de especie humana y twi'lek
lista_jedi.barrido_filtro('human', 'especie')
print()
lista_jedi.barrido_filtro("twi'lek", 'especie')

print()

# e. listar todos los Jedi que comienzan con A
lista_jedi.barrido_comienza_con(['a'])

print()

# f. mostrar los Jedi que usaron sable de luz de más de un color
lista_jedi.barrido_sables_luz()

print()

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
lista_jedi.barrido_sables_amarillo_violeta()

print()

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
lista_jedi.barrido_maestro('qui-gon jin')
print()
lista_jedi.barrido_maestro('mace windu')
