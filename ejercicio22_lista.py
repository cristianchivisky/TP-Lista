from lista import Lista

class Jedi:

    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"

lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('jedis.txt')
lineas = file.readlines()

lineas.pop(0)  
for linea in lineas:
    datos = linea.split(';')
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')
   
lista_jedi.barrido()
print()
lista_jedi2.barrido()

dato = lista_jedi.busqueda('ahsoka tano', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')
dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')
print()
print('padawan de joda y luke:')
lista_jedi.barrido_jedi_master()
print()
print('jedis especie humana y twilek:')
lista_jedi2.barrido_jedi_especie()
print()
print('jedis que empiezan con a:')
lista_jedi.barrido_comienza_con(['a'])
print()
print('jedis que usaron sables de distintos colores:')
lista_jedi.barrido_sable_mas_de_un_color()
print()
print('jedis que usaron sable amarillo o violeta:')
lista_jedi.barrido_jedi_sable()
print()
lista_jedi.barrido_padawans()