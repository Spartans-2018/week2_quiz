import inspect


class Animal:
    species=None
    def __init__(self, name):
        self.name=name
        self.species=None

class Tiger(Animal):


    def __init__(self, name):
        self.name=name
        self.species="the Tiger"


    def make_noise(self):
        print("Roar!")

class Dog(Animal):

    def __init__(self, name):
        self.name=name
        self.species="The Dog"

    def make_noise(self):
        print("Bark!")

class Cow(Animal):


    def __init__(self, name):
        self.name=name
        self.species="The Cow"


    def make_noise(self):
        print("Moo!")


class Zoo:


    def __init__(self):
        self.animals=[]

    def add(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

        else:
            raise Exception("Not valid animal")


    def show_animals(self):

        for item in self.animals:
            print(item.name, item.species)
            item.make_noise()


mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")
lion='king'


zoo = Zoo()
zoo.add(mike)

zoo.add(molly)
zoo.add(bessie)

zoo.show_animals()
zoo.add(lion)
