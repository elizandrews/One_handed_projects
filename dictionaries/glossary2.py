# Use glossary.py, but replace print statements with a loop
# Then, add 5 more terms to the glossary

glossary = {
    'list' : 'a data-type used to store multiple items in a single variable',
    'variable' : 'a symbolic name used as a pointer to an object',
    'tuple' : 'an immutable list',
    'dictionary' : 'a data-type that stores key-value pairs',
    'python' : 'a high level, general purpose programming language',
    }

glossary['key'] = 'identifier of a entry in a dictionary'
glossary['value'] = 'data associated with the key in a dictionary'
glossary['sort'] = 'method that returns variables in alphanumerical order'
glossary['string'] = 'a data-type that represents a sequence of characters'
glossary['float'] = 'a data-type that is a number with a decimal place'

for k, v in glossary.items():
    print(f"{k.title()} is defined as {v}.")