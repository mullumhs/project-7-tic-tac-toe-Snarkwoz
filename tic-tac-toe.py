grid = []

def initialisegrid():
    # creates the grid
    for i in range(3):
        grid.append(["-", "-", "-"])

def print_grid():
    for row in grid:
        for col in row:
            print(col, end = " ")
        print("")

def player_turn(turncount):
    # this is the check for getting a number between 1 and 3. Shows up many times
    while True:
        col = input("Select column (1 - 3): ")
        try:
            col = int(col)
            if col >= 1 and col <= 3:
                break
            else:
                print("Must be a number between 1 and 3")
        except:
            print("Must be a number between 1 and 3")
    col = col - 1
    while True:
        row = input("Select row (1 - 3): ")
        try:
            row = int(row)
            if row >= 1 and row <= 3:
                break
            else:
                print("Must be a number between 1 and 3")
        except:
            print("Must be a number between 1 and 3")
    row = row - 1
    # checks the turncount to determine which tile gets placed
    if turncount % 2 == 0:
        while True:
            if grid[row][col] == "-":
                grid[row][col] = "x"
                break
            else:
                print("That spot already has a symbol on it.")
                while True:
                    col = input("Select column (1 - 3): ")
                    try:
                        col = int(col)
                        if col >= 1 and col <= 3:
                            break
                        else:
                            print("Must be a number between 1 and 3")
                    except:
                        print("Must be a number between 1 and 3")
                col = col - 1
                while True:
                    row = input("Select row (1 - 3): ")
                    try:
                        row = int(row)
                        if row >= 1 and row <= 3:
                            break
                        else:
                            print("Must be a number between 1 and 3")
                    except:
                        print("Must be a number between 1 and 3")
                row = row - 1
    else:
        while True:
            if grid[row][col] == "-":
                grid[row][col] = "o"
                break
            else:
                print("That spot already has a symbol on it.")
                while True:
                    col = input("Select column (1 - 3): ")
                    try:
                        col = int(col)
                        if col >= 1 and col <= 3:
                            break
                        else:
                            print("Must be a number between 1 and 3")
                    except:
                        print("Must be a number between 1 and 3")
                col = col - 1
                while True:
                    row = input("Select row (1 - 3): ")
                    try:
                        row = int(row)
                        if row >= 1 and row <= 3:
                            break
                        else:
                            print("Must be a number between 1 and 3")
                    except:
                        print("Must be a number between 1 and 3")
                row = row - 1

# Each of these functions check for a win at the end of every turn.
def checkverticalwin():
    #  This one checks a win in a column
    for col in range(0,3):
        if grid[0][col] == grid[1][col] == grid[2][col] and not grid[0][col] == "-":
            if grid[0][col] == "x":
                return "x"
            if grid[0][col] == "o":
                return "o"
    return "nowin"

def checkhorizontalwin():
    # This one checks for a win in a row
    for row in range(0,3):
        if grid[row][0] == grid[row][1] == grid[row][2] and not grid[row][0] == "-":
            if grid[row][0] == "x":
                return "x"
            if grid[row][0] == "o":
                return "o"
    return "nowin"

def checkdiagonalwin():
    # This one checks for a win on the diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and not grid[1][1] == "-" or grid[0][2] == grid[1][1] == grid[2][0] and not grid[1][1] == "-":
        if grid[1][1] == "x":
            return "x"
        if grid[1][1] == "o":
            return "o"
    return "nowin"

def main():
    initialisegrid()
    turncount = 1
    print_grid()
    while True:
        player_turn(turncount)
        print_grid()
        # Runs through each win condition to check if there is a winner
        if checkverticalwin() == "x" or checkhorizontalwin() == "x" or checkdiagonalwin() == "x":
                print("Congratulations player x!")
                break
        elif checkverticalwin() == "o" or checkhorizontalwin() == "o" or checkdiagonalwin() == "o":
                print("Congratulations player o!")
                break
        elif checkverticalwin() == "nowin" and checkhorizontalwin() == "nowin" and checkdiagonalwin() == "nowin":
                print(" ")
        # Checks for a draw
        if turncount == 9:
            print("It's a draw!")
            break
        turncount = turncount + 1

main()