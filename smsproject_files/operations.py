from db import get_connection
def add_Student():
    con = get_connection()
    student_name = input("enter student_name here--")
    Dob = input("enter student_dob here--")
    gender = input("enter student_gender here--")
    email  = input("enter student_email here--")
    phone_num = input("enter student_phone_num here--")
    branch = input("enter student_branch here--")
    cur = con.cursor()
    query = """insert into Students (student_name,dob,gender,email,phone,Branch) values (%s,%s,%s,%s,%s,%s)"""
    values = (student_name, Dob ,gender,email,phone_num, branch)
    cur.execute(query,values)
    con.commit()
    con.close()
    print(f"{student_name} added succesfully") 

def view_Student():
    con = get_connection()
    cur = con.cursor()
    cur.execute("select * from Students")
    data = cur.fetchall()
    for i in data:
        print(i)
    con.close()
    print("students data fetched successfully!!")


def update_Student():
    student_id = int(input("Enter student ID to update: "))
    choice = input("Enter choice: ")

    fields = {
        "1": "student_name",
        "2": "dob",
        "3": "gender",
        "4": "email",
        "5": "phone",
        "6": "branch"
    }

    if choice in fields:
        new_value = input(f"Enter new {fields[choice]}: ")
        con = get_connection()
        cursor = con.cursor()
        query = f"UPDATE students SET {fields[choice]}=%s WHERE student_id=%s"
        cursor.execute(query, (new_value, student_id))
        con.commit()
        
        if cursor.rowcount > 0:
            print(" Student updated successfully")
        else:
            print(" Student not found")
        con.close()
    else:
        print(" Invalid choice!")

def delete_Student():
    con = get_connection()
    cur = con.cursor()
    student_id=int(input("enetr student_id "))
    cur.execute("delete from Students where student_id = %s",(student_id,))
    con.commit()
    con.close()




    