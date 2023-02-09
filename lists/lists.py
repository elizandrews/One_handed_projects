# basic list bicycles

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

first_bike = f"My first bicycle was a {bicycles[2].title()}."
print(first_bike)


# adding elements in a list using motorcycles list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('ducati')
print(motorcycles)


# Inserting new elements to a list

motorcycles.insert(0, 'suzuki')
print(motorcycles)


# Removing items from a list using del statement, can no longer access value removed

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)


# Removing items using pop() method, can access removed value if needed, pops from end of list if not specified

motorcycles.append('suzuki')
motorcycles.append('yamaha')

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle the author owned was a {last_owned.title()}.")

amazing_race = motorcycles.pop(1)
print(f"On the Amazing Race last season, they went to the {amazing_race.title()} factory in Italy.")

motorcycles.append('suzuki')
motorcycles.append('yamaha')
motorcycles.append('ducati')


# Removing items by value, deletes only first occurance of value, need to use loop if more than 1

motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is too expensive for me.")

# Permanent sort of a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# Temporary sort of a list, can also take reverse=True argument, sorting is more complex when all values aren't lowercase

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print(sorted(cars))

print(cars)

# Reverse order of a list (non-alphabetical, permanent)

cars.reverse()
print(cars)

# Finding the length of a list

print(len(cars))