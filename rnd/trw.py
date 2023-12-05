# Secure Password (Words --> ASCII)
from random import randint

# change a vowel to a special character
def vowel_to_spec(n_min: int, n_max: int):
  return chr(randint(n_min, n_max))

vowels = dict(a=(33, 37),e=(38,42),i=(43,47),o=(58,61),u=(91, 94))

# Convert a list of words to ASCII - changing each letters' values
def to_ascii(to_conv: str):
  password = ""
  splt = to_conv.lower()
  for char in splt:
    if vowels.get(char):
      nmin,nmax = vowels.get(char)
      password += vowel_to_spec(nmin, nmax)
    else:
      password += char
      
  return password

word1,word2,word3 = input("Provide a word: "),input("Provide a word: "),input("Provide a word: ")
as_ascii = to_ascii("".join([word1, word2, word3]))
print(as_ascii)