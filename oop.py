"""
What the f**k is an attribute?

Purpose of talk:
    To explain basic principles of OOP
    Give an intro to terminology

    Why? Because this vocabulary comes up in tutorials, algorithm practice and, most importantly, interviews!
    Personal motivation: I didn't understand instructions until I started to get an idea for these concepts. Learning about it deepened
    my knowledge and understanding of Python. Then I met many other "Quereinsteiger"s like myself and found this was quite a common
    thing. So I decided to put together a little tutorial about it. Please bear in mind, I'm really touching the surface here and also
    there are still gaps in my knowledge, so if anyone wants to step in at any point and correct me please do! I will list resources
    I have used at the end so you can continue practicing and expanding your knowledge.

"""
def printPyLadies():
    print("Yay, PyLadies")

statement = printPyLadies()
print(statement)

class Empty:
    pass

class Pyladies:
    #class attribute/variable
    category = "Pythonista"

    #instance attribute/variable
    # __init__ also known as a constructor
    #Difference between attribute / variable here
    # why do we have this init method??

    def __init__(self, name, strength, job): #self = parameter, others = parameters passed as arguments
        self.name = name
        self.strength = strength
        self.job = job

    #instance method
    def skills(self):
        return f"{self.name} is a {self.job} who is really good at {self.strength}"    

    def typing(self):
        return f"{self.name} is now typing"

    def learning(self, subject):
        return f"{self.name} loves to learn about {subject}"

#self, name, strength, job
    

# instantiate object
Victoria = Pyladies("Victoria", "Django", "Software Developer")
Jane = Pyladies("Jane", "Keras", "Data Scientist")

#access class attribute
print(f"Victoria is a {Victoria.__class__.category}")
print(f"Jane is also a {Jane.__class__.category}")

# call instance methods
print(Victoria.skills())
print(Jane.skills())

print(Victoria.learning("Docker"))
print(Jane.learning("OOP and butterflies"))

print(Victoria.typing())



"""
Resources:
https://www.programiz.com/python-programming/object-oriented-programming
Corey Schafer - OOP tutorials
(put links in slide)
https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/
https://medium.com/swlh/everything-is-an-object-in-python-learn-to-use-functions-as-objects-ace7f30e283e


"""