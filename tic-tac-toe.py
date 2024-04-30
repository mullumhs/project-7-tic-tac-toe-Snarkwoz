grid = []

def initialisegrid():
    for i in range (3):
        grid.append(["-", "-", "-"])

def player_turn(turncount):
    col = input("Select column (1 - 3): ")
    while True:
        while not col.isdigit():
            print("Must be a number between 1 and 3")
            col = input("Select column (1 - 3): ")
        col = int(col)
        if col > 0 and col <= 3:
            break
        else:
            print("Must be a number between 1 and 3")
            col = input("Select column (1 - 3): ")
    col = col - 1
    row = input("Select row (1 - 3): ")
    while True:
        while not row.isdigit():
            print("Must be a number between 1 and 3")
            row = input("Select row (1 - 3): ")
        row = int(row)
        if row > 0 and row <= 3:
            break
        else:
            print("Must be a number between 1 and 3")
            row = input("Select row (1 - 3): ")
    row = row - 1
    
    if turncount % 2 == 0:
        while True:
            if grid[row][col] == "-":
                grid[row][col] = "x"
                break
            else:
                print("That spot already has a symbol on it.")
                col = input("Select column (1 - 3): ")
                while True:
                    while not col.isdigit():
                        print("Must be a number between 1 and 3")
                        col = input("Select column (1 - 3): ")
                    col = int(col)
                    if col > 0 and col <= 3:
                        break
                    else:
                        print("Must be a number between 1 and 3")
                        col = input("Select column (1 - 3): ")
                col = col - 1
                row = input("Select row (1 - 3): ")
                while True:
                    while not row.isdigit():
                        print("Must be a number between 1 and 3")
                        row = input("Select row (1 - 3): ")
                    row = int(row)
                    if row > 0 and row <= 3:
                        break
                    else:
                        print("Must be a number between 1 and 3")
                        row = input("Select row (1 - 3): ")
                row = row - 1
    else:
        while True:
            if grid[row][col] == "-":
                grid[row][col] = "o"
                break
            else:
                print("That spot already has a symbol on it.")
                col = input("Select column (1 - 3): ")
                while True:
                    while not col.isdigit():
                        print("Must be a number between 1 and 3")
                        col = input("Select column (1 - 3): ")
                    col = int(col)
                    if col > 0 and col <= 3:
                        break
                    else:
                        print("Must be a number between 1 and 3")
                        col = input("Select column (1 - 3): ")
                col = col - 1
                row = input("Select row (1 - 3): ")
                while True:
                    while not row.isdigit():
                        print("Must be a number between 1 and 3")
                        row = input("Select row (1 - 3): ")
                    row = int(row)
                    if row > 0 and row <= 3:
                        break
                    else:
                        print("Must be a number between 1 and 3")
                        row = input("Select row (1 - 3): ")
                row = row - 1

#def checkverticalwin():


#def checkhorizontalwin():


#def checkdiagonalwin():


def print_grid():
    for row in grid:
        for col in row:
            print(col, end = " ")
        print("")

def main():
    initialisegrid()
    turncount = 1
    while True:
        player_turn(turncount)
        #checkverticalwin()
        #if checkvertical
        #checkdiagonalwin()
        #checkhorizontalwin()
        print_grid()
        if turncount == 9:
            print("It's a draw!")
        turncount = turncount + 1

main()