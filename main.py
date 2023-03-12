print("----------Expense Tracker----------")
while True:
        op1 = int(input("1. Add a transaction\n2. View transactions\n3. Quit App\nEnter an option number: "))
        if op1 == 1:
            print("----------Add Transaction---------")
            name = raw_input("Enter name of the person: ")
            amount = int(input("Enter amount (only num): "))
            description = raw_input("Give a short description: ")
            with open("expenses", "a") as at:
                at.write(name + "\t\t" + str(amount) + "\t\t\t" + description + "\n")
            print("Transaction added!")
            print("------------------------------------------------")
        elif op1 == 2:
            print("----------View Transactions----------")
            with open("expenses", "r") as vt:
                trans = vt.read()
            print("Name\t\tAmount\t\tDescription")
            print("------------------------------------------------")
            print(trans)
            print("------------------------------------------------")
        elif op1 == 3:
            break
        else:
            print("Invalid Input!")
