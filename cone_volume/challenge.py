"""
The Challenge

Calculate the volume of a right circular cone.

Input

The input consists of two lines of text. 
The ﬁrst line contains integer r, the radius of the cone. 
The second line contains integer h, the height of the cone. 
Both r and h are between 1 and 100. (That is, the minimum value 
for r and h is 1, and the maximum value is 100.)

Output

Output the volume of the right circular cone with radius r
and height h.

The formula to calculate the volume is (πr2h)/3.
"""

from math import pi


def get_cone_volume(r, h):
    return (pi * r**2 * h) / 3
