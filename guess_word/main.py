stored_pass = "hello"
password = ""
pass_mismatch = stored_pass != password

guesses = 0
pass_len = len(stored_pass)

# count how many times a character appears in a word
def appears(word: str, query: str):
  appears_amt = 0
  for char in word:
    if char == query:
      appears_amt += 1
  
  return appears_amt

print(f"There are {pass_len} characters in the password.")

while pass_mismatch:
  if guesses == 5 and pass_mismatch:
    print("Incorrect, you lose!")
    exit(0)
  elif guesses == 1:
    print(f"The first letter of the word is: {stored_pass[0]}")
  elif guesses == 3:
    print(f"The last character of the word is {stored_pass[pass_len-1]}")

  guesses += 1
  res = input("Enter your guess: ")

  if len(res) == 1:
    print(f"The word contains the letter {res} {appears(stored_pass, res)} times.")
  password = res
  pass_mismatch = stored_pass != password

print("Correct, you win!")