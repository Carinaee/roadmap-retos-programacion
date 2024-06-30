""""
Herencia y plimorfismo
"""

# mecanismo de la POO para heredar parametros, variables o valores de otra clase
# capacidad de una clase para tomar diferentes formas, ej  una clase se pueda comportar de una manera distinta a partir de otra clase
class Animal
      def __init__(self, name: str):
          self.name = name
      def sound():
          pass
        
class Dog(Animal):
    def sound():
        print("Guau")

class Cat(Animal):
    def sound():
        print("Miau")

def print_sound (animal.Animal):
    animal.sound()


my_animal = Animal("Animal")
my_animal.sound()
my_dog = Dog("Perro")
my_dog.sound()
my_cat = Cat("Gato")
my_cat.sound()

"""
Extra
"""

class Employee:
    def __init__(self, id:int, name:str)
        self.id = id
        self.name = name
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)


class Manager(Employee):
    
    def coordinate_projects():
        def __init__(self, id:int, name:str, project:str):
        super().__init__(id, name)
        self.project = project

class ProjectManager(Employee):
      print(f"{self.name} está coordinando su proyecto.")
  
class Programmer(Employee):
    def __init__(self, id:int, name:str, language:str):
        super().__init__(id, name)
        self.language = language
    
    def code(self):
        print(f"{self.name} esta programandoes {self.language}")

    def add(self, employee):
      print(
          f"un programador no tienen empleados a su cargo. {employee} no se añadira.") 

my_manager = Manager(1, "manager")
my_project_manager = ProyectManager(2, "Seeb", "proyecto 1")
my_project_manager2 = ProyectManager(2, "Seeb", "proyecto 2")
my_programmer = Programmer(4, "jus", "python")


my_manager.add






