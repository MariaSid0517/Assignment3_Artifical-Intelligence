# Assignment3_Artifical-Intelligence

Sudoku solver using backtracking

A given sudoku puzzle likes look the following puzzle: its a 9x9 square with some numbers
filled in and some empty cells

|   |   | 3 | 7 | 1 |   |   |   | 9 |
|   |   |   |   |   |   | 4 |   |   |
|   |   |   |   | 5 |   |   |   | 6 |

| 9 |   |   |   |   | 5 | 6 |   |   |
| 7 |   | 8 |   |   |   |   |   | 1 |
| 3 |   | 5 |   | 2 |   |   |   |   |

|   |   | 1 |   |   | 4 |   | 2 |   |
|   |   |   |   |   |   | 7 | 3 |   |
|   |   |   |   |   |   |   |   |   |

[[x00, x01, x02, x03... x08],
 [x10, x11, x12, x13... x18],
 ...
 [x80, x81, x82, x83... x88]]
These x_rc values correspond to the value at the rth row, cth column (starting with 0-index) These values could be empty (we will represent this with -1)

The goal is to fill in the empty spots and ensure that the rows, columns, and 
each 3x3 box have 9 different numbers.

Now, let's solve our sudoku puzzle using Python!

Packages:
To run this code, you will need to use the pprint library to bring the sudoku puzzle.
python 3.13.1


Input/Output:
To enter a puzzle to be solved, you need to enclose the entire puzzle in brackets and each row should also consist of brackets. Each number in the row should be separated by commas, and each row should be separated by a bracket and comma as well. The -1 is a placeholder for the spaces in the puzzle and will be replaced by the correct number that correctly solves the puzzle.
The output will return in the same format as the input. 

In order to change input, you need to assign a name to a puzzle using the format described above
and then call the function solve_sudoku to solve the puzzle. However, you need to print the function and it will return either true or false. 

pprint will return the solved puzzle with the correct numbers if solve_sudoku was true.