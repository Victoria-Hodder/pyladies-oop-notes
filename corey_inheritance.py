"""
Learn inheritance from : https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5&t=0s

"""

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


class Developer(Employee):
    raise_amt = 1.10 #changing this doesn't affect the parent class

    def __init__ (self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__ (self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)


    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev1 = Developer('Victoria', 'Hodder', 65000, 'Python')
dev2 = Developer('Bob', 'Dings', 50000, 'JavaScript')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev1])

print(mgr_1.fullname())

mgr_1.add_employee(dev2)
mgr_1.remove_employee(dev1)
mgr_1.print_emps()


"""
print(help(Developer)) - useful command

isinstance()
issubclass()
rewatch this part...
"""