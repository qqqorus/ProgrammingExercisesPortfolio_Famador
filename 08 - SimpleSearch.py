# Simple Search

names = ["Jake".lower(), "Zac".lower(), "Ian".lower(), "Ron".lower(), "Sam".lower(), "Dave".lower()] # list of names
# names are in lowercase to ignore capitalization

user_search = input("Who is the person you want to search for?: ") # allows the user to input the search term instead of using a predefined value

if user_search.lower() in names:
    print(f"{user_search} is in the list.")
else:
    print(f"{user_search} is not in the list.")