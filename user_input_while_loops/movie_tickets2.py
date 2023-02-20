# Movie theater charges based on age:
# # Under 3: free
# # Btwn 3 & 12: $10
# # Over 12: $15
# Write a while loop that asks users their age & tells them the cost of tickets

# Write a version of movie_tickets.py that :
# # Uses a conditional test in the while loop to stop the loop
# # Uses an active variable to control how long the loop runs
# # Uses a break statement to exit the loop when the user enters a quit value

active = True

prompt = "\nWelcome to RealWorld theater! How old are you?"
prompt += "\n(Enter 'q' or 'quit' to quit.)"

while active == True:
    age = input(prompt)

    if age == 'q':
        active = False
        print("Enjoy the movie!")
    elif age == 'quit':
        print("Have a nice day!")
        break
    elif int(age) < 3:
        print("Your ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print("Your ticket is $10.")
    elif int(age) >= 13:
        print("Your ticket is $15.")