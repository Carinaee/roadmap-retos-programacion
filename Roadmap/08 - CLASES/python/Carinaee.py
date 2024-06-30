"""
Clases
"""

#clase, es para Programación orientada a objetos, es para crear nuevas entidades / programas

class Programador:
  surname: str = None

  def __init__(self, name: str, age: int, language: list):
      self.name = name
      self.age = age
      self.language = language

  def print(self):
      print(
          f"Nombre: {sel.name} | Edad: {self.age} | Lenguaje: {self.language}")

mi_programador = Programador("Sebastian, "30", ["Python"])
mi_programador.print()
mi_programador.surname = "Seeb"
mi_programador.print()
mi_programador.age = 30
mi_programador.print()

"""
Pila y cola con clases
"""

#LIFO 
Class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
          return None
        return self.stack.pop()

    def count(self):
        for item in reversed(stack.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C") 
print(my_stack.count())
my_stack.print()
my_stack.pop()


#FIFO

class Queue:

  def __init__(self):
      self.queue = []

  def equeue(self, item):
      self.queue.append(item)

  def dequeue(self):
              if sefl.count() == 0:
          return None
      return self.queue.pop(0)

  def count(self):
      return len(self.queue)

  def print(Self):
      for item in self.queue:
          print(item)




my_queue = Queue()
my_queue.queue("A")
my_queue.queue("B")
my_queue.queue("c")
print(my_queue.count())
my_queue.print()
my_queue.dequeue

