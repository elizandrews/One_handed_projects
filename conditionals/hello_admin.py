# Make a list of 5 or more usernames, including 'admin'
# Loop through the list and add a greeting for each user
# # If the username is admin, print a special greeting

usernames = ['python356', 'y3r0c', 'matt12345', 'l2thdoctor', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, good to see you!")