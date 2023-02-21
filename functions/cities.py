# Make a dictionary called cities with the names of 3 cities as keys
# # Include the country, population, and a fact about the city
# Print the name of each city and all the information you have about it

cities = {
    'barcelona' : {
        'country' : 'spain',
        'population' : 1_620_000,
        'fact' : 'Barcelona has two official languages: Catalan and Spanish.',
    },

    'tokyo' : {
        'country' : 'japan',
        'population' : 13_960_000,
        'fact' : 'Tokyo is home to a robot hotel.',
    },

    'lima' : {
        'country' : 'peru',
        'population' : 11_045_000,
        'fact' : 'Lima is the second largest city built in a desert.',
    },
}

for city, information in cities.items():
    print(f"\n{city.title()} :")
    country = information['country']
    population = information['population']
    fact = information['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\t{fact}")