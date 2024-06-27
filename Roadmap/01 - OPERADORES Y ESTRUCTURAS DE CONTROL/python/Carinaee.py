"""
funciones de usuario
"""

# Simple

def func():
  print("Hola mundo de la programación!")

func()

#esta función tiene retorno

def func_retorno():
  return "hola, estimado mundoo"

print(func_retorno())

#funcion con un argumento

def func_arg(nombre):
  print(f"Hola, {nombre}!")


func_arg("mundooo")

#funciones varios con argumentos

def funct_arg(func, name):
  print(f"{func}, {name}!")

funct_arg("Holaaa", "Vida")
funct_arg(func="Holaaa", name="Vida")


# argumento predeterminado

def pred_arg_func(name="Python"):
  print(f"Hola, {Python}!")

# funcion con argumentos y retorno

def return_arg_func(func, name)
  return f"{func}, {name}!"

print(return_arg_("Hi", "amigo"))

#funcion con retorno de varios valores 

def mulp_val_func():
  return "Hola", "hermoso", "python", "y", "mundo"

greet, name = mulp_val_func()
print(name)
print(greet)

# con numero varibales de arg

def  variab_arg_func(*name)
 for name in names:
  print(f"hola, {name}!}"

# funcion con un numero variable de argumentos

def variable_arg_funct(*names)
  for name in names:
    print(f"Hola, mundo"
        
variable_arg_func("Hola", "mundo", "de", "programación)

# funcion con numero variable de argumentos con palabra clave

def variable_arg_func(**names):
  for key, value in names.items():
    print(f"{value} ({key})!")

variable_arg_func(
  language="Python",
  name="Seeb",
  alias="Cheeb",
  age="1"
)


"""
Funcion al interior de otras funciones

"""
print(len("Sebb"))
print(type(1))
print("Sebb".upper())

"""
Una variable local y global

"""

global_var = "Python"
  local_var = "Hola"
  print(f"{local_var}, {global_var}!")


print(f"{local_var}, {global_var}!")

print(global_var)
  
hellow_python

""" 
reto extra
"""

def print_numbers(text_1, text_2) -> int:
  count = 0
    for number in range (1, 101)
      if number % 3 == 0 and number % 5 == 0:
        print(text_1 + text_2)
      elif number % 3 == 0:
        print(text_1)
      elif number % 5 == 0:
        print(text_2)
      else:
        print(number)
        count += 1
      return count

print(print_numbers("holaa", "holaa"))
























