""" Inheritance """

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
Resource: https://www.programiz.com/python-programming/object-oriented-programming
"""