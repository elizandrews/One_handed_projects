# Write a program that asks the user what kind of rental car they'd like
# Print a message about that car

car = input("What type of car would you like to rent? ")

if car.lower() == 'prius':
    print(f"\nI'm sorry, we do not currently have a {car.title()} available.")
else:
    print(f"\nLet me see if I can find you a {car.title()}.")