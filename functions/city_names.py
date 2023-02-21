# Write a function called city_country that takes the name of city & country
# Function should return string formatted as "Santiago, Chile"
# Call your function with 3+ city-country pairs & print returned values

def city_country(city, country):
    """Return a city-country pair, neatly formatted"""
    location_pair = f"{city}, {country}"
    return location_pair

location = city_country('paris', 'france')
print(location.title())

location2 = city_country('milan', 'italy')
print(location2.title())

location3 = city_country('new York city', 'united states')
print(location3.title())

location4 = city_country(country='england', city='london')
print(location4.title())