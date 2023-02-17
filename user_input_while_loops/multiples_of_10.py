# Ask the user for a number. Then report whether it is divisible by 10 or not

number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is divisible by 10.")
else:
    print(f"The number {number} is not divisible by 10.")