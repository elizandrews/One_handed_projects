# Write a loop that prompts the user to enter a series of toppings
# # until they enter a 'quit' value
# As they enter each topping, print a message saying you'll add that topping to
# # the pizza

active = True

prompt = "\nEnter a topping you would like added to your pizza:"
prompt += "\n(Enter 'quit' to quit adding toppings.)"

while active == True:
    topping = input(prompt)

    if topping == 'quit':
        active = False
        print("We have noted the toppings for your pizza.")
    else:
        print(f"\nWe are adding {topping} to your pizza!")