# Movie theater charges based on age:
# # Under 3: free
# # Btwn 3 & 12: $10
# # Over 12: $15
# Write a while loop that asks users their age & tells them the cost of tickets

active = True

prompt = "\nWelcome to RealWorld theater! How old are you?"
prompt += "\n(Enter 'q' to quit.)"

while active == True:
    age = input(prompt)

    if age == 'q':
        active = False
        print("Enjoy the movie!")
    elif int(age) < 3:
        print("Your ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print("Your ticket is $10.")
    elif int(age) >= 13:
        print("Your ticket is $15.")