from cola import Cola

class Personaje:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero
    
    def __str__(self):
        return f'Nombre: {self.nombre} | Superhoroe: {self.superheroe} | Genero: {self.genero}'

personajes = Cola()

personajes.arribo(Personaje('Tony Stark', 'Iron Man', 'M'))
personajes.arribo(Personaje('Wanda Maximoff', 'Scarlet Witch', 'F'))
personajes.arribo(Personaje('Steve Rogers', 'Capitán América', 'M'))
personajes.arribo(Personaje('Natasha Romanoff', 'Black Widow', 'F'))
personajes.arribo(Personaje('Scott Lang', 'AntMan', 'M'))
personajes.arribo(Personaje('Carol Danvers', 'Capitana Marvel', 'F'))
personajes.arribo(Personaje('Peter Park', 'SpiderMan', 'M'))

# Punto A
for i in range(personajes.tamanio()):
    dato = personajes.mover_al_final()
    if(dato.superheroe == 'Capitana Marvel'):
        print('El nombre de Capitana Marvel es', dato.nombre)

# Punto B
print()
print('Personajes Femeninos')
for i in range(personajes.tamanio()):
    dato = personajes.mover_al_final()
    if(dato.genero == 'F'):
        print(dato)

# Punto C
print()
print('Personajes Masculinos')
for i in range(personajes.tamanio()):
    dato = personajes.mover_al_final()
    if(dato.genero == 'M'):
        print(dato)

# Punto D
print()
for i in range(personajes.tamanio()):
    dato = personajes.mover_al_final()
    if(dato.nombre == 'Scott Lang'):
        print('El superhoroe con nombre Scott Lang es', dato.superheroe)

# Punto E
print()
print('Personajes que comienzan con "S"')
for i in range(personajes.tamanio()):
    dato = personajes.mover_al_final()
    if('S' in [dato.nombre[0], dato.superheroe[0]]):
        print(dato)

# Punto F
print()
for i in range(personajes.tamanio()):
    dato = personajes.mover_al_final()
    if(dato.nombre == 'Carol Danvers'):
        print('El personaje Carol Danvers está en la cola')
        print('Y su nombre de superheroe es', dato.superheroe)
