import mysql.connector as ms
con=ms.connect(host="localhost",user="root",passwd=None,database="bank")
cm=con.cursor()

def cca():
    ano=int(input("enter account number"))
    n=input("enter name")
    ad=input("enter address")
    b=int(input("enter balance"))
    tp=input("enter s for saving or c for current")
    adhno=int(input("enter Adhaar number"))
    pno=int(input("enter Pan number"))
    i="insert into customer (Accno,AccHolderName,AccHolderAddress,Balance,TypeofAcc,AdhaarNo,PanNo) values({},'{}','{}',{},'{}',{},{})"
    j=(ano,n,ad,b,tp,adhno,pno)
    cm.execute("insert into customer (Accno,AccHolderName,AccHolderAddress,Balance,TypeofAcc,AdhaarNo,PanNo) values({},'{}','{}',{},'{}',{},{})".format(ano,n,ad,b,tp,adhno,pno))
    con.commit()

def dca():
    cm.execute("select * from customer")
    r=cm.fetchall()
    for i in r:
        print(i)
    

def dlca():
    n=int(input("enter Account Number"))
    cm.execute("delete from customer where Accno={}".format(n))
    con.commit()

def leave():
    con.close()

def start():
    print("1-create new account")
    print("2-display account")
    print("3-delete account")
    print("4-close portal")
    ch=int(input("enter 1 to 4"))
    if ch==1:
        cca()
        start()
    elif ch==2:
        dca()
        start()
    elif ch==3:
        dlca()
        start()
    elif ch==4:
        leave()

start()
       
       
    



    
