from operations import add_Student,view_Student,update_Student,delete_Student
import sys

while True:
    print("1.add student")
    print("2.view student")
    print("3.update student")
    print("4.delete  student")
    print("5.exit")

    choose = int(input("enter value here--"))
    if choose == 1:
        add_Student()
    elif choose == 2:
        view_Student()
    elif choose == 3:
        update_Student()
    elif choose == 4:
        delete_Student()
    elif choose == 5:
        print("Exist...")
        sys.exit()
    else:
        print("invalid choice:")


    

