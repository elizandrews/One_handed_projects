# Use hello_admin.py and add an if test to ensure the list is not empty
# # If the list is empty, print "We need to find some users!"

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, good to see you!")
else:
    print("We need to find some users!")