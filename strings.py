print("Giraffe\nAcademy")
print("Giraffe \"Academy\"")
print("Giraffe\\Academy")

# string variable
phrase = "New Giraffe Academy"
print(phrase)
print(phrase + " is cool")

# functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())     # returns a bool
phraseUpper = "NEW GIRAFFE ACADEMY"
print(phraseUpper.isupper())
# several functions can be applied in tandem
print(phrase.upper().isupper())

print(len(phrase))  # receives phrase as an argument and return its length

# string index
print(phrase[0])        # indexes start at 0
print(phrase[5])

# index function
print(phrase.index('A'))
print(phrase.index('f'))
print(phrase.index("Acad"))

# replace function
print(phrase.replace("New", "Old"))
print(phrase)
