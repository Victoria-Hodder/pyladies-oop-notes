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

#next time write a child class which inherits from Pyladies

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
print(Jane.fave_subjects("OOP and butterflies"))


"""
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return f"{self.name} sings {song}"

    def dance(self):
        return f"{self.name} is now dancing"

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print(f"Blu is a {blu.__class__.species}")
print(f"Woo is also a {woo.__class__.species}"

# access the instance attributes
print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")


# parent class
class Bird():
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

"""

"""
Resources:
https://www.programiz.com/python-programming/object-oriented-programming
Corey Schafer - OOP tutorials
(put links in slide)
https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/

"""