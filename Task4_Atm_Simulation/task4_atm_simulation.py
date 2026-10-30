
import math

class ATM:
    """Handles the account logic: balance, deposit and withdraw."""

    def __init__(self, balance=0):
        self._balance = balance

    def check_balance(self):
        return self._balance

    def _has_valid_decimals(self, amount):
        # money can only have up to 2 decimal places
        return abs(amount * 100 - round(amount * 100)) < 1e-9

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than 0."
        if not self._has_valid_decimals(amount):
            return False, "Amount can have at most 2 decimal places."
        self._balance += amount
        return True, f"{amount:.2f} deposited successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."
        if not self._has_valid_decimals(amount):
            return False, "Amount can have at most 2 decimal places."
        if amount > self._balance:
            return False, "Insufficient balance."
        self._balance -= amount
        return True, f"{amount:.2f} withdrawn successfully."


class ATMController:
    """Handles the menu and talks to the user."""

    def __init__(self, atm):
        self.atm = atm

    def get_amount(self, message):
        value = input(message)
        try:
            amount = float(value)
        except ValueError:
            return None
        if not math.isfinite(amount) or amount > 1_000_000_000:   # rejects nan, inf and huge numbers
            return None
        return amount

    def show_menu(self):
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def run(self):
        print("Welcome to the ATM!")

        try:
            while True:
                self.show_menu()
                choice = input("Choose an option (1-4): ").strip()

                if choice == "1":
                    print(f"Your current balance is: {self.atm.check_balance():.2f}")

                elif choice == "2":
                    amount = self.get_amount("Enter amount to deposit: ")
                    if amount is None:
                        print("Invalid input. Please enter a number.")
                    else:
                        _, message = self.atm.deposit(amount)
                        print(message)

                elif choice == "3":
                    amount = self.get_amount("Enter amount to withdraw: ")
                    if amount is None:
                        print("Invalid input. Please enter a number.")
                    else:
                        _, message = self.atm.withdraw(amount)
                        print(message)

                elif choice == "4":
                    print("Thank you for using the ATM. Goodbye!")
                    break

                else:
                    print("Invalid choice, please pick a number from 1 to 4.")
        except (KeyboardInterrupt, EOFError):
            print("\nThank you for using the ATM. Goodbye!")


if __name__ == "__main__":
    my_atm = ATM(balance=1000)   # starting balance
    controller = ATMController(my_atm)
    controller.run()
    
