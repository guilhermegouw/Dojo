"""
The Challenge

There are n villages located at distinct points on a straight road.
Each village is represented by an integer that indicates its position on the
road.
A village’s left neighbor is the village with the next smallest position;
a village’s right neighbor is the village with the next biggest position.
The neighborhood of a village consists of half the space between that village
and its left neighbor, plus half the space between that village and its right
neighbor.

For example:
If there’s a village at position 10, with its left neighbor at position 6
and its right neighbor at position 15, then this village’s neighborhood
starts from position 8 (halfway between 6 and 10) and ends at position 12.5
(halfway between 10 and 15).

{
    | 6 | 10 | 15 |
    starts at (6 + 10) / 2 = 8
    ends at (10 + 15) / 2 = 12.5
    size = 12.5 - 8 = 4.5
}

The leftmost and rightmost villages have only one neighbor, so the definition
of a neighborhood doesn’t make sense for them.
We’ll ignore the neighborhoods of those two villages in this problem.
The size of a neighborhood is calculated as the neighborhood’s
rightmost position minus the neighborhood’s leftmost position.

For example:
The neighborhood that goes from 8 to 12.5 has size 12.5 – 8 = 4.5.
Determine the size of the smallest neighborhood.

Input

The input consists of the following lines:
A line containing integer n, the number of villages. n is between 3 and 100.
n lines, each of which gives the position of a village.

Output

Output the size of the smallest neighborhood.
Include exactly one digit after the decimal point.
"""


def get_smallest_neighborhood(villages):
    villages.sort()
    smallest = float("inf")
    for i in range(1, len(villages) - 1):
        start = (villages[i - 1] + villages[i]) / 2
        end = (villages[i] + villages[i + 1]) / 2
        size = end - start
        if size < smallest:
            smallest = size
    return smallest
