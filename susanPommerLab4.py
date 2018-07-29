###########################################################
# Course:  CS21B Python Programming: Lab #4
# Name:  Susan Pommer
#
# Description:  This program asks user to input a date
# in mm/dd/yyyy format.
# Input reviewed for following invalid formats:
# * month and date not two digits
# * year not four digits
# * not separated by slashes
# * day = 31 in April, June, Sept and Nov
# * day = 29, 30, 31 in February
#
# Program converts and prints date in format:
#   month name day, year
#   month is spelled out;
#   day is 2 digit d;
#   year if 4 digit yyyy
#
# File name:  susanPommerLab4.py
# Date:  February 5, 2018
###########################################################

# Import Regression Expression  __ CHECK THIS
import re

## ------- DEFINE MAIN PROGRAM ------- ##

def main():

    # Number of loops of program
    NUM_DATES = 5

    # Initialize loop variable
    i = 0

    # Loop five times to ask user for input dates
    while (i < NUM_DATES):
        # Request input date to convert; define format
        date_to_convert = str(input("Enter a date (mm/dd/yyyy): "))

        # This pattern looks for proper date format
        # Months from 01 - 12
        # Days from 01 - 31 (check later for months < 31 days)
        # Years from 0000 - 9999
        pattern = '(?P<month>[0][1-9]|[1][0-2])/+' \
                  '(?P<day>[0][1-9]|[1-2][0-9]|[3][0-1])/+' \
                  '(?P<year>[0-9]\\d{3}$)'

        # Checks validity of day, given month
        # Checks for user input errors (e.g. 3 digit month)
        # Errors and exits program if not a valid date
        try:
            # Regression match using pattern and user input date
            # Splits input; creates dictionary to store month, day, year
            regexp = re.match(pattern, date_to_convert).groupdict()

            # print(regexp)  ## FOR TEST ONLY

            # Get month and day from dictionary
            cal_month = regexp.get('month')
            cal_day = regexp.get('day')
            cal_year = regexp.get('year')

            # Call function - check 30-day months for day = 31
            check_30_months(cal_month, cal_day)

            # Call function -- check February for days 29, 30 or 31
            check_feb(cal_month, cal_day)

        # error is receive compiler AtttributeError
        except AttributeError:
            print_error()

        # increment loop variable
        i = i+1

        # Call function to translate month to month name
        month_name = id_month_name(cal_month)

        # Print converted date
        print("The converted date is: " + month_name +
              ' ' + cal_day + ', ' + cal_year +'\n')

# ------------ FUNCTIONS ------------------------

# Function to check 30 day months for 31st day
def check_30_months(cal_month, cal_day):
    # watching my line length :-)
    if (cal_month == '04') or (cal_month == '06') or \
            (cal_month == '09') or (cal_month == '11'):
        if (cal_day == '31'):
            print_error()

# Function to February for 29th, 30th, 31st date
# NOTE:  Does not consider leap years
def check_feb(cal_month, cal_day):
    # watching my line length :-)
    if (cal_month == '02'):
        if (cal_day == '29') or (cal_day == '30') or \
            (cal_day == '31'):
            print_error()

# Function to print error and exit program
def print_error():
    print('Input error')
    exit(0)

# Function to translate month to month name
def id_month_name(cal_month):
    # List of calendar month names
    month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September',
                   'October', 'November', 'December']

    index = int(cal_month) - 1
    return month_names[index]


# Call main function
main()

## -------------------- SAMPLE RUN --------------------------- ##
# Test run using PyCharm
#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab4-3.py"
#Enter a date (mm/dd/yyyy): 01/01/0001
#The converted date is: January 01, 0001

#Enter a date (mm/dd/yyyy): 02/05/2018
#The converted date is: February 05, 2018

#Enter a date (mm/dd/yyyy): 12/31/9999
#The converted date is: December 31, 9999

#Enter a date (mm/dd/yyyy): 02/28/5562
#The converted date is: February 28, 5562

#Enter a date (mm/dd/yyyy): 02/29/5562
#Input error

#Process finished with exit code 0
## -------------------------------------------------------------##
