# Nesting - storing multiple dictionaries in a list or a list of items as values
# # in a dictionary

# A list of dictionaries

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# # Make an empty list for storing aliens
aliens = []

# # # Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# # # # # Change the first 3 aliens to yellow
######### Change the yellow aliens to green
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# # # Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print(". . .")

# # # Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# List in a dictionary

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
        "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# # Revisiting favorite languages poll to allow for multiple responses
favorite_languages = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"{language.title()}")

# Nesting a dictionary in a dictionary (gets complicated quickly)

users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris',
    },

}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# Good practice to make structure of multiple nested dictionaries identical