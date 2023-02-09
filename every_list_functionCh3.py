learn_languages = ['french', 'italian', 'japanese', 'chinese', 'korean', 'spanish']

print(len(learn_languages))

print(f"I'll learn {learn_languages[0].title()} first.")
learn_languages.append('portuguese')
print(learn_languages)

learn_languages[4] = 'arabic'
print(learn_languages)

learn_languages.insert(4, 'korean')
print(learn_languages)

del learn_languages[5]
print(learn_languages)

popped_language = learn_languages.pop(5)
print(f"I have learned {popped_language.title()} before.")

learn_languages.remove('portuguese')
print(learn_languages)

print(sorted(learn_languages))
print(learn_languages)

print(sorted(learn_languages, reverse=True))
print(learn_languages)

learn_languages.sort()
print(learn_languages)

learn_languages.sort(reverse=True)
print(learn_languages)

learn_languages.reverse()
print(learn_languages)

print(learn_languages[-1])