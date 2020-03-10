class Animal:
  def __init__(self, Animal):
    print(Animal, 'is an animal.')

class Mammal(Animal):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    super().__init__(mammalName)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammal):
    print(NonWingedMammal, "can't fly.")
    super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammal):
    print(NonMarineMammal, "can't swim.")
    super().__init__(NonMarineMammal)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.')
    super().__init__('Dog')
    
d = Dog()
print('')
bat = NonMarineMammal('Bat')

#resource: https://www.programiz.com/python-programming/methods/built-in/super

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