# Make a list called sandwich_orders and fill with names of various sandwiches
# Make an empty list called finished_sandwiches and loop through
# Print a message for each order, and as each is made, move to finished list
# After all sandwiches are made, print a message listing each sandwich made

sandwich_orders = ['italian', 'pastrami', 'tuna melt', 'italian', 'blt']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Your {current_sandwich} is being made.")
    finished_sandwiches.append(current_sandwich)

print(f"\nThe following sandwiches have been completed:")
for sandwich in finished_sandwiches:
    print(sandwich)