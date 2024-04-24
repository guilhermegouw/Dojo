"""
You're given a 2 dimensional array of integers(a matrix).
Write a function that returns the transpose of this matrix.

The transpose of a matrix is a flipped version of the original matrix across
its main diagonal(which runs from the top left to the bottom right); it 
switches the rows and column indices of the original matrix.

You can assume the input matrix will always have at least 1 value; however,
its width and height are not necessarily equal.

Input 1:

matrix = [
    [1, 2],
    ]

Output:

[
    [1], 
    [2]
]

Input 2:

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

Output:

[
    [1, 3, 5],
    [2, 4, 6]
]

Input 3:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:

[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
"""