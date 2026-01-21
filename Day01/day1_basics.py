# Day 1 – Python Basics

Today I started learning Python as part of my placement preparation.

## What I learned today
- Printing output and using variables
- Understanding data types and type conversion
- Using if, elif, and else conditions
- For loops and while loops
- Writing functions and lambda functions
- Working with lists, tuples, sets, and dictionaries
- Solving basic logical problems

## Practice programs
- Check even or odd numbers
- Find the biggest number
- Grade calculation using marks
- Reverse a number
- Multiplication tables
- Temperature condition program
- Simple lambda function examples

#1 Basic 
print("Hello world")
a="shan"
print(a)

b = 26
c =6.6
d = "100"
print(b)
print(type(c))
print(int(d))

#------------------------------------------------------------------------------------- if else-------------------------------------------------------------------------------------------
x = int(input("Enter your age:" ))
if(x>15):
    print("You are eligible")
elif(x==15):
    print("moderate")
else:
    print("You are not eligible")

y = int(input("Enter a number: "))
if(y%2==0):
    print("it is even")
else:
    print("it is odd")

#4 ------------------------------------------------------------------------------------elif----------------------------------------------------------------------------------------------
mark = int(input("Enter Your Mark:"))
if(mark>=90):
    print("A")
elif(mark>=75):
    print("B")
elif(mark>=50):
    print("C")
else:
    print("Fail")

#5 
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if(a>b):
    print("The Biggest Number Is:",a)
elif(b>a):
    print("The Biggest number Is:",b)
else:
    print("Both are Equal")

#------------------------------------------------------------------------------------Steet Light----------------------------------------------------------------------------------------
light = str(input("Wich Light : "))
if light == "green":
    print("You can Go")
elif light == "yellow":
    print("ready")
elif light == "red":
    print("Stop")
else:
    print("Please give the color green yellow or red")

#-------------------------------------------------------------------------------------for loop----------------------------------------------------------------------------------------------
for i in range(1,11):
    print(2*i)

# Q) print all the odd numbers between 1 to 15
for i in range(1,16):
    if(i%2 != 0):
        print(i)

#q----------------------------------------------------------------------------------Star -------------------------------------------------------------------------------------------------
x = "*"
for i in range(1,7):
    print(i*x)


#-------------------------------------------------------------------------------------while loop--------------------------------------------------------------------------------------------
i = 1
while(i<=5):
    print(i)
    i += 1

i = 3
while(i<=30):
    print(i*1)
    i += 1

#------------------------------------------------------------------------------------multiplication table----------------------------------------------------------------------------------
num = int(input("Enter the number:"))
i = 1
while(i<=10):
    print(num,"x",i,"=",num*i)
    i+=1
#-------------------------------------------------------------------------------------argument function-----------------------------------------------------------------------------------
def add(a,b):
    print(a+b)
add(10,20)


#with return type
def sum(c,d):
    return(c+d)

addition = sum(40,20)
print(addition)

#--------------------------------------------------------------------------------------------lamda function--------------------------------------------------------------------------------
add = lambda x,y:x+y
print(add(10,20))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Q1)take input print its type and then double of it
#q2)take input salary as string then convert into integer and add bonus 500 and print
#q3)print Hot if(temp>=30) normal>=15 else cold
#q4)print table of 7 and count how many numbers are printed
#q5)take a number and reverse it
#q6)check even odd using function
#q7)create a lambda function to return a cube of a number


#q1
a = input("Enter the value:")
print(type(a))

z = int(a)
print(z*2)

#q2
salary = str(input("Enter Salary:"))
sal = int(salary)
print(sal+500)

#q3
temp = int(input("Enter the temperature:"))
if(temp>=30):
    print("Hot")
elif(temp>=15):
    print("Normal")
else:
    print("Cold")

#q4
num = int(input("Enter wich numltiplaction number needed:"))
i = 1
while(i<=10):
    print(num,"X",i,"=",num*i)
    i += 1

#q5
Number = int(input("Enter Number:"))
reverse = int(str(Number)[::-1])
print("Reverse oder = ",reverse)

#------------------------------------------------------------------------------------------- List ----------------------------------------------------------------------------------------
marks = [10,20,30,40]
print(marks[0])
marks.append(100)
print(marks)
marks.insert(2,75)
print(marks)
marks.remove(75)
print(marks)
marks.pop()
print(marks)


age = [23,45,16,18,20]
print(age)
age.sort()
print(age)
age.reverse()
print(age)
print(len(age))
print("Max:",max(age))
print("Sum:",sum(age))
print("Average:",sum(age)/len(age))

#------------------------------------------------------------------------------------------- Tuple ------------------------------------------------------------------------------------------

days = ('monday','Tuesday','Wed','Thu','monday')
print(days[0])
print(days[-1])
print(days.count('monday'))
print(days.index('Tuesday'))
print('monday' in days)

t = (10,20,30,40,50)
print(t[:3])
#---------------------------------------------------------------------------------------------Set--------------------------------------------------------------------------------------------
numbers = {10,20,30,40,10,20}
print(numbers)
for i in numbers:
    print(i)
numbers.add(100)
print(numbers)
numbers.update([120,130])
print(numbers)
numbers.remove(175)
print(numbers)# will gie error if element doesnt exist
numbers.discard(175)
print(numbers)#will not give error whether if element is there or not
numbers.pop() # random number will be removed
print(numbers)


a = {1,2,3}
b = {3,4,5}
c = {3,2}
print(a.union(b))
print(a.intersection(b))
print(c.issubset(a))

#--------------------------------------------------------------------------------------------Dictionary--------------------------------------------------------------------------------------


                 


## Why I am doing this
I am practicing Python daily to strengthen my basics and improve my problem-solving skills for placement interviews.

👨‍💻 **Name:** Muhammed Shan S T  
📅 **Day:** 1
