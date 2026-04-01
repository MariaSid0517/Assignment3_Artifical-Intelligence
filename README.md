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

Now, let's solve our sudoku puzzle using Python! :D