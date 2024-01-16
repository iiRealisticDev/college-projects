
inp = input("Please provide a number: ")

try:
  inp = float(inp)
except ValueError:
  print("This is not a number!")
  exit()

if inp > 50:
  if inp > 75:
    print("The number is greater than 75")
  else:
    print("The number is greater than 50")
else:
  print("The number is less than or equal to 50")