"""
excepciones
"""
try:
    print (10/1)
    print([1, 2, 3, 4][4])

except Exception as e:
    print(f"se ha producido un error: {type(e).__name__}")

"""
Tarea extra
"""
class StrTypeError(Exception):
   pass 

def process_params(parameters: list):
  if len(parameters) < 3:
      raise IndexError()
  elif parameters[1] == 0:
      raise ZeroDivisionError()
  elif type(parameters[2]) == str:
      raise StrTypeError(
          "el segundo elemento no puede ser texto")
    
  print(parameters[2])
  print(parameters[0]/parameters[1])
  
try:
  process_params([1, 2, 3, 4])
except IndexError as e:
  print("El numero de elementos de una lista debe ser mayor que dos")
except ZeroDivisionError as e:
  print("El segundo de elemento de la lista mayor a 0")
except StrTypeError as e:
  print(f"{e}")
except Exception as e:
  print(f"error inesperado: {e}")
else:
    print("no se produjo ningun error")
finally:
  print("El programa finaliza")














