# Modify favorite_numbers so each person can have more than 1 number
# Print each person's name and favorite numbers

favorite_numbers = {
    'corey' : [32, 21],
    'ellen' : [29, 30, 31],
    'joseph' : [28],
    'maya' : [14, 19, 34, 57],
    'alex' : [37, 101],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is:")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"{number}")