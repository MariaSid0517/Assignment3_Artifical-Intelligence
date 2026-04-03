from pprint import pprint


def find_next_empty(sudoku):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for row in range(9):
        for col in range(9): # range(9) is 0, 1, 2, ... 8
            if sudoku[row][col] == -1:
                return row, col

    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(sudoku, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess

    # for a guess to be valid, then we need to follow the sudoku rules
    # not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = sudoku[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    #then the columns
    col_vals = [sudoku[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if sudoku[row][col] == guess:
                return False

    return True

def solve_sudoku(sudoku):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(sudoku)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        if is_valid(sudoku, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            sudoku[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(sudoku):
                return True
        
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        sudoku[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    #returns TRUE or FALSE if the puzzle is solvable or not
    return False

if __name__ == '__main__':
    example_board = [
        [-1, -1, 3,   7, 1, -1,   -1, -1, 9],
        [-1, -1, -1,   -1, -1, -1,   4, -1, -1],
        [-1, -1, -1,   -1, 5, -1,   -1, -1, 6],
        [9, -1, -1,   -1, -1, 5,   6, -1, -1],
        [7, -1, 8,   -1, -1, -1,   -1, -1, 1],
        [3, -1, 5,   -1, 2, -1,   -1, -1, -1],
        [-1, -1, 1,   -1, -1, 4,   -1, 2, -1],
        [-1, -1, -1,   -1, -1, -1,   7, 3, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
    unsolvable_board = [
        [5, 1, 6,   8, 4, 9,   7, 3, 5],  # two 5s in this row
        [3, -1, 7,   6, -1, 5,   -1, -1, -1],
        [-1, 8, 9,   7, -1, -1,   -1, 6, -1],
        [1, -1, 5,   -1, 2, -1,   4, -1, -1],
        [4, -1, -1,   -1, -1, -1,   -1, -1, 2],
        [-1, -1, 4,   -1, 9, -1,   3, -1, 1],
        [-1, 6, -1,   -1, -1, 3,   9, 8, -1],
        [-1, -1, -1,   5, -1, 6,   2, -1, 4],
        [-1, 4, 2,   9, 7, -1,   6, 5, -1]
    ]
    print(solve_sudoku(unsolvable_board))  # should print False
