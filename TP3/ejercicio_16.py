from cola import Cola

class Documento:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f'Nombre: {self.nombre} | Tipo: {self.tipo}'

colaImpresion = Cola()

# Punto A
colaImpresion.arribo(Documento('Lucas', 'empleado'))
colaImpresion.arribo(Documento('Juan', 'empleado'))
colaImpresion.arribo(Documento('Pedro', 'empleado'))

# Punto B
print('- Punto B')
print(colaImpresion.atencion())

# Punto C
colaImpresion.arribo(Documento('Francisco', 'staff'))
colaImpresion.arribo(Documento('Pablo', 'staff'))

# Punto D
colaImpresion.arribo(Documento('Felipe', 'gerente'))

# Punto E
print('- Punto E')
print(colaImpresion.atencion())
print(colaImpresion.atencion())

# Punto F
colaImpresion.arribo(Documento('Santiago', 'empleado'))
colaImpresion.arribo(Documento('Franco', 'empleado'))
colaImpresion.arribo(Documento('Matías', 'gerente'))

# Punto G
print('- Punto G')
while(not colaImpresion.cola_vacia()):
    print(colaImpresion.atencion())
