#--------------------------------------------------------------------------------------------recap------------------------------------------------------------------------------------------


fruit = []
print(fruit)
#append is used to add alement
fruit.append("apple")
print(fruit)


#Q find the sum of all elements in a list
numbers = [5,1015]
total = 0
for i in numbers:
    total = total+i
print(total)

##remove duplicates elements from the list
num = [1,2,3,4,4]
unique = []
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)

#convert list into tuple
numbers = [1,2,3,4,5]
print(type(numbers))
print(numbers)
numbers_tuple = tuple(numbers)
print(type(numbers_tuple))
print(numbers_tuple)


#converting tuple to list
colors = ("red","blue","green")
print(type(colors))
print(colors)
colors_list = list(colors)
print(type(colors_list))
print(colors_list)

#conversion of list to set
lists = [1,1,2,3,3,4]
print(type(lists))
print(lists)
lists_to_set = set(lists)
print(type(lists_to_set))
print(lists_to_set)

#converting dictionary to set
student = {'name':'karan','age':24}
student_set = set(student)
print(student)
print(student_set)

#converting set into dictionary
subjects = {"Maths","Science","English"}
subject_dict = dict.fromkeys(subjects,100)
print(subjects)
print(subject_dict)
print(type(subject_dict))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#catching any specific error
try:
    x=int(input("enter number:"))
    print(10/x)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter only number")


#else block
try:
    num = int(input("enter number:"))
    print(10/num)
except:
    print("error occured")
else:
    print("No error,program run succesfully")


#finally block
try:
    f = open("movies1.txt")
except:
    print("file not found")
finally:
    print("program finished")#in both case finaly will print

    
age  = int(input("enter your age: "))
if age<18:
    raise ValueError("Age must be 18 or above for vote")
print("you can vote")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#custome error
class LowBalanceError(Exception):
    #this line create a custome exception named LowbalanceError
    #pass is used becuase class cannot be empty in pythonn
    pass
balance = 500
withdraw = int(input("Enter amount:"))
if withdraw>balance:
    raise LowBalanceError("Insufficient balance")
print("withdraw succesfull")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    num=int(input("enter a umber:"))
    print(100/num)
except ZeroDivisionError:
    print("cant be divided by zero")
except ValueError:
    print("Value error occured")
finally:
    print("Done")
#-----------------------------------------------------------------------------------------------------------------------------
try:
    try:
        print(1/10)
    finally:
        print("inner finally")
except ZeroDivisionError:
    print("Outer exception")
finally:
    print("Outer Finally")


#-----------------------------------------------------------------
def test():
    try:
        return 10
    finally:
        return 20
print(test())

#-----------------------------------------------------
try:
    try:
        x=int("abc")
    except ValueError:
        print("Inner Handles")
        raise
except Exception:
    print("Outer handled")

def test():
    try:
        return 10
    except:
        return 20
    else:
        return 30
print(test())

age = int(input("enter ur age"))
if age<18:
    raise ValueError("Age must be 18 or more")
print(
    "your are eligible"
)

#---------------------------------------------------------------------
num = int(input("enter ur number"))
if(num<0):
    raise ValueError("number must be positive")
print("you entered:",num)
#--------------------------------------------------------------------
#practice questions
print(True+True+False)
print("5"+"4")
print("5"*10)


def change(x):
    x+=10
a=5
change(a)
print(a)

def update(lst):
    lst.append(10)
num=[1,2,3]
update(num)
print(num)

t=(1,2,3)
t=t+(4,)
print(t)

s={1,2,3,3,4,4}
print(len(s))

for i in range(3):
    print(i)
else:
    print("done")

try:
    print("A")
    10/0
    print("B")
except:
    print("c")
print("D")

#q move all zeros to end
num=[0,1,0,3,12]
result=[]
zero_count = 0
for n in num:
    if n == 0:
        zero_count += 1
    else:
        result.append(n)
for i in range(zero_count):
    result.append(0)
print(result)

#-------------------------------------------------------
#checking palindrome or not
text = str(input("enter name : "))
left = 0
right = len(text)-1
isPalindrome = True
while left<right:
    if text[left] != text[right]:
        isPalindrome=False
        break
    left+=1
    right-=1
print(isPalindrome)
#--------------------------------------------------------
#finding longest word from the sentense
sentance = str(input("enter the sentence: "))
words = sentance.split()
longest = ""
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)
#---------------------------------------------------------
A=[1,2,3,2]
target = 5
count = 0
for i in range(len(A)):
    total = 0
    for j in range(i,len(A)):
        total += A[j]
        if total == target:
            count+=1
print(count)


nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(nums[i],nums[j])


nums = [2,7,11,15]
target = 9
left = 0
right = len(nums)-1
while left < right:
    current_sum = nums[left]+nums[right]
    if current_sum == target:
        print(nums[left],nums[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1
    

nums = [10,20,30,40,50]
slow = 0
fast = 0
while fast<len(nums) and fast+1<len(nums):
    slow+=1
    fast+=2
print(nums[slow])
