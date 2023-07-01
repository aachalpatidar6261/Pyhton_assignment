class bank:
    def Exists(self,cname,acno,accounttype):
        self.cname=cname
        self.acno=acno
        self.accounttype=accounttype

        self.balance = 10000        

    
    def display(self):
        print("coustomer name :",self.cname)
        print("account number :",self.acno)
        print("balance :",self.balance)
        print("account type : ",self.accounttype)

bank = bank()

print("1. Current Account.           2. Saving Account.           3. NIR")

choice =int(input("Enter a number : "))
if choice ==1:
    accounttype="Current Account"
elif choice ==2:
    accounttype = "Saving Account"
elif choice==3:
    accounttype = "NIR"
else:
    print("Invalid choice")
cname = input("Enter customer name : ")
acno = input("Enter Account number : ")
bank.Exists(cname,acno,accounttype)
bank.display()