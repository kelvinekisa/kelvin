# Python object Oriented programming

#instance attribute
class Employee:
    pass


empl_1 = Employee()
empl_2 = Employee()

print(empl_1)
print(empl_2)

empl_1.first = 'John'
empl_1.last = 'Kelvin'
empl_1.email = 'John@company.ac.ke'


empl_2.first = 'John'
empl_2.last = 'Mukiri'
empl_2.email = 'mukiri@usercompany.ac.ke'

print(empl_2.email)
print(empl_1.email)


#class sttribute

class Employee:
    def __init__(self, first, last, pay,):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}' .format(self.first, self.last)

employee_1 = Employee("john", "Kerry", 60000)
employee_2 = Employee('Kevin', 'Ekisa', 50000)
employee_3 = Employee('Joy', 'Kasusya', 200000)

print(employee_3.email)
print(employee_1.fullname())

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


#instance method
    def description(self):
        return f'{self.name} is {self.age} years old'

#nother instance method
    def speak(self, sound):
        return f'{self.name} say {sound}'



