import re

def count_vowels_and_consonants(sentence: str):
  vowels = 0
  consonants = 0
  # vowel regex
  vowels_regex = re.compile(r'[aeiou]', re.IGNORECASE)
  # consonant regex
  consonants_regex = re.compile(r'[bcdfghjklmnpqrstvwxyz]', re.IGNORECASE)

  for letter in sentence:
    if vowels_regex.match(letter):
      vowels += 1
    elif consonants_regex.match(letter):
      consonants += 1
  return (vowels, consonants)


sentence = input("Enter a sentence: ")
vowels, consonants = count_vowels_and_consonants(sentence)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")