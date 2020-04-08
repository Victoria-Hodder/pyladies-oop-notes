def printPyLadies():
    print("Yay, PyLadies")

print(printPyLadies())

statement = printPyLadies()
print(statement)

class Empty:
   pass

class Pyladies:
    #class attribute/variable
    category = "Pythonista"

    def __init__(self, name, strength, job): #parameters/arguments
        self.name = name     #instance attribute/variable
        self.strength = strength
        self.job = job
    # __init__ (called constructor in other languages)

    #instance method (a function that is associated with a class)
    def skills(self):
        return f"{self.name} is a {self.job} who is really good at {self.strength}"    

    def typing(self):
        return f"{self.name} is now typing"

    def learning(self, subject):
        return f"{self.name} loves to learn about {subject}"


# instantiate object
Victoria = Pyladies("Victoria", "Django", "Software Developer")
Jane = Pyladies("Jane", "Keras", "Data Scientist")

#access class attribute
print(f"Victoria is a {Victoria.__class__.category}")
print(f"Jane is also a {Jane.__class__.category}")

# call instance methods
print(Victoria.skills())
print(Jane.skills())

print(Victoria.typing())

print(Victoria.learning("Docker"))
print(Jane.learning("OOP and butterflies"))


"""
Resources:
https://www.programiz.com/python-programming/object-oriented-programming
Corey Schafer - OOP tutorials
(put links in slide)
https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/
https://medium.com/swlh/everything-is-an-object-in-python-learn-to-use-functions-as-objects-ace7f30e283e


"""