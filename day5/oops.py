class student:
    print("hey this is first class")
s1=student()
print(s1)

class student:
    # constructor
    def __init__(self):
        print("Hey this is first class")
s1=student()
print(s1)

class student:
    # constructor
    def __init__(self):
        self.name="Rahul"
s1=student()
print(s1.name)

class student:
    def __init__(self,fullname):
        self.name=fullname
s1=student('Arjun')
print(s1.name)

class marks:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

s1= marks('Arjun',10)
s2 = marks('aman',20)
s3 = marks('arian',30)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)

#print color and model of a car
class car:
    def __init__(self,colour,model):
        self.colour = colour
        self.model = model
cm1=car('Black','Mercedes')
cm2=car('Red','Ferrari')
cm3=car('Yellow','Lamborghini')
print(cm1.colour,cm1.model)
print(cm2.colour,cm2.model)
print(cm3.colour,cm3.model)


class student:
    collage_name='LPU'
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
s1=student('Aaron',90)
s2=student('Ron',90)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s1.collage_name)
print(s2.collage_name)
print(student.collage_name)

class employee:
    companyName = "CISCO"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e1 = employee("ARUND",20000)
e2 = employee("RON",30000)
print(e1.companyName,e1.name,e1.salary)
print(e2.companyName,e2.name,e2.salary)


class car:
    showroom="Mercedes"
    def __init__(self,car_name,price):
        self.name = car_name
        self.price = price
c11 = car("s_class",2000000)
c12 = car("A_class",3000000)
print(c11.showroom,c11.name,c11.price)
print(c12.showroom,c12.name,c12.price)

class collage:
    collageName = "LPU"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
s1=collage("Anna",100)
s2=collage("Bill",90)
print(s1.collageName,s1.name,s1.marks)
print(s2.collageName,s2.name,s2.marks)
collage.collageName = "CTU"
print(s1.collageName,s1.name,s1.marks)
print(s2.collageName,s2.name,s2.marks)

class company:
    companyName='Infosys'
    def __init__(self,eName,salary):
        self.eName=eName
        self.salary=salary
e1=company('mary',20000)
e2=company('tom',50000)
print(e1.companyName,e1.eName,e1.salary)
print(e2.companyName,e2.eName,e2.salary)
e1.salary=17000
print(e1.companyName,e1.eName,e1.salary)
print(e2.companyName,e2.eName,e2.salary)

class Student:
    total_student = 0
    def __init__(self,name):
        self.name = name
        Student.total_student += 1
s1=Student("shan")
s2=Student("aaaaa")
print(s1.name,s2.name)
print(s1.total_student)

#---------method---------
class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("welcome",self.name)
s1=Student("shan")
s1.hello()

#-----static method
class Student:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("welcome",self.name)
    @staticmethod
    def college_name():
        print("This is Lpu")
s1=Student("shan")
s1.hello()
s1.college_name()


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.mark=marks
    def display(self):
        print("Hi ",self.name,"your mark is ",self.mark)
s1=Student("Shan",99)
s2=Student("harsh",88)
s1.display()

#-------------
class Student:
    def __init__(self,marks):
        self._marks = marks
    def getmarks(self):
        return self._marks
s1=Student(100)
print(s1.getmarks())

#-----------------------private
class Bank_balance:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
s1=Bank_balance(15000)
print(s1.get_balance())


#-----------------------------------------changing values
class Bank_balance:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,new_balance):
        self.__balance=new_balance
s1=Bank_balance(15000)
s1.set_balance(10000)
print(s1.get_balance())


#--------bank 
class ATM:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self,deposit):
        self.__balance += deposit
        print("balance after deposit",self.__balance)
    def withdraw(self,withdraw):
        if self.__balance<withdraw:
            print("Insufficiant balance")
        else:
            self.__balance -= withdraw
            print("balance after withdrawing",self.__balance)
S1=ATM(10000)
S1.deposit(1000)
S1.withdraw(5000)
print("balance after all ",S1.get_balance())

