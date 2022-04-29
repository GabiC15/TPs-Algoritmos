# Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
# matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
# y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
# avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

# 0 = pared
# 1 = camino

matriz3 = [
    [1,1,1,0,0,0,0,0],
    [0,0,1,0,1,1,1,0],
    [1,1,1,1,1,1,1,0],
    [1,0,1,0,0,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,1,1],
    [1,1,1,1,0,0,1,0],
    [0,0,0,0,1,1,1,1]
]

matriz = [
    [1,1,1,0,0,0,0,0],
    [0,0,1,0,1,1,1,0],
    [1,1,1,1,1,0,1,0],
    [1,0,1,0,0,1,1,0],
    [1,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1],
    [1,1,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,1]
]

matriz2 = [
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,1]
]

correctPath = []

def laberinto(matriz, x, y, positions):
    lastPos = len(matriz)-1

    if((x == lastPos) & (y == lastPos)):
        return True
    
    if((not matriz[x][y]) | positions.count([x, y]) > 0):
        return False

    positions.append([x, y])

    if(x < lastPos):
        if(laberinto(matriz, x+1, y, positions)):
            correctPath.append([x+1, y])
            return True
    if(y < lastPos):
        if(laberinto(matriz, x, y+1, positions)):
            correctPath.append([x, y+1])
            return True
    if(x > 0):
        if(laberinto(matriz, x-1, y, positions)):
            correctPath.append([x-1, y])
            return True
    if(y > 0):
        if(laberinto(matriz, x, y-1, positions)):
            correctPath.append([x, y-1])
            return True
    return False

print(laberinto(matriz3, 0, 0, []))

WARNING = '\033[93m'
ENDC = '\033[0m'

for i in range(len(matriz3[0])):
    raw = ''
    for j in range(len(matriz3[0])):
        if([i, j] in correctPath):
            raw += f'{WARNING} {matriz3[i][j]} {ENDC}'
        else:
            raw += f' {matriz3[i][j]} '

    print(raw)