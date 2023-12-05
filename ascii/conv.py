msg = ""

while True:
  char = input("Provide a character decimal: ")
  if char == "end":
    print(msg)
    exit(0)

  try:
    msg += chr(int(char))
  except:
    print("that is not a number")
  