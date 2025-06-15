from model import Bank
accounts = {}

def get_account(account_no):
    """Helper function to retrieve an account from the dictionary."""
    if account_no in accounts:
        return accounts[account_no]
    else:
        print(f"Error: Account {account_no} not found.")
        return None

def main_menu():
    """Displays the main menu options."""
    print("\n" + "="*30)
    print(" Welcome to the Basic Bank System!")
    print("="*30)
    print("1. Create Account")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. View Balance")
    print("5. View All Account Info")
    print("6. Exit")
    print("="*30)

def create_account():
    """Handles creating a new bank account."""
    print("\n--- Create New Account ---")
    account_no = input("Enter a unique account number: ").strip()

    if account_no in accounts:
        print(f"Error: Account number {account_no} already exists. Please choose a different one.")
        return

    owner_name = input("Enter account holder name: ").strip()

    
    if not owner_name:
        print("Account holder name cannot be empty.")
        return

    try:
        new_account = Bank(owner_name, account_no)
        accounts[account_no] = new_account
        print(f"Account {account_no} created successfully for {owner_name}.")
    except Exception as e:
        print(f"An error occurred while creating the account: {e}")

def handle_deposit():
    """Handles depositing funds into an account."""
    print("\n--- Deposit Funds ---")
    account_no = input("Enter account number: ").strip()
    account = get_account(account_no)

    if account:
        try:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")

def handle_withdraw():
    """Handles withdrawing funds from an account."""
    print("\n--- Withdraw Funds ---")
    account_no = input("Enter account number: ").strip()
    account = get_account(account_no)

    if account:
        try:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")

def handle_view_balance():
    """Handles viewing the balance of an account."""
    print("\n--- View Balance ---")
    account_no = input("Enter account number: ").strip()
    account = get_account(account_no)

    if account:
        print(f"Account {account.account_no} balance: {account.get_balance():.2f}")

def handle_view_all_accounts():
    """Handles viewing information for all created accounts."""
    print("\n--- All Account Information ---")
    if not accounts:
        print("No accounts created yet.")
        return

    for account_no, account in accounts.items():
        account.display_account_info()


# --- Main Program Loop ---
if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            create_account()
        elif choice == '2':
            handle_deposit()
        elif choice == '3':
            handle_withdraw()
        elif choice == '4':
            handle_view_balance()
        elif choice == '5':
            handle_view_all_accounts()
        elif choice == '6':
            print("Thank you for using the Basic Bank System! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")