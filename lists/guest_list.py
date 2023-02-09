# Invite at least 3 people to dinner from a guest list

dinner_guests = ['Robin Williams', 'Steve Martin', 'Martin Short']

print(f"Dear {dinner_guests[0]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[1]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[2]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")

# Martin Short won't be able to make it
# Modify your list to remove the person who can't make it with another person you decided to invite
# Print a second set of invites for each person on the new list

absentee = dinner_guests.pop()
print(f"Declined: {absentee}")
dinner_guests.append("Trevor Noah")

print(f"Dear {dinner_guests[0]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[1]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[2]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")

# More space at the table, Add 3 guests
# Add print call informing people of larger table
# Add 1 new guest to beginning of list, middle of list, end of list
# Print new set of invitations for everyone on your list

print("I found a larger venue, so we'll be able to invite more people. The more the merrier!")
dinner_guests.insert(0, 'Eddie Murphy')
dinner_guests.insert(2, 'Taika Waititi')
dinner_guests.append('Chelsea Peretti')

print(f"Dear {dinner_guests[0]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[1]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[2]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[3]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[4]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")
print(f"Dear {dinner_guests[5]},\nPlease join me for dinner tomorrow night. We'll have a grand time!\nRegards,\nLiz")

# Oh no, the larger venue cancelled, so I can only invite 2 people to dinner!
# Remove guests one at a time until only 2 people remain. Each time, print an apology to the people you can't invite
# Print a message to the 2 remaining people letting them know they're still invited
# Use del to remove the last 2 people leaving an empty list and print to confirm the list is empty

print("Oh no, the larger venue cancelled, so I can only invite 2 people to dinner!")

uninvited_guests = dinner_guests.pop()
print(f"Dear {uninvited_guests},\nSadly, I will be unable to host you for dinner tomorrow. Let's do lunch instead?\nRegards,\nLiz")
uninvited_guests = dinner_guests.pop()
print(f"Dear {uninvited_guests},\nSadly, I will be unable to host you for dinner tomorrow. Let's do lunch instead?\nRegards,\nLiz")
uninvited_guests = dinner_guests.pop()
print(f"Dear {uninvited_guests},\nSadly, I will be unable to host you for dinner tomorrow. Let's do lunch instead?\nRegards,\nLiz")
uninvited_guests = dinner_guests.pop()
print(f"Dear {uninvited_guests},\nSadly, I will be unable to host you for dinner tomorrow. Let's do lunch instead?\nRegards,\nLiz")

print(f"Dear {dinner_guests[0]},\nYou may have heard that we have to change venues, but I'm still looking forward to seeing you!\nLiz")
print(f"Dear {dinner_guests[1]},\nYou may have heard that we have to change venues, but I'm still looking forward to seeing you!\nLiz")

print(len(dinner_guests))

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)