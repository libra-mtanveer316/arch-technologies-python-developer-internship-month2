
# ATM SIMULATION

A console-based Python program that simulates a simple ATM. Users can check their balance, deposit money and withdraw funds. Built during Month 2 of my Python Development internship at **Arch Technologies**.

**Repository:** https://github.com/libra-mtanveer316/arch-technologies-python-developer-internship-month2

---

## Quick Start

### Run the program

```bash
python task4_atm_simulation.py
```

---

## How It Works

The program is split into two classes. `ATM` holds the account logic, and `ATMController` handles the menu and user input.

```text
Start
  |
  v
Create ATM object (starting balance = 1000)
  |
  v
Pass it to ATMController and call run()
  |
  v
Print welcome message
  |
  v
Show menu and ask for a choice
  |
  v
1 -> show current balance
2 -> ask amount -> deposit (greater than 0, at most 2 decimal places)
3 -> ask amount -> withdraw (greater than 0, at most 2 decimal places, not more than balance)
4 -> print goodbye message and exit
anything else -> "Invalid choice" message
  |
  v
Go back to the menu
```

### Classes

| Class | Responsibility |
|-------|----------------|
| `ATM` | Stores the balance in `_balance`. Methods: `check_balance()`, `deposit()`, `withdraw()` |
| `ATMController` | Shows the menu, reads user input and calls the `ATM` methods |

---

## Concepts Applied

| # | Concept |
|---|---------|
| 1 | Classes and objects (OOP) |
| 2 | Encapsulation of the balance inside the `ATM` class |
| 3 | Methods and return values |
| 4 | `while` loops |
| 5 | Conditional logic |
| 6 | `try` / `except` for input handling |
| 7 | f-strings |

---

## Example Session

```text
Welcome to the ATM!

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 1
Your current balance is: 1000.00

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 2
Enter amount to deposit: 500
500.00 deposited successfully.

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 3
Enter amount to withdraw: 2000
Insufficient balance.

===== ATM MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Choose an option (1-4): 4
Thank you for using the ATM. Goodbye!
```

---

## Files

| File | Purpose |
|------|---------|
| `task4_atm_simulation.py` | Main program — run this |
| `requirements.txt` | Dependency list (none — standard library only) |
| `README-Task4.md` | This file |

## Author

**Muhammad Tanveer**  
Python Development Intern — Arch Technologies