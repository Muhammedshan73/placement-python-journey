try:
    #risky code
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
except:
    #error handling code
    print("error occured!!!!!!!!!!!!!!")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    file = open("movies.txt","r")
    print(file.read())
except FileNotFoundError: # if file is excisting it will give file output if not it will give file not founf
    print("file not found")
finally:
    print("program ends")
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

