class Dog():
    # Class obj attributes
    # similar to static var in C++
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
        print("{} {} {}".format(self.breed, self.name, self.spots))

    def displayDogInfo(self):
        print("{} {} {}".format(self.breed, self.name, self.spots))
    
    def __str__(self):
        return f"{self.breed}, {self.name}, {self.spots}"

    def __len__(self):
        return len(self.breed) + len(self.name)
    
    def __del__(self):
        print("Deleted {}".format(self.name))

class Circle():
    # Class obj attributes
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = Circle.pi * radius * radius
    
    def getCircumference(self):
        return 2 * Circle.pi * self.radius
    
    def getRadius(self):
        return Circle.pi * self.radius * self.radius

class Animal():
    def __init__(self):
        print("Animal created")
    
    def whoAmI(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")
    
    def whoAmI(self):
        print("I am a cat")

class Cow(Animal, Dog):
    def __init__(self):
        Animal.__init__(self)
        Dog.__init__(self, 'Lab', 'Tommy', True)
        print("Cow created")
    
    def whoAmI(self):
        print("I am a cow")

if __name__ == '__main__':
    myDog = Dog('Labrador', 'Sammy', False)
    myDog.name = 'Chu'
    myDog.displayDogInfo()

    myCircle = Circle(20)
    print(myCircle.getCircumference())
    print(myCircle.getRadius())

    myCat = Cat()
    myCat.whoAmI()
    myCat.eat()

    myCow = Cow()
    myCow.whoAmI()

    #myAnimal = Animal()
    #myAnimal.speak()

    for pet in [myCat, myCow]:
        print(type(pet))
        print(pet.whoAmI())

    print(myDog)
    print(len(myDog))
    del myDog
