class Bank:
    def __init__(self, owner, account_no):
        self.owner = owner
        self.account_no = account_no
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def transfer_money(self, to_account, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if self.balance >= amount:
            to_account.balance += amount
            self.balance -= amount
            print(f"Transfer Success! {amount:.2f} transferred from account {self.account_no} to {to_account.account_no}.")
            print(f"Your new balance: {self.balance:.2f}")
            print(f"Recipient's new balance: {to_account.balance:.2f}")
        else:
            print(f"Insufficient balance. Your current balance is {self.balance:.2f}, but you tried to transfer {amount:.2f}.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposit successful. Your new balance is {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        vat_rate = 0.15
        total_cost = amount + (amount * vat_rate)

        if self.balance >= total_cost:
            self.balance -= total_cost
            print(f"Withdrawal successful: {amount:.2f} (plus 15% VAT: {amount * vat_rate:.2f}).")
            print(f"Total deducted: {total_cost:.2f}.")
            print(f"Your new balance: {self.balance:.2f}")
        else:
            print(f"Insufficient funds for withdrawal. You tried to withdraw {amount:.2f} (plus {amount * vat_rate:.2f} VAT, total {total_cost:.2f}).")
            print(f"Your current balance is {self.balance:.2f}.")

    def display_account_info(self):
        """Prints all the account details."""
        print(f"Account Number: {self.account_no}")
        print(f"Account Holder: {self.owner}")
        print(f"Balance: {self.balance:.2f}")
        print("-" * 30) 
        