from authentication import signup,login
from customers import withdraw,deposit,check_Bal,request
from admin import search_customer,delete_customer,search_admin,fetchUsers,viewReqs
print("1. signup")
print("2. login")
print("3. exit")

choose=input("choose above options any one :-- ")
if choose == "1":
    signup()
elif choose == "2":
    abc=login()
    user_id,user_name,user_pswd,user_role=abc
    if user_role == "customer":
        print("------customer menu ---------")
        print("1.withdraw")
        print("2.deposit")
        print("3.check_Bal")
        print("4.request (atm/loan/checkbook)")
        chooseOpt=int(input("enetr option here :-- "))
        if chooseOpt  == 1:
            withdraw(user_id)

        if chooseOpt == 2:
            deposit(user_id)   

        if chooseOpt == 3:
            check_Bal(user_id)   
        if chooseOpt  == 4:
            request(user_id)   
    if user_role =="admin":
        while True:
            print("--------admin features----------") 
            print("1.search for customer")
            print("2.search for admin")
            print("3.fetch all users")
            print("4.delete  customer")
            print("5.view requests for customer")

            choose =int(input("enter yr option here :----    "))
            if choose == 1:
                search_customer()
            elif choose ==2:
                search_admin()  
            elif choose == 3:
                fetchUsers()   
            elif choose == 4:
                delete_customer()  
            else:
                viewReqs()      

    
