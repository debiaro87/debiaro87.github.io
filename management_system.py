
students=[] #to create list in python
def add_student():
    number=int(input("How many student do you want to add:"))
    for i in range (number):
        student={} #to create dictionary in python
        student["name"]=input(f"Enter {i+1} student :")
        student["id"]=input("Enter ID:")
        student["department"]=input("Enter department:")
        
        while True: # it make loop untill the user enter the valid mark number
            mark=float(input("Enter mark:"))
            if 0<=mark<=100:
                student["mark"]=mark
                break
            else:
                print("please enter valid mark")
        students.append(student) # to add the dictionary to list
        print()
    print("Student added successfully")

    print()
    print("="*5,"STUDENT LISt","="*5)
    for student in students:
        print("Name:",student["name"])
        print("ID:",student["id"])
        print("Department:",student["department"])
        print("Mark",student["mark"])
        
def view_student(): # this is making function in python
    print()
    
    if len(students)==0:
        print("no data exist")
        return # this check if data exist and out from the iner loop to the outside one
    for student in students:
        print("Name:",student["name"])
        print("ID:",student["id"])
        print("Department:",student["department"])
        print("Mark:",student["mark"])
        
def search_stud():
    print()
    if not students:
        print("no data exist")
        return
    search=input("Enter student name you find:")
    found=False
    for student in students:
        if student["name"]==search:
        
            print("Name",student["name"])
            print("ID:",student["id"])
            print("Department:",student["department"])
            print("Mark:",student["mark"])
            found=True
            break # if true the above it break and start the next one
    if not found:
        print("the student you find does not exist")
        print()
    
def update_mark():
    print()
    if not students:
       print("no data exist") 
       return
    update=input('Enter the person you find to update it"s mark:')
    print()
    found=False
    for student in students:
        if student["name"]==update:
            new_mark=float(input("Enter new mark:"))
            if 0<=new_mark<=100:
                student["mark"]=new_mark
                print("mark updated successfully !")
            else:
                print("pls enter valid mark 0-100")
            found=True
            break
    if not found:
        print("student not found !")
      
    print()
def Delete_student():
    print()
    if not students:
        print("no data exist")
        return
    del_name=input("Enter the student you find to delete from the data:")
    found=False
    print()
    for student in students:
        if student["name"]==del_name:
            students.remove(student)
            print(" student deleted successfully")
            found=True
            break
    if not found:
        print("student not found")
print()
Man_system=["Add Student","View Student","Search Student","Update mark","Delete Student","Exit"] # creating list

while True:
    print()
    print("="*5 ,"STUDENT MANEGEMENT SYSTEM","="*5)
    for i in range(len(Man_system)):
        print(f"{i+1}.{Man_system[i]}")   # accessing the list   
    print()
    choice=int(input("Enter your choice:"))
    if choice==1:
        add_student() # just calling the functioned program
    elif choice==2:
        view_student()
    elif choice==3:
        search_stud()
    elif choice==4:
        update_mark()
    elif choice==5:
        Delete_student()
    elif choice==6:
        print("Thank you !")
        break
    else:
        print("invalid choice")

    

