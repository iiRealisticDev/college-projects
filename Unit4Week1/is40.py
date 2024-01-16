user_num = input("Please provide a number: ")

try:
  user_num = int(user_num)
except ValueError:
  print("This is not a number!")
  exit()

if user_num == 40:
  print("You have entered 40.")
  