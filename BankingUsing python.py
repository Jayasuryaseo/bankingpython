Accountno=883875
pin=2000
Savings_Amount=5000

credit="c"
debit="d"

a=int(input("Enter Your Account Number:"))

if(a==Accountno):
    print("Account Number Verified")
    b=int(input("Enter Your Pin:"))
    if(b==pin):
        print("Pin validated")
        c=str(input("Please Choose Transaction Credit/Debit:"))
        
        if(c==credit):
            print("You Choosed Credit")
            x=int(input("Enter Amount You Want to Credit:"))
            print("Amount Successfully Cedited:",x)
            print(Savings_Amount+x, "Avalable Balance")
            
        else:
            print("You Choosed Debit")
            y=int(input("Enter Amount You Want:"))
            print("Amount Debited Successfully:",y)
            print(Savings_Amount-y, "Available Balance")
    else:
        print("Pin Entered is Incorrect")
             
else:
    print("Account Number You Entered is Not Valid") 
        

