#creating file
file=open("students.txt","w")
file.write("Name: Rahul \n")
file.write("Course: Python \n")
file.close()
#----------------------------------------------------------------------------------------------Reading file----------------------------------------------------------------------------------
file = open("students.txt","r")
data = file.read()
print(data)
file.close()
#-----------------------------------------------------------------------------------------------append---------------------------------------------------------------------------------------
file = open("students.txt","a")
file.write("marks: 90\n")
file.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
file = open("personal.txt","r")
data = file.read()
data2 = file.readlines()#it will print the line and also it will covert the text file into list so that we can check what is the len of the fie
print(len(data))
file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
file = open("personal.txt","w")
file.write("my name is shan")
file.close()

file = open("personal.txt","r")
data = file.read()
print(data.upper())
print(len(data))
file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
file = open("personal.txt","r")
data = file.read()
words = data.split()
print("Total words in the file are : ",len(words))
file.close()

file = open("personal.txt","w")
file.write("my name shan  and shan is teaching")
file.close()

file = open("personal.txt","r")
data = file.read()
count = data.lower().count("shan")
print("shan has camed ",count," times")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
file = open("personal.txt","r")
data = file.read()
print(data)
file.close()

file = open("personal.txt","r")
data1 = file.read()
rep = data1.replace("shan","althaf")
print(rep)
file.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\

file = open("movies.txt","w")
file.write("Persuit of happiness\n")
file.write("inception\n")
file.write("kgf\n")
file.close()


file = open("movies.txt","r")
data = file.read()
print(data)

words = data.split()
for w in words:
    print(w[::-1]) # reverse in oder 
data2 = data.replace(" ","")
print("\n")
print(data2[:25])
file.close()
