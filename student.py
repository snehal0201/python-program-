import sys
students = []
id_no = 1
while 1:
    choice= int(input("Enter your choice:"))
    print("1.add students")
    if choice == 1:
        name = input("enter your name:")
        age = int(input("enter your age:"))
        course = input("enter your course:")
        id_no = id_no + 1

        students.append([name,age,course])
        
    elif choice == 2:
        id_no = int(input("Enter Id no:"))
        del students[id_no]

    else:
        sys.exit()
    
        
