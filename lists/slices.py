# Use one of the programs from this chapter - animals.py

animals = ['cheetah', 'leopard', 'giraffe']

for animal in animals:
    print(f"A {animal} has spots.")

print("All these animals have spots!")

# Add more to the list

animals.append('frogs')
animals.append('dalmations')

# Print a message with the first 3 items from the list using a slice

print("The first three animals are:")

for animal in animals[:3]:
    print(animal)

# Print the middle 3 animals with a message

print("The three middle animals are:")

for animal in animals[1:4]:
    print(animal)

# Print the last three animals

print("The last three animals are:")

for animal in animals[2:]:
    print(animal)