"""Same content as oop.py, for copy and paste purposes during the presentation"""

class Pyladies:
    #class attribute/variable
    category = "Pythonista\n"

    def __init__(self, name, strength, job): #parameters/arguments
        self.name = name     #instance attribute/variable
        self.strength = strength
        self.job = job
    # __init__ (called constructor in other languages)

    #instance method (a function that is associated with a class)
    def skills(self):
        return f"\n{self.name} is a {self.job} who is really good at {self.strength}\n"

    def typing(self):
        return f"\n{self.name} is now typing\n"

    def learning(self, subject):
        return f"\n{self.name} loves to learn about {subject}\n"


# instantiate object
Victoria = Pyladies("Victoria", "Django", "Software Developer")
Jane = Pyladies("Jane", "Keras", "Data Scientist")


#access class attribute
print(f"\nVictoria is a {Victoria.category}")
print(f"Jane is also a {Jane.category}")

# call instance methods
print(Jane.skills())
print(Victoria.skills())

print(Jane.typing())
print(Victoria.typing())

print(Jane.learning("statistics"))
print(Victoria.learning("Docker"))


