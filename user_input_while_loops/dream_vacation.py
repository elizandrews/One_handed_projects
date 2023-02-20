# Write a poll that asks about users dream vacations
# Include a block of code that prints the results

# Empty dictionary for responses
responses = {}

# Flag to indicate polling is active
polling_active = True

while polling_active == True:
    # Prompt for name & response
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would "
                "you go? ")

    # Stores response in dictionary
    responses[name] = location

    # Determine if anyone else will take the poll
    repeat = input("Would you like to have anyone else respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete
# Show the results

print("\n\n - - - Poll Results - - - ")
for name, location in responses.items():
    print(f"{name} would like to vacation in {location}.")