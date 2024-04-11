board = []

def initialise_board():
    for i in range(6):
        board.append(["-", "-", "-", "-", "-", "-", "-"])

def player_turn(num):
    if num % 2 == 0:
        currentplayer = "x"
    else:
        currentplayer = "o"
    return currentplayer

def userinput(currentplayer):
    col = input("Select column (1 - 6): ")
    while True:
        while not col.isdigit():
            print("Must be a number between 1 and 6")
            col = input("Select column (1 - 6): ")
        col = int(col)
        if col > 0 and col <= 7:
            break
        else:
            print("Must be a number between 1 and 6")
            col = input("Select column (1 - 6): ")
    col = col - 1

    for row in range(5, -1, -1):
        if board[row][col] == "-":
            board[row][col] = currentplayer
            return

def print_board():
    for row in board:
        for col in row:
            print(col, end = " ")
        print("")

#def check_draw():
#def check_horizontal():
#def check_vertical():
#def check_diagonal():

def main():
    initialise_board()
    num = 0
    currentplayer = "x"
    while True:
        currentplayer = player_turn(num)
        userinput(currentplayer)
        print_board()
        print("")
        num = num + 1


main()