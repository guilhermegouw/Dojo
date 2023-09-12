"""
The Challenge

Lena has n unopened boxes of action ﬁgures. 
The boxes cannot be opened (otherwise the action ﬁgures lose their value), so 
the order of action ﬁgures in a box cannot bechanged. 
Further, a box cannot be rotated (otherwise the action ﬁgures will be facing 
the wrong way).
Each action ﬁgure is speciﬁed by its height. 
For example:
one of the boxes might have three action ﬁgures, from left
to right, of heights 4, 5, and 7. 
When I talk about a box of action ﬁgures, I'll always list the heights from 
left to right.
Lena wants to organize the boxes, which means to arrange the boxes so that 
heights of action ﬁgures increase or stay the same from left to right.
Whether she can organize the boxes or not depends on the heights of action 
ﬁgures in the boxes. 
For example: 
- if a ﬁrst box has action ﬁgures of heights 4, 5, and 7, and a second box has 
action ﬁgures of heights 1 and 2, then she can organize these boxes by putting 
the second box ﬁrst.
- (3, 4, 5, 7), (2, 1, 2) => YES
But if we keep the ﬁrst box as is and change the second box to have action 
ﬁgures of heights 6 and 8, then there's no way to organize these boxes.
- (3, 4, 5, 7), (2, 6, 8) => NO
Determine whether it's possible for Lena to organize the boxes.

Input

The input consists of the following lines:
- A line containing integer n, the number of boxes. n is
between 1 and 100.
- n lines, one for each box. Each of these lines begins with integer k, 
indicating the number of action ﬁgures in this box. 
k is between 1 and 100. (Since k is at least 1, we don't have to worry about 
empty boxes.) 
Following k, there are k integers giving the heights of the action ﬁgures from 
left to right in this box. Each height is an integer between 1 and 10,000. 
There is a space between each pair of integers on the line.

Output

If Lena can organize the boxes, output YES; otherwise, output NO.
"""

def can_organize(boxes, *contents):
    organizable = 'YES'
    for i in range(1, boxes):
        if (contents[i][-contents[i][0]] < contents[i-1][-1]
            and contents[i][-1] > contents[i-1][-contents[i-1][0]]):
            organizable = 'NO'
            return organizable
    
    return organizable


if __name__=='__main__':
    can_organize(3, (2, 1, 2), (2, 3, 6), (1, 5))