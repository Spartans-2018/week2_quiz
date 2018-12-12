import inspect

class Animal:
    """Animal has a property called "species" and a property called "name". "species" is initialized to None, "name" is set by an argument to the constructor."""

    species = "None"

    def __init__(self, name):
        self.name = name
        
    def make_noise(self):
        # print()
        return print()

# Tiger's species property is "tiger" and its "make_noise()" method prints out "Roar!"
class Tiger(Animal):
    species = "the tiger"

    def make_noise(self):
        return("Roar!")


# Dog's species property is "dog" and its "make_noise()" method prints out "Bark!"
class Dog(Animal):
    species = "the dog"

    def make_noise(self):
        return("Bark!")

# Cow' species property is "cow" and its "make_noise()" method prints out "Moo!"
class Cow(Animal):
    species = "the cow"

    def make_noise(self):
        return("Moo!")

#  --------------------------------------------
class Zoo:

    animals=[]
    def __init__(self):
        pass

    def add(self, animal):
        if(inspect.isclass(animal)):
            return self.animals.append(animal)
        else:
            # instance of Animal or subclass
            raise Exception("Input is not an instance or Subclass of Animal")
         
    def show_animals(self):
        for animal in self.animals:
            print(animal.name +" " + animal.species)
            print(animal.make_noise())


# ---------- test  ----------
mike = Tiger("Mike")
molly = Dog("Molly")
bessie = Cow("Bessie")

zoo = Zoo()
zoo.add(mike)
zoo.add(molly)
zoo.add(bessie)

zoo.show_animals()
# Mike the tiger
# Roar!
# Molly the dog
# Bark!
# Bessie the cow
# Moo!

zoo.add("bad value") # should raise an exception