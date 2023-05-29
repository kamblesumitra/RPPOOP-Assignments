class BankAccount:
    def __init__(self, name, account_number, account_type):
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into the account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from the account. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_account_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")


# Function to create a bank account
def create_account():
    name = input("Enter account holder's name: ")
    account_number = input("Enter account number: ")
    account_type = input("Enter account type: ")
    return BankAccount(name, account_number, account_type)


# Function to perform account operations
def perform_operations(account):
    while True:
        print("\n--- Bank Account Operations ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Information")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_account_info()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


# Main program
print("Bank Account Program\n")

account = create_account()
perform_operations(account)
