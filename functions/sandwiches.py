# Write a function that accepts a list of items a person wants on a sandwich
# Should have 1 parameter that collects as many items as call provides
# Should print a summary of each sandwich being ordered
# Call function 3+ times with different number of toppings being ordered

def build_sandwich(bread, *toppings):
    """Print the sandwich details being ordered"""
    print(f"Making a sandwich on {bread} with toppings:")
    for topping in toppings:
        print(f" - {topping}")

build_sandwich('baguette', 'ham', 'butter', 'cheese')
build_sandwich('wheat', 'grape jelly', 'peanut butter')
build_sandwich('rye', 'pastrami', 'mustard')