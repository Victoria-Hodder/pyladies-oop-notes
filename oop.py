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

class Empty:
    pass

# parent class
class Pyladies:
    #class attribute/variable
    category = "Pythonista"

    #instance attribute/variable
    # __init__ also known as a constructor
    def __init__(self, name, strength, job):
        self.name = name
        self.strength = strength
        self.job = job

    #instance method
    def description(self):
        return f"{self.name} is a {self.job} who is really good at {self.strength}"

    def fave_subjects(self, subject):
        return f"{self.name} loves to learn about {subject}"


# instantiate object
Victoria = Pyladies("Victoria", "Django", "Software Developer")
Jane = Pyladies("Jane", "Keras", "Data Scientist")

#access class attribute
print(f"Victoria is a {Victoria.__class__.category}")
print(f"Jane is also a {Jane.__class__.category}")

# call instance methods
print(Victoria.description())
print(Jane.description())

print(Victoria.fave_subjects("Docker"))
print(Jane.fave_subjects("OOP and butterflies\n"))


#parent class
class Developers():

    def __init__(self):
        print("Developer is ready\n")

    def whoisThis(self):
        print("Developer\n")

    def typing(self):
        print("Type faster\n")


#child class
class DjangoUser(Developers):

    def __init__(self):
        # call super() function
        super().__init__() # not sure what this is for??!?!?! 
        print("DjangoUser is ready\n")

    def whoisThis(self):
        print("DjangoUser\n")

    def migrate(self):
        print("Migrate faster\n")

sam = Developers()
victoria = DjangoUser()
sam.whoisThis()
victoria.whoisThis()
sam.typing()
victoria.migrate()

"""
Resources:
https://www.programiz.com/python-programming/object-oriented-programming
Corey Schafer - OOP tutorials
(put links in slide)
https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/

"""