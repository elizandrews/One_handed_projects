# Checking for special items

requested_toppings = ['sausage', 'green peppers', 'onions']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nYour pizza is finished!")

# As opposed to:

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now!")
    else:
        print(f"Adding {requested_topping}.")
    
print("\nYour pizza is finished!")

# Checking a list is not empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nYour pizza is finished!")
else:
    print("Are you sure you want a plain pizza?")

# Using multiple lists

available_toppings = ['mushrooms', 'pepperoni', 'sausage', 'olives',
                     'extra cheese', 'pineapple', 'green pepper']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nYour pizza is finished!")