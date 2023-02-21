# input() function - pauses program for user input & assigns to variable
# Interprets user entry as a string

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello {name}!")

# To write a prompt w/ more than 1 line, assign prompt to a variable
# Then, pass variable to the input function

prompt = "If you enter your name, we can personalize your messages."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to accept numerical input

age = input("How old are you? ")
age = int(age)
print(age >= 18)

# Modulo - divides one operator by another and returns the remainder

print(4%3)
print(5%3)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number%2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
