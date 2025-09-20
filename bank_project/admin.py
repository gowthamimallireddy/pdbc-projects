from db_connection import db_connection
dbC=db_connection()
cur=dbC.cursor()

def search_customer():
    user_Name=input("enter customer name :--  ")
    cur.execute("select *  from users where user_name = %s and user_role=%s " ,(user_Name,"customer"))
    customerData=cur.fetchone()
    print(customerData,"cData")

def search_admin():
    user_Name=input("enter customer name :--  ")
    cur.execute("select *  from users where user_name = %s and user_role=%s  " ,(user_Name,"admin"))
    customerData=cur.fetchone()
    print(customerData,"cData")

def fetchUsers():
    cur.execute("select *  from users  ")
    customerData=cur.fetchall()
    print(customerData,"cData")

def delete_customer():
    user_Name=input("enter customer name :--  ")
    cur.execute("select *  from users where user_name = %s",(user_Name,))
    user_id=cur.fetchone()[0]
    cur.execute("delete from accounts where user_id = %s " ,(user_id,))
    cur.execute("delete from requests where user_id = %s " ,(user_id,))
    cur.execute("delete from users where user_id = %s " ,(user_id,))
    dbC.commit()
    print("customer deletd successfully...........")

def viewReqs():
    option=input("choose 1) loan 2 ) atm_card 3 ) checkbook")
    if option == "1":
        cur.execute("""
        select users.user_name,accounts.account_balance,requests.req_type,requests.req_amount
from users
left join accounts 
using (user_id)
left join requests
using (user_id)
where requests.req_type = %s
        """,("loan",))
        reqData=cur.fetchall() 
        for i in reqData:
            user_name,user_main_bal,user_req_type,user_quoteamt=i
            print(f"{user_name},,{int(user_main_bal)},{user_req_type},{int(user_quoteamt)}")
    elif option == "2":
        cur.execute("select *  from requests  where req_type=%s",("atm_card",))
        reqData=cur.fetchall()
        print(reqData)

    elif option == "3" :
        cur.execute("select *  from requests  where req_type=%s",("checkbook",))
        reqData=cur.fetchall() 
        print(reqData)

    else:
        return "invalid "    
