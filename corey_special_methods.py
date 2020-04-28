class Employee:
    raise_amt = 1.04

    def __init__ (self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): # for developers
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self): # for users
        return f'{self.fullname()} - {self.email}'

    def __add__ (self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Victoria', 'Hodder', 65000)
emp_2 = Employee('Bob', 'Dings', 50000)

print(len(emp_1))

# print(emp_1)

# print(repr(emp_1))
# print(str(emp_1))

