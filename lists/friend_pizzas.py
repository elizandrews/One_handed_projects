# Copy the list from pizzas.py. Make a new copy of the pizzas list as friend_pizzas

pizzas = ['supreme', 'cheese', 'margherita']
friend_pizzas = pizzas[:]

# Add a new pizza to the original list. Add a different pizza to friend_pizzas

pizzas.append('deep dish')
friend_pizzas.append('pepperoni')

# Prove you have 2 separate lists by printing messages using a for loop

print("My favorite pizzas are:")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
    print(pizza)