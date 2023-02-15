# Using dictionary favorite_languages
# Make a list of people who should take the poll. Include some names from poll
# Loop through list of people who should take poll
# # If they have taken the poll, print a message thanking them for responding
# # If not, print a message inviting them to take the poll

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'java',
    'phil' : 'python',
    }

requested = ['jen', 'ethan', 'edward', 'jacob', 'sarah', 'phil', 'caroline']

for name in requested:
    print(f"Hi, {name.title()}!")

    if name in favorite_languages:
        print("Thank you for taking the poll!")
    else:
        print("Please take a moment to take our poll.")