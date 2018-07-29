###########################################################
# Course:  CS21B Python Programming: Lab #3
# Name:  Susan Pommer
# Topic:  This program demonstrates the Bank Account class
# Description: Test driver for the Bank Account class
# from susanPommerBank.py file
#
# File name:  susanPommerLab3.py
# Date:  January 30, 2018
###########################################################

# Import BankAccount class from susanPommerBank.py
from susanPommerBank import BankAccount

def main():

    ##### CODE FOR TEST RUN #1 ######
    # Print Test Run output Header
    ## Test with withdrawal > balance

    # Print Test Run output Header
    print("Test Output for Run #1")

    # Instantiate a Bank Account object
    # with original balance of $1000
    account = BankAccount(1000.0)

    # Get and print account balance
    print_balance(account)

    # Deposit $500
    account.deposit(500.00)

    # Get and print account balance
    print_balance(account)

    # Withdraws $2000
    account.withdraw(2000.00)

    # Get and print account balance
    print_balance(account)

    # Adds 1% interest
    account.add_interest(1.0)

    # Get and print account balance
    print_balance(account)
    print(" ")

    #################################
    ##### CODE FOR TEST RUN #2 ######
    ## Test with withdrawal < balance; 10% interest
    # Print Test Run output Header
    print("Test Output for Run #2")

    # Instantiate a Bank Account object
    # with original balance of $100
    account = BankAccount(100.00)

    # Get and print account balance
    print_balance(account)

    # Deposit $5000
    account.deposit(5000.00)

    # Get and print account balance
    print_balance(account)

    # Withdraws $2000
    account.withdraw(2000.00)

    # Get and print account balance
    print_balance(account)

    # Adds 10% interest
    account.add_interest(10.0)

    # Get and print account balance
    print_balance(account)
    print(" ")

    ##################################
    ##### CODE FOR TEST RUN #3 ######
    # corner case -- zero initial balance
    # different order of other functions

    # Print Test Run output Header
    print("Test Output for Run #3")

    # Instantiate a Bank Account object
    # zero initial balance
    account = BankAccount(0.0)

    # Get and print account balance
    print_balance(account)

    # Deposit $50000
    account.deposit(50000.00)

    # Get and print account balance
    print_balance(account)

    # Adds 2% interest
    account.add_interest(2.0)

    # Get and print account balance
    print_balance(account)

    # Withdraws $4000
    account.withdraw(4000.00)

   # Get and print account balance
    print_balance(account)

#############  FUNCTIONS ###################################

# Print formatted current account balance
def print_balance(account):
    print("Account Balance: $%10.2f" % account.get_balance())


# Start program
main()

## -------------------- SAMPLE RUN --------------------------- ##
#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab3.py"
#Test Output for Run #1
#Account Balance: $   1000.00
#Account Balance: $   1500.00
#Account Balance: $   1490.00
#Account Balance: $   1504.90
#
#Test Output for Run #2
#Account Balance: $    100.00
#Account Balance: $   5100.00
#Account Balance: $   3100.00
#Account Balance: $   3410.00
#
#Test Output for Run #3
#Account Balance: $      0.00
#Account Balance: $  50000.00
#Account Balance: $  51000.00
#Account Balance: $  47000.00
#
#Process finished with exit code 0

## -------------------------------------------------------------##
