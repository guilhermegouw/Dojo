"""
The Challenge

Farmer John has purchased a swimming pool for his cows.
The pool is open from time 0 to time 1000.
Farmer John hires n lifeguards to monitor the pool.
Each lifeguard monitors the pool for a given interval of time.

For example:
A lifeguard might start at time 2 and end at time 7.
I’ll denote such an interval as 2–7.
The number of units of time covered by an interval is the ending time minus the
starting time.

For example:
The lifeguard whose time interval is 2–7 covers 7 – 2 = 5 units of time.
Those time units are from time 2 to 3, 3 to 4, 4 to 5, 5 to 6, and 6 to 7.
Unfortunately, Farmer John only has enough money to pay for n – 1 lifeguards,
not n lifeguards, so he must fire one lifeguard.

Determine the maximum number of units of time that can still be covered after
firing one lifeguard.

Input

lifeguards is a list of tuples each tuple represents the interval covered by a
lifeguard (1, 5) where 1 is the start and 5 in the end.

Output

An integer representing the maximum intervals that can be covered after firing
a lifeguard.
"""


def get_maximum_intervals_covered(lifeguards):
    if len(lifeguards) == 1:
        return 0
    interval_by_lifeguard = [end - start for start, end in lifeguards]
    return sum(interval_by_lifeguard) - min(interval_by_lifeguard)
