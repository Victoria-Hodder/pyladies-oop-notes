""" Improving my oop knowledge with class/static methods """

class Pyladies:
    # class attribute/variable
    category = "Pythonista\n"

    def __init__(self, name, strength, job): # parameters/arguments
        self.name = name     # instance attribute/variable
        self.strength = strength
        self.job = job
    # __init__ (called constructor in other languages)

    # instance method (a function that is associated with a class)
    def skills(self):
        return f"\n{self.name} is a {self.job} who is really good at {self.strength}\n"

    def typing(self):
        return f"\n{self.name} is now typing\n"

    def learning(self, subject):
        return f"\n{self.name} loves to learn about {subject}\n"

    # adding a class method
    @classmethod
    def flask(cls):
        return f"I like to use Flask!"

    @classmethod
    def django(cls):
        return f"I like to use Django!"




flask = Pyladies.flask()
django = Pyladies.django()

print(flask)
print(django)

"""
Resources: https://realpython.com/instance-class-and-static-methods-demystified/#class-methods

"""