# Is It Even

def main():
# the program should ask the user for a number from within the main function.
    number = float(input("Give me a random number: "))
    answer = even_or_odd(number)
    print(answer)
    # the message returned by the function should be printed from within the main function.

# the entered number should be passed to a function that determines if the value is even or odd.
def even_or_odd(number): # the argument 'number' is inside the parentheses because it is a parameter used to provide a value inside this function
    return f"{number:.0f} is even." if number % 2 == 0 else f"{number:.0f} is odd."
    # the function should return a message indicating whether the number is even or odd.

print(main())
