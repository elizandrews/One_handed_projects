# Make a dictionary containing 3 major rivers and their primary location
# Use a loop to print a sentence about each river
# Use a loop to print each river name
# Use a loop to print each country represented

rivers = {
    'nile' : 'egypt',
    'amazon' : 'brazil',
    'ganges' : 'india',
    }

for river, country in rivers.items():
    print(f"The {river.title()} river flows through {country.title()}.")

print("\nThe rivers in our dictionary are:")
for river in rivers:
    print(river.title())

print("\nThe countries in our dictionary are:")
for country in rivers.values():
    print(country.title())