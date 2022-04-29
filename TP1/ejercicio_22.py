# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
#   a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#   queden más objetos en la mochila;
#   b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
#   c. Utilizar un vector para representar la mochila.

mochila = [
    'Pistola blaster',
    'Holocrón',
    'Rifle blaster',
    'Sable de luz',
    'Granado de pulso',
]

def usarLaFuerza(vector, elements):
    if(len(vector) == 0):
        print('No quedan mas objetos en la mochila')

    elif(vector[0] == 'Sable de luz'):
        print('Se ha encontrado el sable de luz')
        print(f'Fue necesario quitar {elements} elementos')
    
    else:
        usarLaFuerza(vector[1:], elements+1)


usarLaFuerza(mochila, 0)