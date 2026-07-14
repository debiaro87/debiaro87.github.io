user_password=8357
balance=1000
print(" Welcome To our Bank ATM Machine !")
print("="*6)
print("Please insert your ATM card ")
print("="*6)
for attempt in range(1,4):
    password=int(input(f"attempt {attempt}/3 - enter your password:"))
    if password==user_password:
        print("="*10)
        print("login successfully !")
    
        while True:
            print("=====MENU====")
            print("1.Check Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            print("5.Fast Cash")
            print("6.change password")
            choice=int(input("Enter your choice:"))
            if choice==1:
                print("Your current balance",balance)
            elif choice==2:
                amount=int(input("how much you need to deposit:"))
                if amount<0:
                    print("please enter amount above zero")
                else:
                    balance+=amount
                    print("deposit successfully !")
                    print("now your balance is:",balance)
            elif choice==3:
                withdraw=int(input("Enter the amount:"))
                if withdraw<0:
                    print("invalid amount")
                elif withdraw > balance:
                    print("Insufficient balance ")
                else:
                    balance-=withdraw
                    print("withdrawn successfully !")
                    print ("your current balance is:",balance)
            elif choice==4:
                print('''thank you for your using our Bank ATM Machine have a nice time !''')
                break
            elif choice==5:
                print("1.100")
                print("2.200")
                print("3.599")
                print("4.1000")
                choice=int(input("enter your choice:"))
                if choice==1:
                    if balance>=100:
                        balance=balance-100
                        print("withdrawn successfully !")
                        print("your current balance is:",balance)
                    else:
                        print("insufficient balance")
                elif choice==2:
                    if balance>=200:
                        balance=balance-200
                        print("withdrawn successfully !")
                        print("your current balance is:",balance)
                    else:
                        print("insufficient balance")
                elif choice==3:
                    if balance>=500:
                        balance=balance-500
                        print("withdrawn successfully !")
                        print("your current balance is:",balance)
                    else:
                        print("insufficient balance")
                else:
                    if balance>=1000:
                        balance=balance-1000
                        print("withdrawn successfully !")
                        print("your current balance is:",balance) 
                    else:
                        print("insufficient balance")
            elif choice==6:
                old_password=int(input("enter your old password:"))
                if old_password==user_password:
                    new_password=int(input("enter new password:"))
                    confirm_password=int(input("confirm your new password:"))
                    if new_password==confirm_password:
                        user_password=new_password
                        print("your password has been changed successfully !")
                    else:
                        print("password doesn't match")
                if old_password!=user_password:
                    print("incorrect password")
            else:
                print("please enter correct choice between 1-5")

    else:
        print("in correct password")
        remaining=3-attempt
        if remaining>0:
           print(f"you have {remaining} attempt(s) remaining.")
        else:
            print("account locked !")
       
    
        
