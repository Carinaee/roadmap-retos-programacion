"""
Manejo de ficheros   UN BARRA \n ,ES UN SALTO DE LINEA
"""
import os
file_name="Carinaee.txt"

with open(file_name, "w") as file:
  file.write("seeb\n")
  file.write("30\n")
  file.write("python")

with open(file_name, "r") as file:
  print(file.read())

os.remove(file_name)


"""
ejercicio extra
"""


while True:
  print("1.")
  print("2.")
  print("3.")
  print("4.")
  print("5.")
  print("6.")
  print("7.")

  option = input("selecciona una opcion")

  if option == "1":
    nombre = input("Nombre: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")
    with open(file_name, "a") as file:
        file.write(f"{nombre}, {cantidad}, {precio}\n")

  elif option == "2":
    name = input ("Nombre: ")
    with open(file_name, "r") as file:
        for line in file.readlines():
          line.split(", ")[0] == name:
            print(line)
            break
          
  elif option == "3":
    nombre = input("Nombre: ")
    cantidad = input("Cantidad: ")
    precio = input("Precio: ")
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
           if line.split(", ")[0] == nombre:
               file.write(f"{nombre}, {cantidad}, {precio}\n")
        else: 
          file.write(line)
          
  elif option == "4":
    nombre = input("Nombre: ")
    with open(file_name, "r") as file:
        lines = file.readlines()
    with open(file_name, "w") as file:
        for line in lines:
           if line.split(", ")[0] != nombre:
                file.write(line)
  
  elif option == "5":
    with open(file_name, "r") as file:
        print(file.read())
  
  elif option == "6":
    name = input("Nombre: ")
    total = 0
    with open(file_name, "r") as file:
        for line in file.readlines():
            components = line.split(", ")
            if components [0] == name:
              quantity = (components[1])
              price = float(components[2])
              total += quantity *price
              break
          print(total)
      
  elif option == "7":
    #os.remove(file_name)
    break
  else:
    print("selecciona una opcion (de 1 al 7)")




