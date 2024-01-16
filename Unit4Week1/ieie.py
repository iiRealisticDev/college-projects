num = input("Please provide a number: ")

try:
  num = int(num)
except ValueError:
  print("This is not a number!")
  exit()

if num < 50:
  print("The number is less than 50")
elif num > 100:
  print("The number is greater than 100")
else:
  print("The number is between 50 and 100")