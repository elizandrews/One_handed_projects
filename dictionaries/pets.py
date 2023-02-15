# Make several dictionaries that each represent a different pet
# In each dictionary, include the type of animal and owner's name
# Store dictionaries in a list called pets
# Loop through the list and print everything you know about each pet

charlie_pet = {
    'animal_type' : 'cat',
    'owner' : 'ellen',
    }

arthur_pet = {
    'animal_type' : 'dog',
    'owner' : 'megan',
    }

leo_pet = {
    'animal_type' : 'cat',
    'owner' : 'gwen',
    }

scout_pet = {
    'animal_type' : 'cat',
    'owner' : 'morgan'
    }

atticus_pet = {
    'animal_type' : 'cat',
    'owner' : 'morgan'
    }

pets = [charlie_pet, arthur_pet, leo_pet, scout_pet, atticus_pet]

for pet in pets:
    print(pet)