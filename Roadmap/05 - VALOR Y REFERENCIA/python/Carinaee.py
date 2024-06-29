"""
valor y referencia
"""

# tipo de dato por valor, es un elemento unico que si se mezcla con otras variables crean un nuevo elemento

entero_a = 10
entero_b = 20
print(entero_a)
print(entero_b)

#tipo de datos por referencia (como listas, tuplas, diccionaios y sets), estos heredan la posición por memoria
mi_lista_a = [10, 20, 30, 40]
mi_lista_b = [50, 60, 70, 80]

mi_lista_a = mi_lista_b

print(mi_lista_a)
print(mi_lista_b)


#  funciones con datos por referenca
def lista_func(mi_list: list):
    mi_list.append(30)

    mi_list_d = mi_list
    mi_list_d.append(40)

    print(mi_list)
    print(mi_list_d)

mi_list_c = [10,20]
my_list_func(mi_list_c)
print(mi_list_c)


"""
dificultad extra

"""
# por valor

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = value_b
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

#por referencia 

def ref(value_a: list, value_b: list) -> tuple:
    temp = value value_a
    value_a = value_b
    value_b =  temp
    return value_a, value_b

my_list_e = [10, 20]
my_list_f = [30, 40]

my_list_g, my_list_h = ref(my_list_e, my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")










