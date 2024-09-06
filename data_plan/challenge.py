"""
The Challenge

Pero has a data plan with his cell phone provider that offers him x megabytes
of data per month.
In addition, any data he doesn’t use in a given month carries over to the
next month.
For example:
  - If x is 10 and Pero uses only 4MB in a given month,
    the remaining 6MB carry over to the next months
    (in which he’d now have 10 + 6 = 16MB available).

We’re given the number of megabytes of data that Pero uses in each of the
first n months. Our task is to determine the number of megabytes available
for the following month.

Input

The input consists of the following lines:

- A line containing integer x, the number of megabytes given to Pero per month.
- A line containing integer n, the number of months that Pero has had the data
  plan.
- n lines, one for each month, giving the integer number of megabytes that
  Pero uses in that month.
  Each number is at least 0 and will never outstrip the number of available
  megabytes.

For example:
If x is 10 and Pero currently has 30MB available, the next number will be
atmost 30.

Output

Output the number of megabytes available for the next month.
"""


def get_mb_available(x, n, mb_used):
    available = x
    for usage in mb_used:
        available -= usage
        available += x
    return available
