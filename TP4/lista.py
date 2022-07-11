
def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoLista():
    info, sig, sublista = None, None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def __str__(self):
        text = '['
        for i in range(self.tamanio()): text += f"'{self.obtener_elemento(i)}', "
        text = text[:-2] + ']'
        return text

    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig
    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_anterior_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.aparicion < 1963):
                print(aux.info)
            aux = aux.sig
    
    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.maestro.busqueda('yoda') != None):
                print(aux.info)
            if(aux.info.maestro.busqueda('luke skywalker')):
                print(aux.info)
            aux = aux.sig

    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    def barrido_porcentaje_victorias(self):
        aux = self.__inicio
        while(aux is not None):
            total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            if(aux.info.batallas_ganadas / total >= 0.79):
                print(aux.info)
            aux = aux.sig

    def barrido_tipo_subtipo(self, tipo, subtipo):
        aux = self.__inicio
        while(aux is not None):
            sub_aux = aux.sublista.__inicio
            while(sub_aux is not None):
                if((tipo == sub_aux.info.tipo) & (subtipo == sub_aux.info.subtipo)):
                    print(aux.info)
                    break
                sub_aux = sub_aux.sig
            aux = aux.sig
    
    def barrido_sables_luz(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.sable_luz.tamanio() > 1):
                print(aux.info) 
            aux = aux.sig
    
    def barrido_sables_amarillo_violeta(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.sable_luz.busqueda('yellow')):
                print(aux.info)
            elif(aux.info.sable_luz.busqueda('purple')):
                print(aux.info) 
            aux = aux.sig

    def barrido_maestro(self, maestro):
        aux = self.__inicio
        busqueda = None
        while(aux is not None):
            busqueda = aux.info.maestro.busqueda(maestro)
            if(busqueda):
                print(aux.info)
                break
            aux = aux.sig
        if(not busqueda):
            print('El maestro', maestro, 'no tiene padawans')

    def cantidad_entrenadores(self, pokemon):
        aux = self.__inicio
        contador = 0
        while(aux is not None):
            entrenador = aux.sublista.busqueda(pokemon, 'nombre')
            if(entrenador):
                contador += 1
            aux = aux.sig
        return contador
    
    def entrenadores_pokemones_repetidos(self):
        aux = self.__inicio
        while(aux is not None):
            sub_aux = aux.sublista.__inicio
            busqueda = None
            while(sub_aux is not None):
                aux.sublista.eliminar(sub_aux.info.nombre, 'nombre')
                busqueda = aux.sublista.busqueda(sub_aux.info.nombre, 'nombre')
                if(busqueda):
                    print(aux.info)
                    break
                sub_aux = sub_aux.sig
            aux = aux.sig
    
    def entrenadores_pokemones(self):
        aux = self.__inicio
        while(aux is not None):
            tyrantrum = aux.sublista.busqueda('Tyrantrum', 'nombre')
            terrakion = aux.sublista.busqueda('Terrakion', 'nombre')
            wingull = aux.sublista.busqueda('Wingull', 'nombre')
            if((tyrantrum != None) | (terrakion != None) | (wingull != None)):
                print(aux.info)
            aux = aux.sig

    def entrenador_con_pokemon(self, nombre_ent, nombre_pok):
        entrenador = self.busqueda(nombre_ent, 'nombre')
        if(not entrenador):
            print('No se ha encontrado el entrenador')
            return
        pokemon = entrenador.sublista.busqueda(nombre_pok, 'nombre')
        if(pokemon):
            print(entrenador.info)
            print(pokemon.info)
        else:
            print('No se ha encontrado el entrenador con el pokemon')

    def barrido_filtro(self, dato, campo = None):
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) == dato):
                print(aux.info)
            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1 

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    def contar_por_casa(self):
        marvel, dc = 0, 0

        aux = self.__inicio
        while(aux is not None):
            if(aux.info.casa.capitalize() == 'Marvel'):
                marvel += 1
            if(aux.info.casa.capitalize() == 'Dc'):
                dc += 1
            aux = aux.sig

        return marvel, dc
    
    def promedio(self):
        total = 0
        aux = self.__inicio
        while(aux is not None):
            total += aux.info.nivel
            aux = aux.sig
        promedio = total / self.tamanio()
        return promedio
    
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                break
            aux = aux.sig
        return mayor

    def mayores_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                break
            aux = aux.sig
    
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) == criterio(mayor.info, campo)):
                print(aux.info)
            aux = aux.sig
