class Bank:
    def openaccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance

    def deposite(self,ammount):
        self.balance +=ammount
        print("Your balance after deposite : ",self.balance)
    
    def withdraw(self,ammount):
        if ammount<=self.balance:
            self.balance-=ammount
            print("Your balance after withdrow : ",self.balance)
        else:
            self.needs=ammount-self.balance
            print("Sorry! You Need To Another ",self.needs," Rs To withdraw.")
    
    def checkbalance(self):
        print("Your current balance : ",self.balance)

bank = Bank()
cname = input("enter customer name : ")
acno = int(input("enter account number : "))
balance = int(input("enter balance : "))

bank.openaccount(cname,acno,balance)

print("1. deposite             2. withdraw             3. checkbalance             4. Exit.")
print("-"*85)

while True:
    choice = int(input("Enter Your choice : "))

    if choice ==1:
        ammount = int(input("enter ammount for deposite : "))
        bank.deposite(ammount)
        print("-"*60)
    elif choice ==2:
        ammount=int(input("enter ammount for withdraw : "))
        bank.withdraw(ammount)
        print("-"*60)
    elif choice ==3:
        bank.checkbalance()
        print("-"*60)
    elif choice ==4:
        print("Thank you for using our service. Good bye.")
        print("-"*60)
        break
    else:
        print("Sorry! Invalid choice...")
