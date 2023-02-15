# Make a dictionary called favorite_places with 3 names and 1-3 places each
# Loop through the dictionary and print each name and their fav places

favorite_places = {
    'andrew' : ['hilton head', 'atlanta', 'greenville'],
    'patrick' : ['atlanta', 'los angeles'],
    'kaitlyn' : ['hilton head'],
    }

for person, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{person.title()}'s favorite place is:")
    else:
        print(f"\n{person.title()}'s favorite places are:")
    for place in places:
            print(f"\t{place.title()}")