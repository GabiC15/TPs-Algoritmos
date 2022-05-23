# Dada una pila de películas de las que se conoce su título, estudio cinematográfico y
# año de estreno, desarrollar las funciones necesarias para resolver las siguientes actividades:
#     a. mostrar los nombre películas estrenadas en el año 2014;
#     b. indicar cuántas películas se estrenaron en el año 2018;
#     c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

from pila import Pila

class Pelicula:
    def __init__(self, titulo, estudio, anioEstreno):
        self.titulo = titulo
        self.estudio = estudio
        self.anioEstreno = anioEstreno
    
    def __str__(self):
        return f'Titulo: {self.titulo} | Estudio: {self.estudio} | Año de estreno: {self.anioEstreno}'

def puntoA(pila):
    pilaAux = Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        if(dato.anioEstreno == 2014):
            print(dato.titulo)
        pilaAux.apilar(dato)
    recargarPila(pilaAux, pila)

def puntoB(pila):
    pilaAux = Pila()
    contador = 0
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        if(dato.anioEstreno == 2018):
            contador += 1
        pilaAux.apilar(dato)
    recargarPila(pilaAux, pila)
    print('Se estrenaron', contador)

def puntoC(pila):
    pilaAux = Pila()
    while(not pila.pila_vacia()):
        dato = pila.desapilar()
        if((dato.estudio == 'Marvel Studios') & (dato.anioEstreno == 2016)):
            print(dato)
        pilaAux.apilar(dato)
    recargarPila(pilaAux, pila)


def recargarPila(pilaLlena, pilaDestino):
    while(not pilaLlena.pila_vacia()):
        pilaDestino.apilar(pilaLlena.desapilar())

peliculas = Pila()

peliculas.apilar(Pelicula('Avengers: Infinity War', 'Marvel Studios', 2018));
peliculas.apilar(Pelicula('Doctor Strange', 'Marvel Studios', 2016));
peliculas.apilar(Pelicula('El justiciero 2', 'Columbia Pictures', 2018));
peliculas.apilar(Pelicula('Star Wars: El ascenso de Skywalker', 'Lucasfilm', 2019));
peliculas.apilar(Pelicula('Guardianes de la galaxia', 'Marvel Studios', 2014));
peliculas.apilar(Pelicula('Misión imposible: repercusión', 'Skydance Productions', 2018));
peliculas.apilar(Pelicula('Capitán América: Civil War', 'Marvel Studios', 2016));
peliculas.apilar(Pelicula('El sorprendente Hombre Araña 2: La amenaza de Electro', 'Sony Pictures', 2014));

pilaNueva = Pila()

print('Nombre películas estrenadas en el año 2014:')
puntoA(peliculas)

print()

print('Cantidad de peliculas que se entrenaron en 2018:')
puntoB(peliculas)

print()

print('Peliculas de Marvel Studios en 2016:')
puntoC(peliculas)
