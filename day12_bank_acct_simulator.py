# Bank Acount Simulator


# Global variable to store account balance
balance = 0.0
transaction_history = [] # to track deposit and withdraw

# Function to deposit money
def deposit(amount):
    global balance
    if amount <= 0:
        print("Deposit amount must be positive.")
        return
    balance = balance + amount
    transaction_history.append(f"Deposited: ${amount:.2f}")
    print(f"Successfully deposited ${amount:.2f}")

# function to withdraw money
def withdraw(amount):
    global balance
    if amount <= 0:
        print(" Withdrawal amount must be positive")
        return
    if amount > balance:
        print("Insufficient Funds! Withdrawal Cancelled")
    else:
        balance = balance - amount
        transaction_history.append(f"Withdrew: ${amount:.2f}")
        print(f"Successfully Withdrew: ${amount:.2f}")

# function to withdraw money
def check_balance():
    print(f" Current Balance: ${balance:.2f}")

def show_history():
    if not transaction_history:
        print(" No Transactions Yet")
    else:
        print("Transaction History: ")
        for t in transaction_history:
            print(" -", t)

# Main program loop
def main():
    while True:
        print("\n====== Jiggy Bank Account Simulator")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Quit")
        choice = input("Enter yout choice (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                deposit(amount)
            except ValueError:
                print("Invalid input. please enter a number.")
        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                withdraw(amount)
            except ValueError:
                print("Invalid input. please enter a number.")
        elif choice == "3":
            check_balance()
        elif choice == "4":
            show_history()
        elif choice == "5":
            print(" ThNK YOU FOR USING THE JIGGY BANK ACCOUNT SIMULATOR. GOODBYE!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5. ")

if __name__ == "__main__":
    main()

def main():

    first_action = int(input(
        "choose an option\n 1. deposit\n 2. withdraw\n 3. check balance \n >>"))
    if first_action == 1:
        deposit()
    elif first_action == 2:
        withdraw()
    elif first_action == 3:
        check_balance()

if __name__ == "__main__":
    main()








