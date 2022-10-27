import sys


def parsePuzzle(file):
    """
    Parses Sudoku puzzle into a 2D Array of int
    """
    with open(file, "r") as file:
        board = [list(map(int, line.split())) for line in file]
    return board


def solve(puzzle):
    """
    Solves the sudoku puzzle using recursion and backtracking
    """

    if not findEmpty(puzzle):
        # If a solution is found for the WHOLE puzzle, print puzzle, return true and end program
        printPuzzle(puzzle)
        return True
    else:
        # Takes the next slot that is equal to 0 or None and assigned
        row, col = findEmpty(puzzle)
    '''
    Loops 1 through 9 as potential answers and then checks
    if that number is valid, if checkNum returns true then assign
    bo[row][col] = i
    If solve returns True a solution is found for that empty slot
    if solve returns False and set previous value back to 0 and back track to try
    a different value
    '''
    for i in range(1, 10):
        if checkNum(puzzle, i, (row, col)):
            puzzle[row][col] = i
            if solve(puzzle):
                return True
            puzzle[row][col] = 0
    return False


def findEmpty(puzzle):
    """
    Finds the next empty index.
    As to not change any numbers already
    provided by the puzzle.
    Only returns boxes equal to 0 or equal to none
    Return (i, j) as row, column
    """
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j


def checkNum(puzzle, num, pos):
    """
    Check Rows, Columns, and Square to see if
    there are duplicate numbers.
    If there are NO duplicates return false
    otherwise return true
    """

    # Check Columns for duplicate values
    for i in range(9):
        if puzzle[i][pos[1]] == num:
            return False

    # Check Rows for duplicate values
    for i in range(9):
        if puzzle[pos[0]][i] == num:
            return False

    '''
    Assigns grid from (0,0) to (2,2)
    Where (0,0) is top left
    and (2,2) is bottom right
    '''
    gridRow = (pos[1] // 3) * 3
    gridCol = (pos[0] // 3) * 3

    # if gridRow > 3 or gridCol > 3:
    #    print(gridCol, gridRow)
    '''
    Values or 0, 1, 2, will be passed into gridRow / gridCol
    to access indexes in each row and col
    Such as box (0,2) we would need indexes from
    (0,6) to (0,8), (1,6) to (1,8), (2,6) to (2,8)
    '''
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[gridCol + i][gridRow + j] == num:
                return False
    return True


def printPuzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=" ")
        print()


if __name__ == "__main__":

    fileInput = input("File Name: ")
    x = parsePuzzle(fileInput)
    print("      Puzzle")
    printPuzzle(x)
    print("==================\n"
          "     Solution")
    solve(x)