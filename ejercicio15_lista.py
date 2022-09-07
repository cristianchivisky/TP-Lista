from tda_lista import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return f'{self.nombre} - torneos ganados: {self.torneos_ganados} - batallas ganadas: {self.batallas_ganadas} - batallas perdidas: {self.batallas_perdidas}'

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - nivel: {self.nivel} - tipo: {self.tipo} - subtipo: {self.subtipo}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'tyrantrum', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'charizard', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'terrakion', 'nivel': 90, 'tipo': 'planta', 'subtipo': 'lucha'},
    {'name': 'bulbasur', 'nivel': 20, 'tipo': 'agua', 'subtipo': 'volador'},
    {'name': 'charmander', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'wingull', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]

for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista() 
print()   
entrenador = input('ingrese nombre del entrenador: ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
else:
    print('el entrenador no esta en la lista')
print()
print('entrenador con mas de tres torneos ganados:')
lista_entrenadores.barrido_entrenador_mas_tres()
print()
print('pokemon de mayor nivel del entrenador con mas torneos ganados:')
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)
print()
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"datos del entrenador:  {pos.info}")
    print('sus pokemons: ')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')
print()
print('entrenadores con porcentaje de batallas ganadas superior al 79% :')
lista_entrenadores.barrido_porcentaje_victorias()
print()
lista_entrenadores.barrido_tipo_pokemons()
print()
entrenador=input('ingrese el nombre del entrenador: ')
lista_entrenadores.barrido_promedio_nivel_pokemons(entrenador)
print()
var1 = input('ingrese nombre del pokemon: ')
lista_entrenadores.barrido_lista_lista_pokemon(var1)
print()
lista_entrenadores.barrido_pokemon_repetidos()
print()
lista_entrenadores.barrido_pokemons_especificos()
print()
var2=input('ingrese el nombre del entrenador: ')
var3=input('ingrese el nombre del pokemon: ')
lista_entrenadores.barrido_entrenador_pokemon(var2, var3)
