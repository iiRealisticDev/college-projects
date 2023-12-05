names = ["Keith", "Lemon", "David", "Steinbeck", "Hindenburg"] # potential things to search for
to_search = input("Provide a name to search for: ") # what to see if is in the list
found = False # whether or not it is found - for the sake of the outer scope

for idx, val in enumerate(names): # loop through the names list
  if val == to_search: # if the value is equal to the query
    print(f"Item found at index {idx}") # print where it was found
    found = True # assign "True" to the found variable
    break # end the loop

if not found: # if found is still False
  print("Item is not in list.") # output that it was not found