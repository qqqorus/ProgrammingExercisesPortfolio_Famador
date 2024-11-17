# Days of the Month

# use a dictionary to map the month numbers (1-12) to the number of days in each month.
months_and_days = {1: 31, 
          2: 28, 
          3: 31, 
          4: 30, 
          5: 31, 
          6: 30, 
          7: 31, 
          8: 31, 
          9: 30, 
          10: 31, 
          11: 30, 
          12: 31}
# ask the user to input the month number.
user_month = int(input("Give me a month number from 1-12: "))

# use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
if user_month != 2 and user_month > 1 and user_month < 12: # setting number boundary
    days_in_month = months_and_days[user_month]
    print(f"The number of days in month {user_month} is {days_in_month}.")
# for february, ask the user if the year is a leap year and adjust the number of days accordingly.
elif user_month == 2:
    yes_leap_year = "Yes"
    no_leap_year = "No"
    leap_year = input("Is this year a leap year? ") # asking if this year is a leap year
    if leap_year.lower() == yes_leap_year.lower(): # .lower() ignores capitalization
        print("The number of days in month 2 is 29.")
    elif leap_year.lower() == no_leap_year.lower():
        print("The number of days in month 2 is 28.")
# if the user inputs a number that is less than 1 and greater than 12
else: 
    print("That is an invalid month number.")