# Battleships

co_ords = []
# loop through 10 times, add an array of 10 *s for each iteration into co_ords
for i in range(10):
    co_ords.append(["*"] * 10)

# print the co_ords array
def print_board():
    for row in co_ords:
        print(" ".join(row))

# print the board
print_board()

# see if the ship can fit in the board
def can_ship_fit(row: int, col: int):
    """
    Checks if a ship can fit in the given row and column position.

    Args:
        row (int): The row position.
        col (int): The column position.

    Returns:
        bool: True if the ship can fit, False otherwise.
    """
    row_fits = row + 1 < 10 and co_ords[row][col] == "*" and co_ords[row + 1][col] == "*"
    col_fits = col + 1 < 10 and co_ords[row][col] == "*" and co_ords[row][col + 1] == "*"
    return row_fits and col_fits

def ask_for_coords():
    """
    Prompts the user to enter row and column numbers within specified ranges [1-5] and [1-10] respectively.
    Checks if a ship can fit at the specified coordinates and prompts the user again if it can't.
    
    Returns:
    - A tuple containing the row and column numbers entered by the user.
    """
    row = int(input("Enter a row number [1-5]: "))
    while row < 1 or row > 5:
        row = int(input("Enter a row number [1-5]: "))

    col = int(input("Enter a column number [1-10]: "))
    while col < 1 or col > 10:
        col = int(input("Enter a column number [1-10]: "))

    can_fit = can_ship_fit(row - 1, col - 1)

    while not can_fit:
        print("Ship can't fit here")
        ask_for_coords()

    return (row, col)


def draw_ship(row: int, col: int):
    #draw the ship in a straight line, either horizontally or vertically, depending on the coords. each ship should be 5 spaces long
    co_ords[row][col] = "S"
    co_ords[row + 1][col] = "S"
    co_ords[row + 2][col] = "S"
    co_ords[row + 3][col] = "S"
    co_ords[row + 4][col] = "S"

def play():
    while True:
        row, col = ask_for_coords()
        draw_ship(row - 1, col - 1)
        print_board()
        if input("Do you want to play again? [y/n]: ") == "n":
            break
        else:
            play()

play()