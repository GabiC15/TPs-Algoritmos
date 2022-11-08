from heap import HeapMax


class Documento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f'Nombre: {self.nombre} | Tipo: {self.tipo}'


colaImpresion = HeapMax()

# Punto A
colaImpresion.arribo(Documento('Lucas', 'empleado'), 1)
colaImpresion.arribo(Documento('Juan', 'empleado'), 1)
colaImpresion.arribo(Documento('Pedro', 'empleado'), 1)

# Punto B
print('- Punto B')
print(colaImpresion.vector[0][0])

# Punto C
colaImpresion.arribo(Documento('Francisco', 'staff'), 2)
colaImpresion.arribo(Documento('Pablo', 'staff'), 2)

# Punto D
colaImpresion.arribo(Documento('Felipe', 'gerente'), 3)

# Punto E
print('- Punto E')
print(colaImpresion.vector[0][0])
print(colaImpresion.vector[1][0])

# Punto F
colaImpresion.arribo(Documento('Santiago', 'empleado'), 1)
colaImpresion.arribo(Documento('Franco', 'empleado'), 1)
colaImpresion.arribo(Documento('Matías', 'gerente'), 3)

# Punto G
print('- Punto G')
for doc in colaImpresion.vector:
    print(doc[0])
