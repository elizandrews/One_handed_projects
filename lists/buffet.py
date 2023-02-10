# Buffet at a restaurant only offers 5 basic foods. Store in a tuple.

buffet_foods = ('steak', 'potatoes', 'broccoli', 'chicken', 'green beans')

# Use a for loop to print each food the restaurant offers

print("Brian's Buffet serves:")
for food in buffet_foods:
    print(food)

# The restaurant changes its menu, replacing two menu items. Add a line that rewrites the tuple and print revised menu

buffet_foods = ('steak', 'potatoes', 'broccoli', 'pork', 'rice')

print("\nBrian's buffet is now serving:")
for item in buffet_foods:
    print(item)