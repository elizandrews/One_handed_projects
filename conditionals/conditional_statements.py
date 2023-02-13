# basic example of if statement in for loop

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == ' bmw':
        print(car.upper())
    else:
        print(car.title())

# True and False equality conditional test
# '=' sets value
# '==' is equality operator - does the actual check to see if value is equal

car = 'bmw'
car == 'bmw'
# returns 'True'

car = 'audi'
car == 'bmw'
# returns 'False'

# Ignoring case when testing equality (aka - just want to test the value)

car = 'Audi'
car == 'audi'
# returns 'False'

car = 'Audi'
car.lower() == 'audi'
# returns 'True'
car
# returns 'Audi'

# Checking for Inequality using '!=' operator

requested_topping = 'mushrooms'

if 'requested_topping' != 'anchovies':
    print("Hold the anchovies!")

# Numercial comparisons

age = 18
age == 18
# returns 'True'

answer = 17
if answer != 42:
    print("Incorrect! Please try again.")

age = 19
age < 21
# returns 'True'

age <= 21
# returns 'True'

age > 22
# returns 'False'

age >= 22
# returns 'False'

# Checking multiple conditions

# Using 'and' and 'or' to test multiple conditions

age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)
# returns 'False'

age_1 = 23
(age_0 >= 21) and (age_1 >= 21)
# returns 'True'

age_0 = 22
age_1 = 18
(age_0 >= 21) or (age_1 >= 21)
# returns 'True'

age_0 = 19
(age_0 >= 21) or (age_1 >= 21)
# returns 'False'

# Checking whether a value is in a list using 'in'

requested_toppings = ['sausage', 'green peppers', 'onions']
'sausage' in requested_toppings
# returns 'True'

'pepperoni' in requested_toppings
# returns 'False'

# Checking whether a value is NOT in a list using 'not in'

banned_users = ['andrew', 'caroline', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean expressions to track conditions

game_active = True
can_edit = False

# Simple if statements

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# If-else statements

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register when you turn 18!")

# If-elif-else chain

age = 12
if age < 4:
    print("Your cost of admission is $0.")
elif age < 18:
    print("Your cost of admission is $25.")
else:
    print("Your cost of admission is $40.")

# OR (more efficiently)

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# Add senior discount for multiple elifs

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your cost of admission is ${price}")

# Sometimes, it's clearer to use another elif instead of else for specifics
# Or if you want to ensure your code runs only under correct conditions

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your cost of admission is ${price}")

# Testing multiple conditions for more than 1 block of code

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Add mushrooms")
if 'pepperoni' in requested_toppings:
    print("Add pepperoni")
if 'extra cheese' in requested_toppings:
    print("Add extra cheese")

print("\nYour order is completed!")