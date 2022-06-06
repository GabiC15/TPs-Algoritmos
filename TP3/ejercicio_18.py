from cola import Cola
from random import randint

def generadorTurnos():
    char = chr(randint(65, 70))
    n = randint(0, 999)
    formatNumber = (f'{n}', f'0{n}',f'00{n}')[(n<100) + (n<10)]
    return f'{char}{formatNumber}'

turnos = Cola()

# Punto A
for i in range(1000):
    turnos.arribo(generadorTurnos())

# Punto B
cola1 = Cola()
cola2 = Cola()
while(not turnos.cola_vacia()):
    dato = turnos.atencion()
    if(dato[0] in ['A', 'C', 'F']):
        cola1.arribo(dato)
    else:
        cola2.arribo(dato)

# Punto C
contA, contC, contF = 0, 0, 0
for i in range(cola1.tamanio()):
    dato = cola1.mover_al_final()
    if(dato[0] == 'A'):
        contA += 1
    elif(dato[0] == 'C'):
        contC += 1
    else:
        contF += 1

contB, contD, contE = 0, 0, 0
for i in range(cola2.tamanio()):
    dato = cola2.mover_al_final()
    if(dato[0] == 'B'):
        contB += 1
    elif(dato[0] == 'D'):
        contD += 1
    else:
        contE += 1

if(cola1.tamanio() > cola2.tamanio()):
    print('La cola 1 tiene mayor tamaño')
    if((contA > contC) & (contA > contF)):
        print('La A tiene mayor cantidad de elementos')
    elif((contC > contA) & (contC > contF)):
        print('La C tiene mayor cantidad de elementos')
    else:
        print('La F tiene mayor cantidad de elementos')
else:
    print('La cola 2 tiene mayor tamaño')
    if((contB > contD) & (contB > contE)):
        print('La B tiene mayor cantidad de elementos')
    elif((contD > contB) & (contD > contE)):
        print('La D tiene mayor cantidad de elementos')
    else:
        print('La E tiene mayor cantidad de elementos')

# Punto D
if(cola1.tamanio() < cola2.tamanio()):
    print('La cola 1 tiene menor tamaño.')
    for i in range(cola1.tamanio()):
        dato = cola1.mover_al_final()
        if(int(dato[1:]) > 506):
            print(dato)
else:
    print('La cola 2 tiene menor tamaño')
    for i in range(cola2.tamanio()):
        dato = cola2.mover_al_final()
        if(int(dato[1:]) > 506):
            print(dato)
