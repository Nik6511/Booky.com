class B(object):
    def buy(self):
        n=int(input("Select your payment method\n 1. Card\n 2. UPI\n"))
        if n==1:
                    d1=input("Enter your 16 digit card Number\n")
                    d2=input("Enter your CVV\n")
                    len1=len(d1)
                    len2=len(d2)
                    while len1!=16 and len2!=3:
                        print("Invalid input! Please enter a valid input")
                        d1=input("Enter your 16 digit card Number\n")
                        d2=input("Enter your CVV\n")
                        len1=len(d1)
                        len2=len(d2)
                    print("___PAYMENT SUCCESSFUL___  Transaction ID:TQG1125216\n")
                    exit()
        elif n==2:
                    d1=input("Enter  your UPI id: ")
                    print("___PAYMENT SUCCESSFUL___  Transaction ID:TQG1125216\n")

        
class A(object):
    def __init__(self):
        pass
    
        
        pass
    def search():
        bname=input("Enter the Book Name or Author Name ISBN of the book\n")
        content=open('BankingDatabase.txt','r')
        L=content.readlines()
        for i in L:
            L1=i.split()
            if bname in L1:
                print("Book Found:",L1)
            
        

    print("----Welcome to Booky.com----\n")
    a=int(input('''Enter your choice
                   1.Search
                   2.Login
                   3.SignUp'''))
    while a<1 and a>3:
        print("Enter a valid choice\n")
        a=int(input('''Enter your choice
                   1.Search
                   2.Login
                   3.SignUp'''))
    if a==1:
        search()
    elif a==2:
        def Login():
            def Database():
                print("Create an account\n")
                user=input("Create a user Id\n")
                pwd=input("Create a password\n")
                content=open('Database.txt','w')
                content.write(user)
                content.write(" ")
                content.write(pwd)
                content.write(" ")
                content.close()
            d=input("Have an Account?[Y/N]")
            if d=='Y':
                user=input("Enter your User name\n")
                pwd=input("Enter your password\n")
                content=open('Database.txt','r')
                L=content.readlines()
                for i in L:
                    L1=i.split()

                
                    while user and pwd not in L1:
                        print("User NOT FOUND!\n")
                        print("TRY AGAIN!")
                        user=input("\nEnter your User name\n")
                        pwd=input("Enter your password\n")

                    print(user+" LOGGED IN!\n")
                    a=int(input('''Enter your choice
                                    1.Search
                                    2.Show Available Books
                                    '''))
                    if a==1:
                        search()
                        val=input("Do you want to buy this book?[Y/N]")
                        if val=='Y':
                            obj=B()
                            obj.buy()
                        elif val=='N':
                            exit()
                    elif a==2:
                        content=open('BankingDatabase.txt','r')
                        L=content.readlines()
                        print("Books in WAREHOUSE\n")
                        for i in L:
                            L1=i.split()
                            print("ISBN Book")
                            print(i,L1)
                        gg=int(input("Enter the ISBN of the Book\n"))
                        for j in range (0,gg):
                            for i in L:
                                L2=i.split()
                        print(L2)
                        a=int(input('''Enter your choice
                                    1.Buy this Book
                                    2.Exit
                                    '''))
                        if a==1:
                            obj=B()
                            obj.buy()
                        elif a==2:
                            exit()


            elif d=='N':
                Database()
                print("Account Created successfully!")
        Login()
    elif a==3:
        def Database():
                print("Create an account\n")
                user=input("Create a user Id\n")
                pwd=input("Create a password\n")
                content=open('Database.txt','w')
                content.write(user)
                content.write(" ")
                content.write(pwd)
                content.write(" ")
                content.close()
        Database()
        print("Account Created successfully!")
        user=input("Enter your User name\n")
        pwd=input("Enter your password\n")
        content=open('Database.txt','r')
        L=content.readlines()
        for i in L:
                    L1=i.split()

                
                    while user and pwd not in L1:
                        print("User NOT FOUND!\n")
                        print("TRY AGAIN!")
                        user=input("\nEnter your User name\n")
                        pwd=input("Enter your password\n")

                    print(user+" LOGGED IN!\n")
                    a=int(input('''Enter your choice
                                    1.Search
                                    2.Show Available Books
                                    '''))
                    if a==1:
                        search()
                        val=input("Do you want to buy this book?[Y/N]")
                        if val=='Y':
                            obj=B()
                            obj.buy()
                        elif val=='N':
                            exit()
                    elif a==2:
                        content=open('BankingDatabase.txt','r')
                        L=content.readlines()
                        print("Books in WAREHOUSE\n")
                        for i in L:
                            L1=i.split()
                            print("ISBN BookName AuthorName Price")
                            print(i,L1)
                        gg=int(input("Enter the ISBN of the Book\n"))
                        for j in range (0,gg):
                            for k in L:
                                L2=k.split()
                                count=count+1
                                if count==gg:
                                    print(L2)
                        a=int(input('''Enter your choice
                        1.Buy this Book
                        2.Exit
                        '''))
                        if a==1:
                            obj=B()
                            obj.buy()
                        elif a==2:
                            exit()
