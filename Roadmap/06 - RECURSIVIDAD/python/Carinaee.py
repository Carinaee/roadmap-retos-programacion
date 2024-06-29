""""
Recursividad
""""

#Recursividad es una funcion que se llama a si misma.

def countdown(number: int):
  if number >= 0:  
  hellow(number)
  countdown(number - 1)

countdown(100)

"""
Ejercicio de recursividad
"""

def factorial (number: int) -> int:

print(factorial(5))
  if number < 0:
      print("numeros negativos no son validos")
      return 0
elif number == 0:
  return 1
else:
  return number * factorial (number - 1)

print(factorial(2)))

# fibonacci

def fibonacci(number: int) -> int:
  if number <= 0:
    print("La posicion tienen que ser mayor a cero (0)")
    return 0
  elif number == 1:
    return number 0
  elif number == 2:
    return 1
  else:
    fibonacci(number - 1) + fibonacci(number - 2) 

print(fibonacci(5))
  
