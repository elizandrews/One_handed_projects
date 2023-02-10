# Use foods.py (aka in list_sections.py) and write for loops to print each list of foods

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('ice cream')
friends_foods.append('cookies')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)