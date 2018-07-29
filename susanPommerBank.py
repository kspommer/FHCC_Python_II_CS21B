###########################################################
# Course:  CS21B Python Programming: Lab #3
# Name:  Susan Pommer
# Description:  This program creates a class
# which models a simple bank account and has features
# spanning deposits, withdrawals, interest and
# penalties.
# Driven by test file susanPommerLab3.py

# File name:  susanPommerBank.py
# Date:  January 30, 2018
###########################################################

## ------- DEFINE CLASS ------- ##

# Class which models a simple bank account
class BankAccount:

    ## Constructs a BankAccount object
    ## Assumes provided an initial deposit amount
    ## @param balance is initial deposit amount
    def __init__(self, initial_balance):
        # Default balance
        DEF_BALANCE = 0.0

        self._balance = initial_balance + DEF_BALANCE

    # Add deposit to account
    # @param amount    customer's deposit amount
    def deposit(self, amount):
        self._balance = self._balance + amount

    # Make withdrawal from account
    # If withdrawal < balance, calculate new balance
    # If withdrawal > balance, impose penalty
    #     and do not allow withdrawal
    ## @param amount is withdrawal amount
    ## @param PENALTY is penalty amount
    def withdraw(self, amount):
        # Define overdraw penalty amount
        PENALTY = 10.0

        # Calculate new balance or apply penalty
        if (amount > self._balance):
            self._balance = self._balance - PENALTY
        else:
            self._balance = self._balance - amount

    # Apply interest to the account
    # Program assumes today's date is end-of-month
    ## @param rate is monthly interest rate
    def add_interest(self, rate):
        if (self._balance > 0):   ## sanity check not neg balance
            self._balance = self._balance * (1 + (rate/100.0))

    # Return the current account balance
    def get_balance(self):
        return(self._balance)
