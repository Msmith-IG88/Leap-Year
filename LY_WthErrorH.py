"""
Name: Michael Smith
Date: April 2021
Description:
This program takes an input from the user and checks
to see if that input is a leapyear. 
Instructions:
1. Navigate to the directory this python file is in.
2. Enter "python3 LY_WthErrorH.py" on the commandline, 
this should start the program.
3. The software will ask you to enter a year and output the results 
all to the commandline.
"""
def leapYear():
    year = input("Enter a year: ")
    while (year.isdigit() != True):
        print("Year entered was not valid")
        year = input("Enter a year: ")

    if ( int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0):
        print(year + " is a leap year")
    else:
        print(year + " is not a leap year")

leapYear()