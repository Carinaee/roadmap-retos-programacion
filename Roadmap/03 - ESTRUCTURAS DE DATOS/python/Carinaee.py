"""
Estructuras
"""

# Listas
my_list: list = ["Brais", "Bl4ck", "Wolfy", "Visionos"]
print(my_list)
my_list.append("Castor")  # Inserción
my_list.append("Castor")
print(my_list)
my_list.remove("Brais")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Cuervillo"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("mouredev@gmail.com")  # Inserción
my_set.add("mouredev@gmail.com")
print(my_set)
my_set.remove("Moure")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))

#Diccionario se crea entre llaves con clave, no son ordenados

mi_dict: dict = {"name":"moure"}

mi_dict["name"] = "seeb" #insertar dato




def mi_agenda():
  
  is_on = True
  
  while True:

  print("")
  print("1. buscar contacto")
  print("2. insertar contacto")
  print("3. actualizar contacto")
  print("4. eliminar contacto")
  print("5. Salir")

  option = input("\nselecciona una opcion: ")

  match option:
    case "1":
        name = input("introduce nombre")
        if name in agenda:
            print(f"el nmero de telefono de {agenda[name]} es {}"}
        else:
          print:(f"el contacto de telefono {name} no existe")
          
    case "2":
        name = input("introduce nombre")
        phone = input("introduce telefono")
        if phone.isdigit() and len(phone) > 0 len(phone) <= 11:
        else:
          print(
              "debes introducir un numero de telefono con menos de 12 digitos")
    case "3":
        name = input ("introduce el nombre de contacto a actualizar")
        if name in agenda:
        name = input("introduce nombre")
        phone = input("introduce telefono")
        if phone.isdigit() and len(phone) > 0 len(phone) <= 11:
        else:
          print(
              "debes introducir un numero de telefono con menos de 12 digitos")
    case "4"
        name = input ("introduce el nombre de contacto a eliminar")
        if name in agenda:
          del agenda[dane]
    case "5"
        print("saliendo de la agenda")
        break
    case _:
        print("opcion no valida, elige de 1 al 5")
  
  if option == "1"

mi_agenda()













