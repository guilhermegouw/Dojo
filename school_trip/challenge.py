"""
The Challenge

Students would like to go on a school trip at the end of the year, but they
need money to pay for it.
- To raise money, they have organized a brunch.
- To attend the brunch,
  - a student in their first year pays $12,
  - a student in their second year pays $10,
  - a student in their third year pays $7,
  - a student in their fourth year pays $5.
Of all of the money raised at the brunch, 50 percent of it can be used to pay
for the school trip (the other 50 percent is used to pay for the brunch
itself).
We are told the cost of the
    - school trip
    - the proportion of students in each year
    - the total number of students.
Determine whether the students need to raise more money for the school trip.

Input

Here are the three inputs:
- The first contains the cost in dollars of the school trip;
    ( it’s an integer between 50 and 50,000. )
- The second contains four numbers indicating the proportion of brunching
students who are in first, second, third, and fourth year.
- The third contains integer n, the number of students attending the brunch.

Output

If the students need to raise more money for the school trip,
output YES or output NO.
"""


def need_to_raise_more_money(cost, proportions, n):
    money_needed = cost * 2
    first_year_raised = (proportions[0] * n) * 12
    second_year_raised = (proportions[1] * n) * 10
    third_year_raised = (proportions[2] * n) * 7
    fourth_year_raised = (proportions[3] * n) * 5
    total_raised = (
        first_year_raised
        + second_year_raised
        + third_year_raised
        + fourth_year_raised
    )
    if money_needed > total_raised:
        return "YES"
    return "NO"
