# Biography

# stores the information (name, hometown, and age) as key-value pairs in a dictionary.
# use variables with appropriate data types for each piece of information.
biography = {
    "first_name": "Quishia",
    "second_name": "Desiree",
    "hometown": "Cebu City",
    "age": 18
}

# print the values on separate lines using a single `print()` statement.
print("Name:", biography["first_name"], biography["second_name"])
print("Hometown:", biography["hometown"])
print("Age:", biography["age"])

##########

# have the user input their name, hometown, and age instead of hardcoding the values.
first_name = str(input("What is your first name? ")) # try giving both your first and second name when asked for your name. 
second_name = str(input("What is your second name? "))
full_name = first_name + " " + second_name
hometown = str(input("Where is your hometown? "))
age = int(input("How old are you? (Please input an integer): ")) 

# print the values on separate lines using a single `print()` statement.
print(f"Name: {full_name}")
print(f"Hometown: {hometown}")
print(f"Age: {age}")
# i am using f-strings to insert variables in strings rather than putting commas (,) and plus signs (+) because it's cleaner and less tedious.