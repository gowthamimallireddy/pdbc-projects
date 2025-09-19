from authentication import signup,login
from customers import withdraw,deposit,check_Bal,request
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

    
