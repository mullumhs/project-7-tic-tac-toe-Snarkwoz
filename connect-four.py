board = []

def initialise_board():
    for i in range(6):
        board.append(["-", "-", "-", "-", "-", "-", "-"])

def userinput():
    col = int(input("Select col: "))
    col = col - 1
    board[0][col] = "o"

def print_board():
    for row in board:
        for col in row:
            print(col, end = " ")
        print("")

