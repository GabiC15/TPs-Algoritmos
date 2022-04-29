# 5. Desarrollar una función que permita convertir un número romano en un número decimal.

rom = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

def romano(valor, vector):
    if(len(valor) == 1):
        return vector[valor[0]]
    elif((vector[valor[0]] >= vector[valor[1]])):
        return vector[valor[0]] + romano(valor[1:], vector)
    else:
        return -(vector[valor[0]]) + romano(valor[1:], vector)

            

print(romano('xxiv', rom))