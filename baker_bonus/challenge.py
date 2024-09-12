"""
The Challenge

Baker Brie has a number of franchisees, each of which sells baked goods
to consumers.
Having reached the milestone of being in business for 13 years, Baker Brie
will celebrate by awarding bonuses based on sales.
The bonuses depend on sales per day and sales per franchisee.

Here’s how the bonuses work:

1. For every day on which the total sales across all franchisees is
a multiple of 13 that multiple will be given as bonuses.
For example:
- A day where the franchisees sold a combined 26 baked goods will add
26 / 13 = 2 bonuses to the total.

2. For every franchisee whose total sales across all days is a multiple of 13,
  that multiple will be given as bonuses.
For example:
A franchisee that sold a total of 39 baked goods will add
39 / 13 = 3 bonuses to the total.

Determine the total number of bonuses awarded.

Input

- A line containing the integer number of franchisees f and
  integer number of days d, separated by a space. (f is between 4 and 130)
  and (d is between 2 and 4,745).
- d lines, one per day, containing f integers separated by spaces.
  Each integer speciﬁes a number of sales. The first of these lines gives
  the sales for each franchise on the first day, the second gives the sales
  for each franchise on the second day, and so on.
  Each integer is between 1 and 13,000.

Output

For each test case, output the total number of bonuses awarded.
"""


def get_total_bonus(f, d, sales):
    total_bonus = 0
    for day in range(d):
        daily_sales = sum(sales[franchise][day] for franchise in range(f))
        if daily_sales % 13 == 0:
            total_bonus += daily_sales // 13

    for franchise in range(f):
        franchise_sales = sum(sales[franchise])
        if franchise_sales % 13 == 0:
            total_bonus += franchise_sales // 13

    return total_bonus
