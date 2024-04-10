board = []

def initialise_board():
    for i in range(6):
        board.append(["-", "-", "-", "-", "-", "-", "-"])

def player_turn():
    if currentplayer == "x":
        currentplayer = "o"
    elif currentplayer == "o":
        currentplayer = "x"
    print(f"Test: {currentplayer}")


def userinput():
    col = input("Select column (1 - 6): ")
    while True:
        while not col.isdigit():
            print("Must be a number between 1 and 6")
            col = input("Select column (1 - 6): ")
            while not col in range(1,7):
                print("Must be a number between 1 and 6")
                col = input("Select column (1 - 6): ")
    col = int(col)
    col = col - 1

    for row in range(5, -1, -1):
        if board[row][col] == "-":
            board[row][col] = "x"
            return

def print_board():
    for row in board:
        for col in row:
            print(col, end = " ")
        print("")

def main():
    initialise_board()
    while True:
        userinput()
        print_board()
        print("")

main()