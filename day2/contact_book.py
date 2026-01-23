contact={}
while True:
    print("\n----contact book----")
    print("1. add contact")
    print("2. view contact")
    print("3. search contact")
    print("4. remove contact")
    print("5. exit")
    choice=input("\nEnter your choice: ")
    if choice=="1":
        name=input("Enter your name: ")
        phone=input("Enter your phone: ")
        contact[name]=phone
        print("\nYour contact added successfully")

    elif choice=="2":
        if contact:
            print("\nsaved contatct:")
            for name,phone in contact.items():
                print(name,":",phone)
        else:
            print("\nNo contact added")

    elif choice=="3":
        name=input("Enter name to search: ")
        if name in contact:
            print('phone number:', contact[name])
        else:
            print("\nNo contact found")

    elif choice=="4":
        name=input("Enter name to remove: ")
        if name in contact:
            del contact[name]
            print("\nYour contact removed successfully")
        else:
            print("\nNo contact removed")

    elif choice=="5":
        print("thank you for using contact book")
        break
    else:
        print("Invalid choice! pls try again")
