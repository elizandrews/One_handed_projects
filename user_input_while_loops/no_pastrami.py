# Using the list sandwich_orders from deli.py, ensure pastrami appears 3+ times
# Add code to print a message that the deli has run out of pastrami
# Use a while loop to remove all occurances of 'pastrami' from sandwich_orders
# Ensure no pastrami orders end up in finished sandwiches

sandwich_orders = ['italian', 'pastrami', 'tuna melt', 'italian', 'blt',
                    'pastrami', 'blt', 'italian', 'pastrami', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we are currently out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Your {current_sandwich} is being made.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been completed:")
for sandwich in finished_sandwiches:
    print(sandwich)