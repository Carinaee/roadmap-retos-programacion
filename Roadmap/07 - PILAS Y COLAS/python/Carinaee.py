"""
Ejercicios
"""

# pilas / stack (ultimo en entrar primero en salir o LIFO)

stack = []

push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

#pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_items)

print(stack.pop())

print(stack)

# cola / queue (primero en entrar primero en salir FIFO)
#queue
queue.append(1)
queue.append(2)
queue.append(3)

queue_item = queue [0]
del queue[0]
print(queue_item)
print(queue.pop(0))

print(queue)

"""
extra
"""

def web_navegacion():
  stack = []
  
  while True
    action = input("Añade una url o interactua con palabras adelante/atras/salir:"
    )

    if action == "salir"":
        print("saliendo de la web)
        break
    elif action ==  "adelante":
        pass
    elif action == "atras":
        if len(stack) > 0
            stack.pop()
    else:
        stack.apeend(action)
    if len(stack) > 0:
        print(f"has navegado a la web: {stack[len(stack) - 1]}")
    else:
        print("estas en la pagina de inicio")
web_navegacion()


# impresora

def impresora_compartida():

  queue = []

  while True:

  action = input("añade un documento para imprimir: ")

    if action == "salir"
      break
    elif action == "imprimir"
      if len(queue) > 0
        print(f"imprimiendo: {queue.pop(0)}")
    else:
      queue.append(action)

    print(f"cola de impresión: {queue}")

impresora_compartida()






