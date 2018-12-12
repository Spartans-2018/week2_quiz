class Animal:
    name = None
    species = None

    def __init__(self, name):
        name = self.name

    def make_noise(self):
        print(5 * '\n')

class Tiger(Animal):
    def __init__(self, name):
        self.name = name
        self.species = "Tiger"

    def make_noise(self):
        print("Roar!")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.species = "Dog"

    def make_noise(self):
        print("Bark!")

class Cow(Animal):
    def __init__(self, name):
        self.name = name
        self.species = "Cow"

    def make_noise(self):
        print("Moo!")

class Zoo:
    animals = []
    def __init__(self):
        pass

    def add(self, objname):
        if not (isinstance(objname, Tiger) or isinstance(objname, Cow) or isinstance(objname, Dog)  or isinstance(objname, Animal)):
            raise Exception("Not a subclass")
        self.animals.append(objname)

    def show_animals(self):
        for i in self.animals:
            print(f"{i.name} the {i.species}")
            i.make_noise()

mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)



zoo.show_animals()










