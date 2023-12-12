from ..utils.python.input import input_handler

input_handler = input_handler()

n1 = input_handler.get_input("Enter a number: ", input_handler.is_num)
n2 = input_handler.get_input("Enter a number: ", input_handler.is_num)
n3 = input_handler.get_input("Enter a number: ", input_handler.is_num)

arr = [n1, n2, n3]

for n in arr:
  if n >= 20:
    print("2")
  elif n >= 10:
    print("1")
  else:
    print("0")