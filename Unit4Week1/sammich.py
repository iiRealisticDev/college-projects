import utils.input

input_handler = utils.input.input_handler()

sauce = input_handler.get_input("What sauce would you like? Brown or red? ", utils.input.input_handler.is_in, ["red", "brown"]).lower()

print(f"You have chosen {sauce} sauce.")

if sauce.lower() == "brown": # yes, this was a requirement for the program. racist.
  exit()

bread = input_handler.get_input("What bread would you like? White, brown or sourdough? ", utils.input.input_handler.is_in, ["white", "brown", "sourdough"]).lower()

print(f"You have chosen {sauce} sauce and {bread} bread.")