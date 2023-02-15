# Dictionary is a collection of key-value pairs
# # Each key is connected with an associated value
# # # Value can be string, list, number, another dictionary

# Simple dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

# Adding new key-value pairs

print(alien_0)

alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

# Beginning with an empty dictionary

alien_1 = {}

alien_1['color'] = 'yellow'
alien_1['points'] = 10

print(alien_1)

# Modifying values in a dictionary

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# # Tracking an alien's movement speed
alien_0 = {'x-position' : 0, 'y-position' : 25, 'speed' : 'medium'}
print(f"The original position: {alien_0['x-position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New position: {alien_0['x-position']}")

# Removing key-value pairs permanently

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Dictionary of similar objects - include comma before final curly brace

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'java',
    'phil' : 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Using get() to access values
# # Using [] to retrieve value from dictionary may result in error if not there

alien_0 = {'x-position' : 0, 'y-position' : 25, 'speed' : 'medium'}

point_value = alien_0.get('points')
print(point_value)

# Looping through all key-value pairs in a dictionary

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'java',
    'phil' : 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through all keys in a dictionary

for name in favorite_languages.keys():
    print(name.title())

# # OR # #

for name in favorite_languages:
    print(name.title())

# Can also access value associate w/ key

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you prefer {language}.")

# Determine if particular key in dictionary using keys()

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a dictionary's keys in a particular order

for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values in a dictionary w/o checking for repeats

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Looping through all values in a dictionary w/ checking for repeats

for language in set(favorite_languages.values()):
    print(language.title())

# Building a set directly - sets do not retain items in a specific order

languages = {'python', ' rust', 'c', 'python'}
languages
# {'rust', 'python', 'c'}

