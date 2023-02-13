# Create a program that simulates how websites ensure unique usernames

# # Make a list of 5+ usernames called current_users

current_users = ['pytHon356', 'y3r0c', 'matt12345', 'l2thdoctor', 'admin']

# # Make another list of 5 called new_users, including 1+ from current_users

new_users = ['python123', 'L1z', 'MATT12345', '12thDoctor', 'john']

# # Loop through new_users list to check if username has already been used
# # # Make sure comparison is case insensitive - make copy of current_users

current_lowercase = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_lowercase:
        print("Please enter a new username.")
    elif user.lower() not in current_lowercase:
        print("This username is available.")
