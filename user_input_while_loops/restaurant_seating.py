# Write a program that asks the user how many ppl are in their dinner group
# If the answer is more than 8, print a message saying they'll have to wait
# # for a table.
# Otherwise tell them their table is ready

dinner_party = input("How many guests are in your dinner party tonight? ")
dinner_party = int(dinner_party)

if dinner_party > 8:
    print("I'm sorry, you will have to wait for a table.")
else:
    print("We have a table available for you! Please follow me.")
