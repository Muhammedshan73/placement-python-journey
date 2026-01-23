student={}
while True:
    print("\n----student book----")
    print("1. add student")
    print("2. view student")
    print("3. search student")
    print("4. remove student")
    print("5. exit")
    choice=input("\nEnter your choice: ")
    if choice=="1":
        name=input("Enter student name: ")
        rollno=input("Enter student roll no: ")
        course=input("Enter student course: ")
        student[rollno]={'name':name,'course':course}
        print("\nstudent  added successfully")

    elif choice=="2":
        if student:
            print("\nall student:")
            for roll,info in student.items():
                print('rollno: ', rollno)
                print("name: ", info["name"])
                print("course:", info['course'])
        else:
            print("\nNo student added")

    elif choice=="3":
        rollno=input("Enter rollno to search: ")
        if rollno in student:
            print('name:', student[rollno]["name"])
            print('course:', student[rollno]["course"])
        else:
            print("\nNo student found")

    elif choice=="4":
        rollno=input("Enter rollno to remove: ")
        removed=student.pop(rollno,'not found')
        if rollno == 'not found':
            # del contact[name]
            print("\nYour student not found")
        else:
            print("\n student removed")

    elif choice=="5":
        print("thank you for using contact book")
        break
    else:
        print("Invalid choice! pls try again")
