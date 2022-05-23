# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:

#     a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando
#        como posición uno la cima de la pila;
#     b. determinar los personajes que participaron en más de 5 películas de la saga,
#        además indicar la cantidad de películas en la que aparece;
#     c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#     d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Pila

class Personaje:
    def __init__(self, nombre, cant_peliculas):
        self.nombre = nombre
        self.cant_peliculas = cant_peliculas

    def __str__(self):
        return f'Nombre: {self.nombre}'

def puntoA(pila):
    pila_aux = Pila()
    pos_groot, pos_rocket = 0, 0
    tamanio = pila.tamanio()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        if(dato.nombre == 'Rocket Raccoon'):
            pos_rocket = tamanio - pila.tamanio()
        if(dato.nombre == 'Groot'):
            pos_groot = tamanio - pila.tamanio()
        pila_aux.apilar(dato)
    
    print('Rocket Raccoon está en la posición: ', pos_rocket)
    print('Groot está en la posición: ', pos_groot)

    recargarPila(pila_aux, pila)

def puntoB(pila):
    pila_aux = Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        
        if(dato.cant_peliculas > 5):
            print(dato, '| Aparece en', dato.cant_peliculas, 'películas.')

        pila_aux.apilar(dato)
    recargarPila(pila_aux, pila)

def puntoC(pila):
    pila_aux = Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        
        if(dato.nombre == 'Black Widow'):
            print('La Viuda Negra paticipó en', dato.cant_peliculas, 'películas.')

        pila_aux.apilar(dato)
    recargarPila(pila_aux, pila)

def puntoD(pila):
    pila_aux = Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        
        if(dato.nombre[0] in ['C', 'D', 'G']):
            print(dato)

        pila_aux.apilar(dato)
    recargarPila(pila_aux, pila)


def recargarPila(pilaLlena, pilaDestino):
    while(not pilaLlena.pila_vacia()):
        pilaDestino.apilar(pilaLlena.desapilar())

personajes = Pila()

personajes.apilar(Personaje('Iron Man', 10))
personajes.apilar(Personaje('Groot', 4))
personajes.apilar(Personaje('Black Widow', 9))
personajes.apilar(Personaje('Rocket Raccoon', 4))
personajes.apilar(Personaje('Doctor Octopus', 2))
personajes.apilar(Personaje('Capitán América', 9))
personajes.apilar(Personaje('Nick Fury', 11))
personajes.apilar(Personaje('Drax', 4))

print('Posición de Rocket Raccoon y Groot:')
puntoA(personajes)

print('')

print('Personajes que participan en mas de 5 películas:')
puntoB(personajes)

print('')

print('Cantidad de películas en las que participó la Viuda Negra:')
puntoC(personajes)

print('')

print('Personajes con nombre que empieza con C, D y G:')
puntoD(personajes)
