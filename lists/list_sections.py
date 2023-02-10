# Slicing a list

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])

print(players[1:4])

print(players[:4])

print(players[2:])

print(players[-3:])

# Looping through a slice

print("These are the first three players on the team:")
for player in players[:3]:
    print(player.title())

# Copying a list - do NOT set friends_foods = my_foods or lists will not remain separate

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My friend's favorite foods are:")
print(friends_foods)

my_foods.append('ice cream')
friends_foods.append('cookies')

print("My friend's favorite foods are:")
print(friends_foods)

