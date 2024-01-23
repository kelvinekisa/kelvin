class Employee:

    number_of_empls = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_empls += 1

    def fullname(self):
        return '{} {}'. format(self.first, self.last)

    # #Accessing a class variable by the class itself
    # def apply_raise(self):
    #     self.pay = int(self.pay * Employee.raise_amount)

    #Accessing a class variable by instance of a class
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

empl_1 = Employee('Kelvin', 'Ekisa', 60000)
empl_2 = Employee('Ruth', 'Mukiri', 60000)
empl_3 = Employee('John', 'Ken', 98880)


# print(empl_1.pay)
# empl_1.apply_raise()
# print(empl_1.pay)

# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)

print(Employee.number_of_empls)
