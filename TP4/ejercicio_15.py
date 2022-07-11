# 15. Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre,
# cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver las siguientes actividades utilizando lista de lista implementando las
# funciones necesarias:

from lista import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return f'{self.nombre} | TG: {self.torneos_ganados} | BG: {self.batallas_ganadas} | BP: {self.batallas_perdidas}'

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} | NV {self.nivel} | TP: {self.tipo} | SBT: {self.subtipo}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45, 'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12, 'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50, 'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10, 'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemones = [
    {'name': 'Tyrantrum', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'Terrakion', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'Wingull', 'nivel': 38, 'tipo': 'agua', 'subtipo': 'volador'},
    {'name': 'pok4', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'pok5', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok6', 'nivel': 65, 'tipo': 'fuego', 'subtipo': 'planta'},
    {'name': 'pok7', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok8', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]


for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'], entrenador['tg'], entrenador['bp'],
        entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemones)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'], pokemon['nivel'], pokemon['tipo'],
            pokemon['subtipo']), 'nombre')

# a. obtener la cantidad de Pokémons de un determinado entrenador;
entrenador = input('Ingrese el nombre del entrenador: ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"El entrenador tiene {pos.sublista.tamanio()} pokemones")
else:
    print('El entrenador no se encuentra en la lista')

print()

# b. listar los entrenadores que hayan ganado más de tres torneos
lista_entrenadores.barrido_entrenador_mas_tres()

print()

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, '-', mayor.sublista.mayor_de_lista('nivel').info)

print()

# d. mostrar todos los datos de un entrenador y sus Pokémones;
entrenador = input('Ingrese nombre del entrenador: ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"Entrenador: {pos.info}")
    print('Le corresponden los siguientes pokemones:')
    pos.sublista.barrido()
else:
    print('El entrenador no se encuentra en la lista')

print()

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
lista_entrenadores.barrido_porcentaje_victorias()

print()

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
lista_entrenadores.barrido_tipo_subtipo('fuego', 'planta')
print()
lista_entrenadores.barrido_tipo_subtipo('agua', 'volador')

print()

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
nombre_entrenador = input('Ingrese nombre del entrenador: ')
entrenador = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
lista_entrenadores.promedio
print('El promedio de', nombre_entrenador, 'es', entrenador.sublista.promedio())

print()

# h. determinar cuántos entrenadores tienen a un determinado Pokémon
pokemon = input('Ingrese nombre del pokemón: ')
cantidad = lista_entrenadores.cantidad_entrenadores(pokemon)
print('El pokemon', pokemon, 'tiene', cantidad, 'entrenadores')

print()

# i. mostrar los entrenadores que tienen Pokémons repetidos
lista_entrenadores.entrenadores_pokemones_repetidos()

print()

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
lista_entrenadores.entrenadores_pokemones()

print()

# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
entrenador = input('Ingrese nombre del entrenador: ')
pokemon = input('Ingrese nombre del pokemon: ')
lista_entrenadores.entrenador_con_pokemon(entrenador, pokemon)
