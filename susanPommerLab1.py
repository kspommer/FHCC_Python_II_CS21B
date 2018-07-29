###########################################################
# Course:  CS21B Python Programming: Lab #1
# Name:  Susan Pommer
# Description:  This program asks user to input their last
#   name and student ID and executes and print a series
#   of calculations
#
# File name:  susanPommerLab1.py
# Date:  January 14, 2018

# Grade received:  22.5 / 22.5
###########################################################

import datetime

## ------- DEFINE MAIN PROGRAM ------- ##

def main():

    # Print today's date
    todays_date = datetime.date.today()
    print("Today's date is " + str(todays_date))

    # Ask user to input file name
    family_name = str(input("Enter your family name: "))

    # Calculate number of letters in last name
    nLet = len(family_name)

    # Ask user to input their student ID
    student_id = int(input("Enter your student ID: "))

    # Call function which calculates sum of the digits in the student ID
    myId = sum_digits(student_id)

    # Print myId and nLet
    print("myId is: " + str(myId))
    print("nLet is: " + str(nLet))

    # Call function which calculates sum of the digits in the student ID
    myId = sum_digits(student_id)

    # Execute and print a series of calculations
    # Expression 1
    expression_1 = myId / 2
    print("expression 1: %.2f" % expression_1)

    # Expression 2
    expression_2 = myId % 2
    print("expression 2: " + str(expression_2))

    # Expression 3
    expression_3 = calc_sequence_sum(nLet)
    print("expression 3: " + str(expression_3))

    # Expression 4
    expression_4 = myId + nLet
    print("expression 4: " + str(expression_4))

    # Expression 5
    expression_5 = abs(nLet - myId)
    print("expression 5: " + str(expression_5))

    # Expression 6
    expression_6 = myId/(nLet + 1100)
    print("expression 6: %.2f" % expression_6)

    # Expression 7
    expression_7 = (nLet % nLet) and (myId * myId)
    print("expression 7: " + str(expression_7))

    # Expression 8
    expression_8 = 1 or (myId/0)
    print("expression 8: " + str(expression_8))

    # Expression 9
    expression_9 = round (3.14, 1)
    print("expression 9: %.2f" % expression_9)


# ------------ FUNCTIONS ------------------------

# Function to sum the digits in the student ID
def sum_digits(id):
    
    # Initialize counter
    sum_digits = 0

    # Loop to sum digits in student ID
    while(id > 0):
        digit = id%10
        sum_digits = sum_digits + digit
        id = id//10

    return sum_digits

# Function to sum the numbers from 2 to and including nLet
def calc_sequence_sum(nLet):
    # Initialize counter
    sequence_sum = 0

    # Loop to sum from 2 to nLet
    for x in range (2, nLet+1):
        sequence_sum = sequence_sum + x

    return sequence_sum

# Call main function
main()

## -------------------- SAMPLE RUN --------------------------- ##
# Test run using PyCharm

#Today's date is 2018-01-14
#Enter your family name: Pommer
#Enter your student ID: 10824359
#myId is: 32
#nLet is: 6
#expression 1: 16.00
#expression 2: 0
#expression 3: 20
#expression 4: 38
#expression 5: 26
#expression 6: 0.03
#expression 7: 0
#expression 8: 1
#expression 9: 3.10

#Process finished with exit code 0

## -------------------------------------------------------------##
