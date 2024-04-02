def main():
    player_tracker()
    board = initialiseBoard()
    displayBoard(board)
    
def player_tracker():
    currentplayer = 1
    
def initialiseBoard():
    board = []
    for _ in range(6):
        row = []
        for _ in range(7):
            row.append('-')
        board.append(row)
    return board
    
def displayBoard(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

if __name__ == "__main__":
    main()