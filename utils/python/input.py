class input_handler:
  def __init__(self):
    pass

  def get_input(self, prompt: str, validator: callable, *args):
    res = input(prompt)
    while not validator(res, args):
      res = input(prompt)

    return res
  
  def is_num(query: str):
    return lambda x: x.isdigit()
  
  def is_len(query: str, length: int):
    return lambda x: len(x) == length
  
  def is_in(query: str, array: list):
    return lambda x: x in array
  
  def is_not_in(query: str, array: list):
    return lambda x: x not in array
  
  def is_alpha(query: str):
    return lambda x: x.isalpha()
  
  def is_alnum(query: str):
    return lambda x: x.isalnum()
  
  def is_lower(query: str):
    return lambda x: x.islower()
  
  def is_upper(query: str):
    return lambda x: x.isupper()
  
  def is_title(query: str):
    return lambda x: x.istitle()