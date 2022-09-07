def criterio(dato, campo=None):
    dic = []
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

    def barrido_lista_lista_pokemon(self, pok):
        aux = self.__inicio
        cont=0
        aux2=False
        while(aux is not None):
            aux1=aux.sublista.__inicio
            while(aux1 is not None):
                if aux1.info.nombre == pok:
                    aux2=True
                aux1=aux1.sig
            if aux2:
                cont+=1
            aux2=False
            aux = aux.sig
        print(f'cant de entrenadores que tienen al pokemon {pok} = {cont}')

    def barrido_pokemon_repetidos(self):
        aux = self.__inicio
        cont=0
        while(aux is not None):
            aux1=aux.sublista.__inicio
            while(aux1 is not None):
                var=aux1.info.nombre
                aux1=aux1.sig
                if aux1 is not None and var == aux1.info.nombre:
                    cont+=1
            if cont>0:
                print(f' el entrenador {aux.info.nombre} tiene pokemons repetidos')
            aux = aux.sig
        

    def barrido_promedio_nivel_pokemons(self, entr):
        aux = self.__inicio
        cont=0
        aux2=0
        while(aux is not None):
            if aux.info.nombre ==entr:
                aux1=aux.sublista.__inicio
                while(aux1 is not None):
                    aux2=aux2+ aux1.info.nivel
                    cont+=1
                    aux1=aux1.sig
            aux = aux.sig
        if cont != 0:
            print(f'promedio del nivel de los pokemons de {entr} = {aux2/cont}')
        else:
            print('no se encontro el entrenador')

    def barrido_pokemons_especificos(self):
        aux = self.__inicio
        while(aux is not None):
            aux1=aux.sublista.__inicio
            while(aux1 is not None):
                if aux1.info.nombre in ['tyrantrum', 'terrakion', 'wingull', 'pok4']:
                    print(f'el entrenador {aux.info.nombre} posee el pokemon {aux1.info.nombre}')
                aux1=aux1.sig
            aux = aux.sig
    
    def barrido_tipo_pokemons(self):
        aux = self.__inicio
        while(aux is not None):
            var=False
            var1=False 
            var2=False
            aux1=aux.sublista.__inicio
            while(aux1 is not None):
                if aux1.info.tipo =='fuego':
                    var=True 
                if aux1.info.tipo == 'planta':
                    var1=True
                if aux1.info.tipo == 'agua' and aux1.info.subtipo == 'volador':
                    var2=True
                aux1=aux1.sig
            if var and var1:
                print(f'el entrenador {aux.info.nombre} posee pokemons del tipo fuego y planta')
            if var2:
                print(f'el entrenador {aux.info.nombre} posee pokemon de tipo agua y subtipo volador' )
            aux = aux.sig
    
    def barrido_entrenador_pokemon(self, entr, pok):
        aux = self.__inicio
        aux2=True
        while(aux is not None):
            aux1=aux.sublista.__inicio
            while(aux1 is not None):
                if aux1.info.nombre == pok and aux.info.nombre == entr:
                    print(f'el entrenador {aux.info} posee el pokemon {aux1.info}')
                    aux2=False
                aux1=aux1.sig
            aux = aux.sig
        if aux2:
            print(f'el entrenador {entr} no posee al pokemon {pok}')
    
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
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_jedi_especie(self):
        aux = self.__inicio
        while(aux is not None):
            if('human' in aux.info.especie or "twi'lek" in aux.info.especie):
                print(aux.info)
            aux = aux.sig

    def barrido_sable_mas_de_un_color(self):
        aux = self.__inicio
        while(aux is not None):
            if(len(aux.info.sable_luz) > 1):
                print(aux.info)
            aux = aux.sig

    def barrido_jedi_sable(self):
        aux = self.__inicio
        while(aux is not None):
            if('yellow' in aux.info.sable_luz or 'violet' in aux.info.sable_luz):
                print(aux.info)
            aux = aux.sig

    def barrido_padawans(self):
        aux = self.__inicio
        var1= True
        var2 = True
        while(aux is not None):
            if('qui-gon jin' in aux.info.maestro): 
                print(f'padawan de qui-gon jin:  {aux.info.nombre}')
                var1=False
            elif('mace windu' in aux.info.maestro):
                print(f'padawans de mace windu:  {aux.info.nombre}')
                var2=False
            aux = aux.sig
        if var1:
            print('qui-gon jin no tiene padawans')
        if var2:
            print('mace windu no tiene padawans')
    
    def barrido_owen_grady(self):
        aux = self.__inicio
        while(aux is not None):
            if('Raptors' in aux.info.nombre or 'Carnootaurus' in aux.info.nombre):
                print(aux.info)
            if('Compsognathus' in aux.info.nombre):
                print('Codigo donde puedes encontrar Compsognathus: ', aux.info.zona)
            aux = aux.sig
    
    def barrido_simon_masrani(self):#Tyrannosaurus Rex, Spinosaurus, Giganotosaurus 
        aux = self.__inicio #nivel ´critical’ o ‘high’.
        while(aux is not None):
            if(('Tyrannosaurus Rex' in aux.info.nombre or 'Spinosaurus' in aux.info.nombre or 'Giganotosaurus' in aux.info.nombre) and ('critical' in aux.info.nivel_alerta or 'high' in aux.info.nivel_alerta)):
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


    def barrido_por_anio(self, dato):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.anio_estreno == dato):
                print(aux.info)
            aux = aux.sig

    def barrido_mayor_recaudacion(self):
        aux = self.__inicio
        var=0
        var1=None
        while(aux is not None):
            if aux.info.recaudacion > var:
                var=aux.info.recaudacion
                var1=aux
            aux = aux.sig
        print(f'la pelicula que mas recaudo es {var1.info}')

    def barrido_mayor_valoracion(self):
        aux = self.__inicio
        var=0
        var1=[]
        while(aux is not None):
            if aux.info.valoracion_publico > var:
                var=aux.info.valoracion_publico
                var1=[]
                var1.append(aux.info.nombre)
            elif aux.info.valoracion_publico == var:
                var1.append(aux.info.nombre)
            aux = aux.sig
        print(f'pelicula/s con mayor valoracion: {var1}')

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
    
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                
            aux = aux.sig
        return mayor

