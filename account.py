import random

class Account:
    def __init__(self, balance=0, acc_no=None):
        self.balance = balance
        self.acc_no = acc_no

    def set_balance(self, bal):
        self.balance = bal

    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} is credited")
        print("Remaining Balance:", self.balance)

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
            return
        self.balance -= amount
        print(f"Rs {amount} is debited")
        print("Remaining Balance:", self.balance)

def main():
  print("HELLO")
  print("WELCOME TO MAKAN BANK")
  while True: 
    choice = input("Do you have an existing account or a new account: ").lower()

    if choice in ("exist", "existing", "existing account","e"):  
        try:
            acc_no = int(input("Enter your account number: "))
        except ValueError:
            print("Invalid account number! Please enter digits only.")
            return
        print("Your account number is:", acc_no)
        acc1 = Account(balance=10000, acc_no=acc_no)
        while True:
            action = input("Check account balance or transaction history: ").lower().strip()
            if action in ("check", "balance", "account balance", "account"):
                print("Bank Balance:", acc1.balance)
            elif action in ("transaction history", "history", "transaction"):
                acc1.credit(5000)
                acc1.debit(8900)
            else:
                print("Not available")
            ag = input("Do you want to continue? (yes/no): ").lower().strip()
            if ag not in ("yes", "y"):
                print("Thank you")
                break
    elif choice in ("new", "new account","n"):
        n = input("Would you like to create a new account (YES/NO) ").strip().lower()
        if n in ("yes", "y"):
           print("You chose YES. Proceeding...")
           print("Enter Your Details")
           name = input("Name: ")
           pan_number = input("PAN Number: ")
           number = random.randint(1_000_000_000, 9_999_999_999)
           print(f"Details received — Name: {name}, PAN: {pan_number}")
           print("Your account is created successfully. Your account number is", number)
        elif n in ("no", "n"):
          print("You chose NO. Exiting...")
        else:
           print("Invalid input. Please enter 'yes' or 'no'.")
    else:
        print("Invalid choice. Please type 'existing account' or 'new account'.")   
    again = input("Do you want to continue banking? (yes/no): ").lower().strip()
    if again not in ("yes", "y"):
        print("Thank you for banking with us!")
        break
main()


