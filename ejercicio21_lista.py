from tda_lista import Lista

class Pelicula:

    def __init__(self, nombre, valoracion_publico, anio_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion_publico = valoracion_publico
        self.anio_estreno = anio_estreno
        self.recaudacion = recaudacion
    
    def __str__(self):
        return f'{self.nombre}, {self.valoracion_publico}, {self.anio_estreno}, {self.recaudacion}'

lista_peliculas = Lista()

peliculas = [
    {'name': 'la momia', 'vp': 8, 'ae': 1999,  'rec': 91600000},
    {'name': 'terminator', 'vp': 10, 'ae': 1984,  'rec': 78000000},
    {'name': 'mortal kombat', 'vp': 7, 'ae': 1995,  'rec': 122000000},
    {'name': 'resident evil', 'vp': 9, 'ae': 2002,  'rec': 103000000},
    {'name': 'rapido y furioso', 'vp': 10, 'ae': 2001, 'rec': 207000000},
]

for pelicula in peliculas:
    lista_peliculas.insertar(Pelicula(pelicula['name'],
                                           pelicula['vp'],
                                           pelicula['ae'],
                                           pelicula['rec']), 'nombre')


lista_peliculas.barrido()
print('ingrese el año de estreno')
anio_elegido=int(input())
lista_peliculas.barrido_por_anio(anio_elegido)
print()
pos=lista_peliculas.mayor_de_lista('recaudacion')
print(f'pelicula que mas recaudo: {pos.info}')
print()
lista_peliculas.barrido_mayor_valoracion()
lista_peliculas2 = Lista()
criterios=['nombre', 'recaudacion', 'anio_estreno', 'valoracion_publico']
dicc=['name', 'rec', 'ae', 'vp']
var=0
for crit in criterios:
    for pelicula in peliculas:
        lista_peliculas2.insertar(Pelicula(pelicula['name'],
                                            pelicula['vp'],
                                            pelicula['ae'],
                                            pelicula['rec']), crit)
    print()
    print(f'listado ordenado por  {crit}')
    lista_peliculas2.barrido()
    for pelicula in peliculas:
        lista_peliculas2.eliminar(pelicula[dicc[var]], crit)
    var+=1