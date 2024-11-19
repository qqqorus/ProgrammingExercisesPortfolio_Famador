# Some Counting

# Write a loop that counts up from 0 to 50 in increments of 1.
for loop1 in range(0, 50): 
    print(loop1, end = ' ')
    if loop1 == 50:
        break # using break so the numbers won't continue displaying connected to the previous loop 
print()
    
# Write a loop that counts down from 50 to 0 in decrements of 1.
for loop2 in range(50, 0, -1):
    print(loop2, end = ' ')
    if loop1 == 0:
        break
print()

# Write a loop that counts up from 30 to 50 in increments of 1.
for loop3 in range(30, 50):
    print(loop3, end = ' ')
    if loop1 == 50:
        break
print()

# Write a loop that counts down from 50 to 10 in decrements of 2.
for loop4 in range(50, 10, -2):
    print(loop4, end = ' ')
    if loop1 == 10:
        break
print()

# Write a loop that counts up from 100 to 200 in increments of 5.
for loop5 in range(100, 200, 5):
    print(loop5, end = ' ')
    if loop1 == 200:
        break
print()