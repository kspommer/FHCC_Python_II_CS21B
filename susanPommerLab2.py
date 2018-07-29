###########################################################
# Course:  CS21B Python Programming: Lab #2
# Name:  Susan Pommer
# Description:  This program will complete a data verification
#    of user selected data file and throw an exception if
#   requirements are violated.
#
#  Exceptions covered include:
#  - user enters invalid file name
#  - file does not start with an integer, n
#  - file does not contain n data values
#    (tests for more / less than n values)
#    (tests for string, float data values)
#
# File name:  susanPommerLab2.py
# Date:  January 22, 2018
###########################################################

## ------- DEFINE MAIN PROGRAM ------- ##

def main():

    # Initialize loop variable
    file_name = "start"

    # Check for exit program condition
    while (file_name != "Exit") | (file_name != 'exit'):

        # Ask user to input file name
        file_name = str(input("Please enter the file name or exit to end the program: "))
        file_lowercase = file_name.lower()

        # End program if user inputs exit
        if (file_lowercase == "exit"):
            break

        # Call function to validate user entered a valid file
        if (valid_file(file_name) == False):
            continue

        # Open the file
        infile = open(file_name, 'r')

        # Read the first line of the file (note: it is String)
        first_number = infile.readline()

        # Call function to validate first row in file contains an integer
        # Valid_first_row = is_integer(first_number)
        if (is_integer(first_number) == False):
            continue

        # Convert first value in data file from string to integer
        n = int(first_number)
        #print(n)    ## TESTING ONLY

        # Read all remaining rows of data file into a list
        nums = infile.readlines()

        # Calculate length of list
        list_length = len(nums)
        #print(list_length)    ## TESTING ONLY

        # Check if data file contains the proper amount data
        # First line of the file should contain the total number of values
        if (list_length != n):
            print("Error: file contents invalid. \n")
            continue

        # Initialize loop, sum and print flag variables
        i = 0
        sum = 0
        flag = 0

        # Loop to check if each data value (in list) is an integer
        # if value is not an integer, break loops
        # if value is integer, adds to sum
        while i < n:
            # print(nums[i])   ##  TESTING ONLY
            if(is_integer(nums[i]) == False):
                flag = 1
                break
            else:
                sum = sum + int(nums[i])
                i = i + 1

        # Check print flag; print if meets all requirements
        if flag != 1:
            print("The sum is " + str(sum) + "\n")

        # Close file
        infile.close()


# ------------ FUNCTIONS ------------------------
# Function to check if valid file name input by user
def valid_file(file_name):
    try:
        infile = open(file_name, 'r')
    except FileNotFoundError:
        print("Error: not a valid file \n")
        return False


# Function to check if a string in file is an integer
def is_integer(number):
    try:
        int(number)
    except ValueError:
        print("Error: file contents invalid. \n")
        return False


# Call main function
main()

## -------------------- SAMPLE RUN --------------------------- ##
# Test run using PyCharm
# Jan 22, 2018 - 6:35 PM

#"C:\Users\Susan Dog\venv\Scripts\python.exe" "C:/Pommer Files/CLASSES/FHC CS21B/susanPommerLab2.py"
#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\good.dat
#The sum is 55

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\good22.dat
#The sum is 253

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\bad1.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\bad2.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\bad.dat
#Error: not a valid file

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\bad3.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\bad4.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\bad5.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\float.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\float3.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\float3-3.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\float3-3c.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\dddd
#Error: not a valid file

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\float3-4.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: C:\Pommer Files\CLASSES\FHC CS21B\Assignment 2 data\float3-4-2.dat
#Error: file contents invalid.

#Please enter the file name or exit to end the program: EXIT

#Process finished with exit code

## -------------------------------------------------------------##
