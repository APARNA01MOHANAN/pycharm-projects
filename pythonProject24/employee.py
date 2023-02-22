'''class Employee:
    pass

class Employee:
    company = 'LTTS'
emp = Employee()
print(emp.company)
print("-------------")
print(Employee.company)

class Employee:
    company = 'Tutorial Gateway'
    def func_message(self):
        print('Welcome to Programming')
emp = Employee()
print(emp.company)
emp.func_message()
print("-------------")
print(Employee.company)
print(Employee.func_message)

class Employee:
    company = 'Tutorial Gateway'
    def __init__(self):
        print('Hello World')
    def func_message(self):
        print('Welcome to Python Programming')
emp1 = Employee()  # Created an Instance
print(emp1.company)
emp1.func_message()
emp2 = Employee()  # Created an Instance
print(emp2.company)
emp2.func_message()

#init with parameters

class Employee():
    company='LTTS'
    def __init__(self,n,a,g):
        self.name=n
        self.age=a
        self.gender=g
    def msg(self):
        print("welcome to OOPS with PYTHON")
emp1=Employee('APARNA',21,'FEMALE')
print(emp1.company)
emp1.msg()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp2=Employee('SURYA',21,'FEMALE')
print(emp2.company)
emp2.msg()
print(emp2.name)
print(emp2.age)
print(emp2.gender)

class Employee:
    company="LTTS"
    def msg(self):
        print("welcome to programming")
emp1=Employee()
emp2=Employee()
emp3=Employee()
emp2.company='py'
emp3.company='Apple'
Employee.company='samsung'
emp1.msg()
print(emp1.company)
print(emp2.company)
print(emp3.company)
print(emp1.company)
print(Employee.company)


class Employee:
    company = 'Tutorial Gateway'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def func_message(self):
        print(self.name + ' is learning Programs')


emp1 = Employee('Mike', 25, 'Male')
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()

emp1.name = 'John'
print(emp1.name)
emp1.func_message()

class Employee:
    company = 'Tutorial Gateway'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def func_message(self):
        print(self.name + ' is learning Programming')


emp1 = Employee('John', 25, 'Male')
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.func_message()

del emp1.name
print(emp1.name)'''

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func_message(self):
        print(self.name + ' is learning Programming')

    def func_msg(aparna):
        print('Tutorial Gateway Welcome ' + aparna.name)


emp1 = Employee('John', 25)
emp1.func_message()
emp1.func_msg()

class Person:
    company='LTTS'
    def __init__(self):
        self.age=23
p1=Person()
p2=Person()
p2.age=45
print(p1.age)
p1.company="ibm"
print (p1.company)

class Vehicle():
    color='blue'
    def __init__(self,brand,mileage,speed,power):
        self.brand=brand
        self.mileage=mileage
        self.speed=speed
        self.power=power
    def function(self):
        print("start")
v1=Vehicle("honda",100000,57,'on')
v2=Vehicle("maruthi",100000,97,'off')
print(v1.mileage)
print(v2.brand)
v1.function()



class parent:
    string = "hello inheretence"

    def display(self):
        return self.string


class childclass(parent):
    pass


class child2(parent):
    pass


class child3(child2):
    pass


child = childclass()
child5 = child2()
child6 = child3()
print(child.display())
print(child5.display())
print(child6.display())


class Person:
    def __init__ (self, name,age):
        self.name = name
        self.age = age
class Professor(Person):
    def isProfessor(self):
        return self.name


sir = Professor('john', 30)
print(sir.isProfessor())


class Employee:

    def __init__(self, fullname, age, income):
        self.fullname = fullname
        self.age = age
        self.income = income

    def func_msg(self,clg):
        self.clg=clg
        print('Welcome to Employee')

    def func_information(self):
        print('At age', self.age, self.fullname, 'is earning', self.income)
        print(self.clg)

class Department(Employee):
    pass


emp = Employee('Suresh', '27', '650000')
emp.func_msg('dkl')
emp.func_information()

print('--------------')
dept = Department('Jenny', '25', '850005')
dept.func_msg('fgh')  # Calling Parent Method func_msg(self)
dept.func_information()  # Calling Parent Method func_information(self)