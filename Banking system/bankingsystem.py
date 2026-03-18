import json
class Customer:
    def __init__(self, name, accountno, balance):
        self.name = name
        self.accountno = accountno
        self.balance = balance
class Bank:
    def __init__(self):
        self.Customer = []

    # Create account
    def create_account(self):
        name = input("Enter your account name: ")
        accountno = int(input("Enter your account number: "))
        balance = float(input("Enter your balance: "))

        custo = Customer(name, accountno, balance)
        self.Customer.append(custo)

        print("Account created successfully!")

    # Deposit money
    def deposit_money(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter deposit amount: "))

        for a in self.Customer:
            if a.accountno == account_number:
                a.balance += amount
                print("Money deposited successfully!")
                print("New balance:", a.balance)
                return

        print("Account not found!")

    # Withdraw money
    def withdraw_money(self):
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter withdraw amount: "))

        for i in self.Customer:
            if i.accountno == account_number:
                if i.balance >= amount:
                    i.balance -= amount
                    print("Money withdrawn successfully!")
                    print("Available balance:", i.balance)
                else:
                    print("Insufficient balance!")
                return

        print("No account found!")

    # Check balance
    def check_balance(self):
        account_number = int(input("Enter your account number: "))

        for i in self.Customer:
            if i.accountno == account_number:
                print("Account holder:", i.name)
                print("Balance:", i.balance)
                return

        print("No account found!")

    # Show all accounts
    def all_account(self):
        if not self.Customer:
            print("No account available!")
        else:
            for i in self.Customer:
                print("Name:", i.name)
                print("Account number:", i.accountno)
                print("Balance:", i.balance)
                print("---------------------")
    #?save file
    def save_to_file(self):
        data = []
        for i in self.Customer:
          data.append({
            "name": i.name,
            "accountno": i.accountno,
            "balance": i.balance
        })

        with open("Customer.json", "w") as file:
           json.dump(data, file)
    #load json
    def load_save_file(self):
        try:
            with open("Customer.json","r") as file:
              data=json.load(file)
              for i in data:
                  entry=Customer(
                        i["name"],
                        i["accountno"],
                        i["balance"]
                  )
                  self.Customer.append(entry)
        except FileNotFoundError:
           pass          

# Create bank object
bank = Bank()
bank.load_save_file()

# Menu
while True:
    print("\n1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit_money()

    elif choice == "3":
        bank.withdraw_money()

    elif choice == "4":
        bank.check_balance()

    elif choice == "5":
        bank.all_account()

    elif choice == "6":
        bank.save_to_file()
        print("Data saved succesfully!")
        break

    else:
        print("Invalid choice!")