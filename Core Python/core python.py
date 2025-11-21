class fruit:
    print("WElcome To Fruit Market")
    print("1. Manager.")
    print("2. Customer.")

    choice=input("Select your role : ")

    if choice==1:
        print("Fruits Market Manager")
        print(" ")
        print("1. Add Fruit Stock")
        print("2. Viwe Fruit Stock")
        print("3. Update Fruit Stock")

        ch = int(input("Enter your choice : "))
        if ch==1:
            print("ADD FRUITS STOCK")
            add_fruit = input("Enter FRUIT NAME : ")
            qty = int(input("ENTER QTY(int kg) : "))
            price = int(input("Enter PRICE : "))
            print("Do you want to perform more operation : Press Y for yes and N for no !")

        elif ch ==2:
            d = {add_fruit : {"Qty" : qty ,  }}