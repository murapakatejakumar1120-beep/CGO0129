while True:
    balance=1000000
    card="t"
    password=9999
    a=input("Insert card:")
    if a==card:
        print("Welcome Teja")
        b=int(input("Enter Password:"))
        if b==password:
              print("Options: 1.Balance Enquiry    2.Withdraw")
              c=int(input("Enter option number:"))
              if c==1:
                  print("Account Balance=",balance)
              elif c==2:
                  d=int(input("Enter amount to withdraw:"))
                  e=balance-d
                  print("Remaining Balance=",e)
              else:
                  print("Invalid Option")
        else:
            print("Invalid Password")
    else:
        print("Invalid card")

##
while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome pooja")
        password=int(input("enter the password"))
        if password==pwd:
            option=int(input('''choose the option
                                1.balance enq
                                2.withdraw'''))
            if option==1:
                print("your acc bal is",account)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=account-money
                print("rem acc bal is",balance)
            else:
                print("invalid option")
        else:
            print("incorrect password")
           
    else:
        print("invalid card")
