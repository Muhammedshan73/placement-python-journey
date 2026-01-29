#*********************************************abstraction********************************************
class Payment:
    def start(self):
        print("Payment started")
    def pay(self,amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("paid using UPI:",amount)
class CARD(Payment):
    def pay(self,amount):
        print("paid using CARD:",amount)
class CASH(Payment):
    def pay(self,amount):
        print("paid using CASH:",amount)
#obj1
obj1 = CARD()
obj1.start()
obj1.pay(1500)

#obj2
obj2 = UPI()
obj2.start()
obj2.pay(200)


#eg 2 shapes
#------abstraction------
class Shapes:
    def start(self):    
        print("Checking area")
    def area(self):
        pass
    def finished(self):
        print("finished\n")
class Circle(Shapes):
    def area(self,l):
        print("Area of circle",3.14*l*l)
class Square(Shapes):
    def area(self,l):
        print("Area of Square is",l*l)
class Rectangle(Shapes):
    def area(self,l,b):
        print("area of rectangle is",l*b)
#obj
obj = Circle()
obj.start()
obj.area(12)
obj.finished()

#obj1
obj1 = Square()
obj1.start()
obj1.area(9)
obj.finished()

#obj2
obj2 = Rectangle()
obj2.start()
obj2.area(5,7)
obj2.finished()

#********************************************interface************************************************

class Shapes:
    def area(self):
        pass
class Circle(Shapes):
    def area(self,l):
        print("Area of circle",3.14*l*l)
class Square(Shapes):
    def area(self,l):
        print("Area of Square is",l*l)
class Rectangle(Shapes):
    def area(self,l,b):
        print("area of rectangle is",l*b)
#obj
obj = Circle()
obj.area(12)

#obj1
obj1 = Square()
obj1.area(9)

#obj2
obj2 = Rectangle()
obj2.area(5,7)

#create a program where abstract class name is course it has two method course info and duration 
#then you want to create an interface exam interface it has a method exam type then we child class python of both course and exam interface in that two method duration and exam type

#abstract class
class Course:
    def course_info(self,course):
        print("course is",course)
    def Duration(self):
        pass

#interface class
class Exam_interface:
    def Exam_type(self,type):
        pass
class Python(Course,Exam_interface):
    def Duration(self,dur):
        print("Duration of the exam is ",dur)
    def Exam_type(self,type):
        print("Exam type is",type,"\n")
class DSA(Course,Exam_interface):
    def Duration(self,dur):
        print("Duration of the exam is ",dur)
    def Exam_type(self,type):
        print("Exam type is",type,"\n")
class Java(Course,Exam_interface):
    def Duration(self,dur):
        print("Duration of the exam is ",dur)
    def Exam_type(self,type):
        print("Exam type is",type,"\n")

obj1 = Java()
obj1.course_info("java")
obj1.Duration("3hr")
obj1.Exam_type("written")

obj2 = DSA()
obj2.course_info("DSA")
obj2.Duration("2hr")
obj2.Exam_type("written+mcq")

obj3 = Python()
obj3.course_info("Python")
obj3.Duration("4hr")
obj3.Exam_type("programing")

#***********************************************composition******************************************** 
class Address:
    def __init__(self,city):
        self.city = city
    def show_address(self):
        print("City:",self.city)

#student class
class Student:
    def __init__(self,name,city):
        self.name = name
        #composition:
        #creating object of address class inside student class
        self.address = Address(city)
    def show_student(self):
        print("Name:",self.name)
        #using object of another class
        self.address.show_address()


#oject
onj = Student("shan","kozhikkode")
onj.show_student()


#create a engine then create a class car 
#->car HAS-A engine

class Engine:
    def Start(self):
        print("Engine Started")
class Car:
    def __init__(self):
        self.engine = Engine()
    def drive(self):
        self.engine.Start()
        print("car is moving")

obj1 = Car()
obj1.drive()




