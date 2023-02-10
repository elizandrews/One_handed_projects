# Tuples - an immutable list using parentheses instead of brackets

rectangle_dimensions = (200, 50)
print(rectangle_dimensions[0])
print(rectangle_dimensions[1])

# Technically, tuples are defined by the presence of a comma
# To define a tuple with only 1 value, must include a trailing comma

my_tuple = (1,)

# Using a for loop to loop through a tuple

for dimension in rectangle_dimensions:
    print(dimension)

# Cannot modify a tuple, but can assign a new variable to a tuple

print("Original dimensions:")
for dimension in rectangle_dimensions:
    print(dimension)

rectangle_dimensions = (400, 100)

print("\nNew Dimensions:")
for dimension in rectangle_dimensions:
    print(dimension)