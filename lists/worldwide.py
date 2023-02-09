# Store 5 places in the world you'd like to visit in a non-alphabetized list and print

travels = ['Egypt', 'Barcelona', 'Peru', 'Mexico', 'Japan']
print(travels)

# Temporarily sort in alphabetical order
print(sorted(travels))

print(travels)

# Temporarily sort in reverse-alphabetical order

print(sorted(travels, reverse=True))

print(travels)

# Permanently sort in reverse order

travels.reverse()
print(travels)

# Reset in original order

travels.reverse()
print(travels)

# Permanently sort in alphabetical order

travels.sort()
print(travels)

# Permanently sort in reverse alphabetical order

travels.sort(reverse=True)
print(travels)