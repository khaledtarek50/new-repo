# import datetime
import OOP_TEST
#   here we make a change
class Employee:
    @property
    def fullname(self):
        return self.fullname

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay, email):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first}{self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def employee_email(self):
        return f'{self.email}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee({self.first}, '{self.last}', {self.pay}, {self.email})"

    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, email, prog_lang):
        super().__init__(first, last, pay, email)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, email, employees=None):
        super().__init__(first, last, pay, email)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, email, prog_lang = emp_str.split('_')
        return cls(first, last, pay, email, prog_lang)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# print(Employee.num_of_emps)
dev_1 = Employee('Khaled', 'Tarek', 50000, 'KhaledTarek@gmail.com')
dev_2 = Developer('test', 'user', 60000, 'testuser@gmail.com', 'java')
mgr_1 = Manager('Sue', 'Smith', 90000, 'SueSmith@gmail.com', [dev_1])
dev_1.first = 'Jim'
print(dev_1.first)
print(dev_1.email)
print(dev_1.fullname())
# print(len(dev_1))
# print(dev_1 + dev_2)
# print(dev_1)
# print(repr(dev_1))
# print(str(dev_1))
# print(1+2)
# print(int.__add__(1, 2))
# print(str.__add__('a','b'))
# print(isinstance(mgr_1, Employee))  # is argument instance = self. from the second argument
# print(issubclass(Developer, Employee))  # is first argument subclass  the second argument

# print(mgr_1.email)
# # mgr_1.add_emp(dev_1)
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)
# mgr_1.print_emps()
# print(dev_1.email)
# print(dev_1.prog_lang)
# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_workday(my_date))
# emp_str_1 = 'John_doe_70000_KhaledTarek@gmail.com'
# # emp_str_2 = 'steve_smith_30000_testuser@gmail.com'
# emp_str_3 = 'jane_doe_90000_testuser2@gmail.com'
# new_emp_1 = Employee.from_string(emp_str_3)
# print(emp_1.email)
# print(emp_1.pay)
# print(help(Developer))
# print(new_emp_1.email)
# print(new_emp_1.pay)

# print(Employee.__dict__)
# Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.06


# Employee.set_raise_amt(1.05)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.num_of_emps)

# print(emp_1.fullname())  # = print(Employee.fullname(emp_1))
# print(emp_2.fullname())
# print(Employee.employee_email(emp_1))
# print(emp_2.email)
#
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)
# print(emp_1)
# print(emp_2)
# emp_1.first = 'Khaled'
# emp_1.last = 'Tarek'
# emp_1.email = 'KhaledTarek@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'test'
# emp_2.last = 'user'
# emp_2.email = 'testuser@gmail.com'
# emp_2.pay = 60000
# print(f'{emp_1.first}{emp_1.last}')
