# 21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
# Desarrolle los algoritmos necesarios para realizar las siguientes tareas:

from random import randint
from lista import Lista

class Pelicula:
    def __init__(self, nombre, valoracion, estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.estreno = estreno
        self.recaudacion = recaudacion
    
    def __str__(self):
        return f'{self.nombre} | VL: {self.valoracion} | EST: {self.estreno} | RN: {self.recaudacion}'

peliculas = Lista()
nombres = ['Thor 1', 'Star Wars 8', 'Transformers 2', 'Iron Man 2', 'Capitán América 3', 'Star Wars 5']
for nombre in nombres:
    peliculas.insertar(Pelicula(nombre, randint(0, 10), randint(2010, 2022), randint(10000*1000, 10000*1500)), 'nombre')

# a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado año
anio = int(input('Ingrese el anio a mostrar: '))
peliculas.barrido_filtro(anio, 'estreno')

print()

# b. mostrar los datos de la película que más recaudo
mayor = peliculas.mayor_de_lista('recaudacion')
print(mayor.info)

print()

# c. indicar las películas con mayor valoración del público, puede ser más de una
peliculas.mayores_de_lista('valoracion')

print()

# d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una lista auxiliar:
auxiliar = Lista()

#   I. por nombre,
peliculas.barrido()
print()

#   II. por recaudación,
while(not peliculas.lista_vacia()):
    elemento = peliculas.obtener_elemento(0)
    peliculas.eliminar(elemento.nombre, 'nombre')
    auxiliar.insertar(elemento, 'recaudacion')
auxiliar.barrido()
print()

#   III. por año de estreno,
while(not auxiliar.lista_vacia()):
    elemento = auxiliar.obtener_elemento(0)
    auxiliar.eliminar(elemento.nombre, 'nombre')
    peliculas.insertar(elemento, 'estreno')
peliculas.barrido()
print()

#   IV. por valoración del público.
while(not peliculas.lista_vacia()):
    elemento = peliculas.obtener_elemento(0)
    peliculas.eliminar(elemento.nombre, 'nombre')
    auxiliar.insertar(elemento, 'valoracion')
auxiliar.barrido()
