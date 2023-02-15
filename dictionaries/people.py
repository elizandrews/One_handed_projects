# Start with person.py
# Make 2 new dictionaries representing different people
# Store all 3 dictionaries in a list called people
# Loop through your list of people and print everything you know about each

gwen_dictionary = {
    'first_name' : 'gwen', 
    'last_name' : 'smith', 
    'age' : 34,
    'city' : 'mauldin'
    }

corey_dictionary = {
    'first_name' : 'corey',
    'last_name' : 'andrews',
    'age' : 32,
    'city' : 'little rock'
    }

joseph_dictionary = {
    'first_name' : 'joseph',
    'last_name' : 'andrews',
    'age' : 27,
    'city' : 'chattanooga'
}

people = [gwen_dictionary, corey_dictionary, joseph_dictionary]

for person in people:
    print(person)