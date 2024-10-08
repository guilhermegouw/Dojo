"""
The Challenge

The United States is divided into geographical regions called states, each of
which contains one or more cities.
Each state has been given a two-character abbreviation.

For example:
The abbreviation for Pennsylvania is PA, and the abbreviation for
South Carolina is SC.

We’ll write city names and state abbreviations in all uppercase.
Consider the pair of cities SCRANTON PA and PARKER SC.
This pair of cities is special because the first two characters of each city
give the abbreviation for the other city’s state.
That is, the first two characters of SCRANTON give us SC
(PARKER’s state), and the first two characters of PARKER
give us PA (SCRANTON’s state).
A pair of cities is special if they meet this property and are not in the same
state.

Determine the number of special pairs of cities in the provided input.

Input

The input consists of the following lines:
- n lines, one per city. Each line gives the name of a city
in uppercase, a space, and its state’s abbreviation in
uppercase. The name of each city is between 2 and 10
characters; the abbreviation for each state is exactly
two characters. The same city name can exist in
multiple states but will not appear more than once in
the same state. The name of a city or state in this
problem is any string that meets these requirements; it
might not be the name of an actual US city or state.

Output

Write output to the file named citystate.out.
Output the number of special pairs of cities.
The time limit for solving each test case is four seconds.
"""


def count_special_pairs(cities):
    special_pairs = 0
    for i, city in enumerate(cities):
        for other_city in cities[i + 1 :]:
            if (
                city[:2] == other_city.split()[1]
                and other_city[:2] == city.split()[1]
            ):
                special_pairs += 1
    return special_pairs
