#inheritance
#One class uses another class's features


class parent:
    def eat(self):
        print('eat')
class child(parent):
    def study(self):
        print('study')
s1=child()
s1.eat()
s1.study()

class Animal:
    def speak(self):
        print('Animal can speak')
class Dog(Animal):
    def bark(self):
        print('Dog can only bark')
s1=Dog()
s1.speak()
s1.bark()


class nokia:
    def call(self):
        print('Nokia can call')
class iphone(nokia):
    # def call(self):
    #     print('iphone can call')
    def internet(self):
        print('iphone can call and have internet')

s1=iphone()
s1.call()
s1.internet()

class parent:
    def __init__(self):
        print('parent constructor')
class child(parent):
    def __init__(self):
        # the below line is used to add parent constructor
        super().__init__()
        print('child constructor')
obj=child()
print(obj)





#Methode overriding
#Child class methode will always override the parent class methode

class parent:
    def work(self):
        print('parent work')
class child(parent):
    def work(self):
        print('child will go to school')
obj=child()
obj.work()

class Father:
    def programmer(self):
        print('I am a Programmer')
class Mother:
    def Nurse(self):
        print('I am a Nurse')
class Child(Father, Mother):
    def Student(self):
        print('I am a Student')
obj=Child()
obj.programmer()
obj.Nurse()
obj.Student()


class teacher:
    def teaching(self):
        print("teaching")
class coder():
    def coding(self):
        print("coding")
class student(teacher,coder):
    def studing(self):
        super().__init__()
        print("studing")
obj=student()
obj.teaching()
obj.coding()
obj.studing()


class parent:
    def __init__(self):
        self.__x=10
class child:
    def show(self):
        print(self.__x)
obj=child(parent)
obj.show()




class Person:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
class Child(Person):

    def showName(self):
        print('My name is ',self.get_name())
obj=Child('Austin')
obj.showName()
#--protected    
class Parent:
    def __init__(self):
        self._x = 100
class Child(Parent):
    def show(self):
        print(self._x)
obj = Child()
obj.show()

# doing example questions
class Person:
    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
class Student(Person):
    def show_name(self):
        print("dear",self.get_name(),"welcome to python coding")
obj = Student(input("enter your name: "))
obj.show_name()


#my method
class Account:
    def __init__(self):
        self._balance = 15000
    def show_balance(self):
        return(self._balance)
class Saving_account(Account):
    def add_money(self):
        print("your current balance is:",self._balance)
        add = int(input("how much you want to deposit: "))
        self._balance += add
        print("after depositing your balance",self.show_balance())
obj = Saving_account()
obj.add_money()

#diamond problem
class A:
    def message(self):
        print("A")
class B(A):
    def message(self):
        print("B")
class C(A):
    def message(self):
        print("C")
class D(C,B):
    pass
obj = D()
obj.message()

#polymorphism
#poly = many
#morph = form
class Dog:
    def speak(self):
        print("Dog is barking")
class Cat:
    def speak(self):
        print("meow")
class Humans:
    def speak(self):
        print("Human speaks")

obj = Dog()
obj.speak()


#polymorphism questions
class Human:
    def speak(self):
        print("Human is speaking")
class Baby:
    def speak(self):
        print("Baby is crying")
class Dog:
    def speak(self):
        print("Dog is barking")

#polymorphism in action
h = Human()
b = Baby()
d = Dog()

h.speak()
b.speak()
d.speak()

#####

#
class Bike:
    def ride(self):
        print("Bike is moving")
class Truck:
    def ride(self):
        print("Truck is moving")
class Car:
    def ride(self):
        print("Car is moving")

C = Car()
T = Truck()
B = Bike()

C.ride()
T.ride()
B.ride()

###
class Person:
    def role(self):
        print("Hi i am a person")
class Student:
    def role(self):
        print("I am a student")
class Teacher:
    def role(self):
        print("I am a teacher")
class Assistant(Student,Teacher):
    pass

obj = Assistant()
obj.role()


