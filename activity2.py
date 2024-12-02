class Animal:
    def move(self):
        pass  

class Dog(Animal):
    def move(self):
        print("Dog is running")

class Bird(Animal):
    def move(self):
        print("Bird is flying")

class Car(Animal):  
    def move(self):
        print("Car is driving")

class Plane(Animal):
    def move(self):
        print("Plane is flying")

# Creating objects and calling the move() method
dog = Dog()
bird = Bird()
car = Car()
plane = Plane()

dog.move()
bird.move()
car.move()
plane.move()