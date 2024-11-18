# Brute Force Attack

# use while loop
password = "12345" # defines the correct password
user_guess = input("Enter your password: ")
# maximum of 5 password attempts
attempts = 5

# use a while loop to repeatedly ask the user for the password until the correct one is entered.
while user_guess != password and attempts != 0:
    attempts -= 1
    print(f"You have {attempts} attempt(s) left.") # informs the user how many attempts they have left
    user_guess = input("Enter your password: ")
    if attempts == 0:
        print("The authorities have been alerted.") # if the maximum number of attempts is reached, inform the user that the authorities have been alerted.
# output an appropriate message when the correct password is entered.
if user_guess == password:
    print("Access Granted.")