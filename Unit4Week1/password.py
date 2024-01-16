username = input("Enter your username: ")
password = input("Enter your password: ")

valid_user = username != ""
valid_pass = password != ""

error_msg = ""

if not valid_pass and not valid_user:
  error_msg += "You have not entered a username or password."
elif not valid_user:
  error_msg += "You have not entered a username."
elif not valid_pass:
  error_msg += "You have not entered a password."

if error_msg != "":
  print(error_msg)
  exit()