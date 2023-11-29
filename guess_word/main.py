stored_pass = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
password = ""
pass_mismatch = stored_pass != password

guesses = 0
pass_len = len(stored_pass)

print(f"There are {pass_len} characters in the password.")

while pass_mismatch:
  if guesses == 5 and pass_mismatch:
    print("Incorrect, you lose!")
    exit(0)
  
  if guesses == 1:
    print(f"The first letter of the word is: {stored_pass[0]}")
  
  if guesses == 3:
    print(f"The last character of the word is {stored_pass[pass_len-1]}")

  guesses += 1
  res = input("Enter your password: ")
  password = res
  pass_mismatch = stored_pass != password

print("Correct, you win!")