# Write a series of conditional tests. Create at least 10, with 5 true, 5 false
# Print a statement describing each test and your predicted results

car = 'prius'
print("Is car == 'prius'? I predict True.")
print(car == 'prius')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

username = 'andi567'
print("\nIs username == 'andi'? I predict False.")
print(username == 'andi')

guess_number = 27
print("\nIs guess number >= 24? I predict True.")
print(guess_number >= 24)

cats = ['smokey', 'gizmo', 'cinder', 'minx', 'casper', 'gidget', 'charlie']
print("\nIs 'hamtato' in cats? I predict False.")
print('hamtato' in cats)

print("\nIs ''Smokey'.lower()' in cats? I predict True.")
print('Smokey'.lower() in cats)

print("\nIs 'vivi' not in cats? I predict True.")
print('vivi' not in cats)

cats.append('leo')
print("\nIs 'Leo' in cats? I predict False.")
print('Leo' in cats)

print("\nIs guess_number == 26? I predict False.")
print(guess_number == 26)

print("\nIs guess number == 27? I predict True.")
print(guess_number == 27)

guess_number = 56

print("\nIs guess_number >= 0 and guess_number <= 50? I predict False.")
print(guess_number >= 0 and guess_number <= 50)

print("\nIs guess_number >= 50 and guess_number <= 100? I predict True.")
print(guess_number >= 50 and guess_number <= 100)

print("\nIs guess_number != 55? I predict True.")
print(guess_number != 55)

print("\nIs guess_number != 56? I predict False.")
print(guess_number != 56)

print("\nIs guess_number == 56 or guess_number == 57? I predict True.")
print(guess_number == 56 or guess_number == 57)

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')