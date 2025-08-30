# This program demonstrates core object-oriented programming (OOP) concepts in Python.
# 1. A custom class with inheritance (Superhero and Sidekick).
# 2. A polymorphism challenge with vehicles.

import random

# -----Activity 1: Superhero Class Design with Inheritance-------

class Superhero:
   
    def __init__(self, name, superpower, identity):
        #Initializes a new Superhero object.
        self.name = name
        self.superpower = superpower
        self.identity = identity
        print(f"Created a new superhero: {self.name}!")

    def introduce_self(self):
        #Prints a brief introduction of the hero.
        print(f"I am {self.name}! My secret identity is {self.identity}.")

    def use_superpower(self):
        #Prints a dynamic message about the hero using their power.
        print(f"{self.name} unleashes the power of {self.superpower}!")


class Sidekick(Superhero):
   
    def __init__(self, name, superpower, identity, mentor):
        #Initializes a new Sidekick object, calling the parent constructor first.
        super().__init__(name, superpower, identity) # Call the parent class's constructor
        self.mentor = mentor
        print(f"And I'm a sidekick to {self.mentor}!")
        
    def use_superpower(self):
        # Prints a dynamic message about the sidekick using their power.
        print(f"Under the watchful eye of {self.mentor}, {self.name} uses their power of {self.superpower}!")


# ---Activity 2: Polymorphism Challenge with Vehicles ----

class Vehicle:
    #A generic base class for a vehicle.

    def move(self):
        "Defines a generic move action. This will be overridden by subclasses."
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    #A Car class that moves by driving.
    def move(self):
        print("Driving")

class Plane(Vehicle):
    #A Plane class that moves by flying.
    def move(self):
        print("Flying")

class Boat(Vehicle):
    #A Boat class that moves by sailing.
    def move(self):
        print("Sailing")


# Program Execution: Demonstrating the Classes 

if __name__ == "__main__":
    print("#Demonstrating Activity 1: Superhero Class ")
    
    # Create an instance of the Superhero class
    superman = Superhero("Superman", "flight and super strength", "Clark Kent")
    superman.introduce_self()
    superman.use_superpower()
    print("-" * 20)
    
    # Create an instance of the Sidekick subclass
    robin = Sidekick("Robin", "acrobatics and martial arts", "Dick Grayson", "Batman")
    robin.introduce_self()
    robin.use_superpower()
    print("\n")

    print(" #Demonstrating Activity 2: Polymorphism Challenge")

    # Create a list of different vehicle objects
    vehicles = [Car(), Plane(), Boat()]
    
    # Loop through the list and call the 'move' method on each object.
    # The same method call, 'vehicle.move()', produces a different result
    # for each object, which is the essence of polymorphism!
    for vehicle in vehicles:
        vehicle.move()
