# Store number 1 - 9 in a list
# Loop through the list
# Use an if-elif-else chain to print the proper ordinal ending for each number

ordinal_numbers = list(range(1, 10))

for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif number >= 4 and number < 10:
        print(f"{number}th")