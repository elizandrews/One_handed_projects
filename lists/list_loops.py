# Basic for loop

magicians = ['penn', 'teller', 'houdini']

for magician in magicians:
    print(magician.title())

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see the next trick, {magician.title()}.")

print("Thank you all. That was a fantastic magic show!")

# numerical lists - range stops at the second value, does NOT count it

for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

# Creating a list of numbers

numbers = list(range(1, 6))
print(numbers)

# Skipping numbers in a range

even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Creating a list of squared numbers

squares = []

for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# # # OR # # #

cubes = []

for value in range(1, 11):
    cubes.append(value**3)

print(cubes)

# List comprehensions - generate numerical list in 1 line of code
squares2 = [value**2 for value in range(1, 11)]
print(squares2)

# Simple stats with numerical lists

digits = list(range(1, 11))

print(min(digits))

print(max(digits))

print(sum(digits))