"""
The Challenge

There are n villages located at distinct points on a straight road. 
Each village is represented by an integer that indicates its position 
on the road.
- A village's left neighbor is the village with the next smallest position; 
- A village's right neighbor is the village with the next biggest position. 
The neighborhood of a village consists of half the space between that village
and its left neighbor, plus half the space between that village and its right 
neighbor. 

For example: 

If there's a village at position 10, with its left neighbor at position 6 and
its right neighbor at position 15, then this village's neighborhood starts from
position 8 (halfway between 6 and 10) and ends at 
position 12.5 (halfway between 10 and 15).

- The leftmost and rightmost villages have only one neighbor, so the deﬁnition 
of a neighborhood doesn't make sense for them. 
We'll ignore the neighborhoods of those two villages in this problem.

The size of a neighborhood is calculated as the neighborhood's rightmost 
position minus the neighborhood's leftmost position. 

For example: 

The neighborhood that goes from 8 to 12.5 has size 12.5 - 8 = 4.5.
Determine the size of the smallest neighborhood.

Input

The input consists of the following lines:
- A line containing integer n, the number of villages. n is between 3 and 100.
- n lines, each of which gives the position of a village.
Each position is an integer between -1,000,000,000 and 1,000,000,000. 
The positions need not come in order from left to right; the neighbor of a 
village could be anywhere in these lines.

Output

Output the size of the smallest neighborhood. 
Include exactly one digit after the decimal point.
"""

def get_size_of_smallest_neighborhood(villages, *positions):
    positions = sorted(positions)
    try:
        start = (positions[0] + positions[1])/ 2
        end = (positions[1] + positions[2])/ 2
        smallest = end - start
    except IndexError:
        return 'It should contain at least 3 positions'
    
    i = 0
    neighborhoods = villages - 2
    
    while i < neighborhoods:    
        start = (positions[i] + positions[i+1])/ 2
        end = (positions[i+1] + positions[i+2])/ 2
        size = end - start
        i += 1
        if size < smallest:
            smallest = size
    return smallest