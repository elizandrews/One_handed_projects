# capitalization

name = "liz andrews"
print(name.title())

name1 = "Liz Andrews"
print(name1.upper())
print(name1.lower())

# f-strings - formatting

first_name = 'liz'
last_name = 'andrews'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Practice your Python, {full_name.title()}!")

reminder = f"I said PRACTICE, {full_name.title()}!!!"
print(reminder)

# formatting for easy reading

print("\tPython")
print("Languages:\n\tPython\n\tJava\n\tSQL")

favorite_language = '  Python  '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)

favored_language = ' python '
print(favored_language.rstrip())
print(favored_language.lstrip())
print(favored_language.strip())

# removing prefixes

nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
simplified_url = nostarch_url.removeprefix('https://')
print(simplified_url)

# apostrophes & quotations

strengths1 = "One of Python's strengths is its diverse community."
strengths2 = 'One of Python\'s strengths is its diverse community.'
print(strengths1)
print(strengths2)