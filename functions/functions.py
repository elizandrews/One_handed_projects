# Function - named blocks of code to do one specific job

# Basic function
# Parentheses required, esp if info needed for function
# Docstring - describes what the function does

def greet_user():
    """Displays a simple greeting"""
    print("Hello!")

greet_user()


# Passing information to a Function

def greet_user(username):
    """Displays a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

# Argument - piece of info passed from function call to function (ex: 'jesse')
# Parameter - piece of info function needs to do its job (ex: username)


# # # # # Passing Arguments # # # # #
# Positional Arguments - need to be in same order as parameters are written

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type} is named {pet_name.title()}.")

describe_pet('cat', "charlie")
describe_pet('dog', 'arthur')


# Keyword Arguments - each argument consists of variable name and value --
# # # -- And lists and dictionaries of values
# Consists of name-value pair passed to a function
# Can be out of order, but always use exact names of parameters in def function

describe_pet(animal_type='cat', pet_name='charlie')


# Default Values #
# # If an argument for a parameter is passed into function call,
# # Then the argument is used
# # Else default value is used
# # # Helps simplify function calls and clarify ways function is used
# Note that position of arguments has been changed - default value last

def describe_cat(pet_name, animal_type='cat'):
    """Displays information about a pet cat"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type} is named {pet_name.title()}.")

describe_cat('smokey')
describe_cat(pet_name='moose', animal_type='dog')


# Remember, there are multiple ways to call most functions
# Use the one that works best for you!

# Unmatched arguments - providing fewer/more arguments than function needs
# # Python's error checking is helpful because it shows names of missing args


# # # # # Return Values # # # # #
# Function can process some data and return a value or set of values
# Return statement takes value from function & sends back to line calling funct
# When calling funct w/ return value, need to provide variable to assign it to

def get_formatted_name(first_name, last_name):
    """Return neatly formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)


# Making an Argument Optional #
# Allows people using function to provide extra info if they want
# Use default values to make 
# # Note: Python evaluates non-empty strings as True

def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return full name neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return(full_name.title())

musician = get_formatted_name2('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name2('elvis', 'presley')
print(musician)

# Returning a Dictionary #

def build_person(first_name, last_name):
    """Return dictionary of info about a person"""
    person = {'first' : first_name, 'last' : last_name}
    return person

musician = build_person('michael', 'jackson')
print(musician)

# Special value None used when variable has no specific value assigned
# None evaluates to False

def build_person2(first_name, last_name, age=None):
    """Return a dictionary of info about a person"""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person2('jimi', 'hendrix', age=27)
print(musician)

# # # # # Using Function w/ While Loop # # # # #
# Careful not to create an infinite loop!
# # We want user to be able to quit as easily as possible - give a way out!
# # break statement is useful in this case

def get_formatted_name(first_name, last_name):
    """Return neatly formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nWhat is your name?")
    print("(Enter 'q' at any time to quit.)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}!")


# # # # # Passing a List # # # # #

def greet_users(names):
    """Print a simple greeting to each user on the list"""
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a list in a function #
# Any changes made are permanent

# # Original Code for printing_models
# Start w/ designs that need printing
unprinted_designs = ['phone case', 'dodecahedron', 'robot pendant']
completed_models = []

# Simulate printing each design until none are left
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing Model: {current_design}")
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been completed: ")
for completed_model in completed_models:
    print(completed_model)


# # printing_models with functions

def print_models(unprinted_designs, completed_models):
    """
    Simulates printing each design until none are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all printed models"""
    print("\nThe following designs have been printed: ")
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case', 'dodecahedron', 'robot pendant']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List #
# Instead of using original list, pass function using a copy
# # Despite ability to do this, uses less time & memory with original list

# Example Calls:
# # function_name(list_name[:])
# # print_models(unprinted_designs[:], completed_models)

# # # # # Passing an Arbitrary Number of Arguments # # # # #

def make_pizza(*toppings):
    """Print the list of requested toppings"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('sausage', 'green pepper', 'onion')

# Creates a tuple called toppings containing all values function receives
# We can create a loop that runs through and describes pizza being ordered

def make_pizza2(*toppings):
    """Summarize pizza to make"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza2('pepperoni')
make_pizza2('sausage', 'green pepper', 'onion')

# Mixing Positional & Arbitrary Arguments #
# Arbitrary must be placed last in function definition
# Often see generic parameter name *args to collect arbitrary positional args

def make_pizza3(size, *toppings):
    """Summarize pizza to make"""
    print(f"\nMaking a {size}-inch pizza with toppings: ")
    for topping in toppings:
        print(f" - {topping}")

make_pizza3(14, 'pepperoni')
make_pizza3(10, 'sausage', 'green pepper', 'onion')

# Using Arbitrary Keyword Arguments #
# Used when want to accept arbitrary # of args, but won't know what info will be
# #  passed into the function
# Accepts as many key-value pairs as statement provides
# Often see parameter name **kwargs used to collect non-specific keyword args

def build_profile(first, last, **user_info):
    """Build dictionary containing everything we know about a user"""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', 
                            location='princeton',
                            field='physics')

print(user_profile)

# # # # # Storing functions in modules # # # # #
# Module - separate file can store functions in and import into main program
# Allows hiding detailed code to focus on higher-level logic & reusing functions
# # in different programs

# # # Best approach importing entire module or importing specific functs # # #

# # # Importing Entire Module # # #

# Separate file in same directory as pizza module
# Makes every function from module available to program
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(10, 'sausage', 'green pepper', 'onion')

# # # Importing specific functions from modules # # #

# Syntax: from module_name import function_name
# OR from module_name import function_1, function_2, function_3
from pizza import make_pizza

pizza.make_pizza(12, 'extra cheese')

# # # Using As to give function an alias # # #
# Name of function may conflict with existing name in program or long length
# Use alias - alternate name for function

from pizza import make_pizza as mp

mp(14, 'anchovies', 'pineapple')

# # # Using As to give Module an alias # # #
# To shorten/call more quickly the module

import pizza as p

p.make_pizza(20, 'pepperoni', 'sausage')

# # # Importing all functions in a module # # #
# Can call each function w/o dot notation
# do NOT use when working with larger modules you didn't write
# # Module has function name matching existing name in project, overwrites funct

from pizza import *

make_pizza(10, 'extra cheese', 'pepperoni')

# # # # # STYLING FUNCTIONS # # # # #

# # Limit lines of code to 79 characters
# # # If longer, press ENTER after open parentheses of definition line
# # # On Next Line, press TAB 2x to separate list of args from body of function
# # Separate multiple functions by 2 blank lines

# Example:
#def function_name(
#        parameter_0, parameter_1, parameter_2,
#        parameter_3, parameter_4, parameter_5):
#    function_body...