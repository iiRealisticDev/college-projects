from board import display_board
from random import randint

instruction_board = [
  ["1", "2", "3"],
  ["4", "5", "6"],
  ["7", "8", "9"]
]

def check_win(board: list[list[str]], plr: str):
  # Check rows
  for row in board:
    if all(cell == plr for cell in row):
      return True

  # Check columns
  for col in range(len(board[0])):
    if all(board[row][col] == plr for row in range(len(board))):
      return True

  # Check diagonals
  if all(board[i][i] == plr for i in range(len(board))) or all(board[i][len(board) - i - 1] == plr for i in range(len(board))):
    return True

  # Check draw
  if all(cell != " " for row in board for cell in row):
    return "DRAW"

  return False


def instructions():
  print(f"""
    Welcome to Noughts and Crosses!
    -------------------------------
    Instructions:
          
    This is a two player game
    Player 1 is crosses (X)
    Player 2 is naughts (0)
    The game is presented in a grid.

    {display_board(instruction_board)}         
To choose a position for your piece, enter the location number.
        """)
  
def move(board: list[list[str]], plr):
  pos = input(f"Player {plr}, provide a position: ")
  try:
    pos = int(pos) - 1
    row = pos // 3
    col = pos % 3
    # pos must be positive, between 1 and 9, and not already taken
    if pos < 0 or pos > 8:
      raise IndexError
  except ValueError:
    print("Please enter a number.")
    move(board, plr)
  except IndexError:
    print("Please enter a number between 1 and 9.")
    move(board, plr)
  
  if not board[row][col] == " ":
    print("That position is already taken, please try again.")
    return move(board, plr)
  board[row][col] = plr

  return board

  
def play(board):
  instructions()
  pve = input("Do you want to play against the computer? (y/n): ")
  if pve == "y":
    plr = "X"
    while True:
      print(display_board(board))
      won = check_win(board, plr)
      if won == True:
        print(display_board(board))
        print(f"Player {plr} wins!")
        ## play again
        res = input("Do you want to play again? (y/n): ").lower()
        if res == "y":
          board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
          ]
          return play(board)
        else:
          print("Thanks for playing!")
        break
      elif won == "DRAW":
        print(display_board(board))
        print("It's a draw!")
        res = input("Do you want to play again? (y/n): ").lower()
        if res == "y":
          board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
          ]
          return play(board)
        else:
          print("Thanks for playing!")
        break
      if plr == "X": # this is the actual player
        board = move(board, plr)
        plr = "0"
      else: # this is the computer
        # pick a random position that is not taken
        pos = randint(1, 9)
        row = (pos-1) // 3
        col = (pos-1) % 3
        while not board[row][col] == " ":
          pos = randint(1, 9)
          row = (pos-1) // 3
          col = (pos-1) % 3

        board[row][col] = plr
        plr = "X"
  else:
    plr = "X"
    while True:
      print(display_board(board))
      board = move(board, plr)
      won = check_win(board, plr)
      if won == True:
        print(display_board(board))
        print(f"Player {plr} wins!")
        ## play again
        res = input("Do you want to play again? (y/n): ").lower()
        if res == "y":
          board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
          ]
          return play(board)
        else:
          print("Thanks for playing!")
        break
      elif won == "DRAW":
        print(display_board(board))
        print("It's a draw!")
        break

      if plr == "X":
        plr = "0"
      else:
        plr = "X"