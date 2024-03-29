"""
This function solves a famous problem known as
“finding a needle in the haystack.”
Both the needle and haystack are strings.

For example, if the needle is "def" and the haystack is "abcdefghi",
the needle is contained somewhere in the haystack, as "def" is a
substring of "abcdefghi".
However, if the needle is "dd", it cannot be found in the haystack
of "abcdefghi".

This function returns true or false, depending on whether the needle can be
found in the haystack:
"""


def find_needle(needle, haystack):
    return needle in haystack


def find_needle_2(needle, haystack):
    i = 0
    while len(haystack) >= len(needle) + i:
        if needle == haystack[i: i + len(needle)]:
            return True
        i += 1
    return False


"""
needle = "def"
haystack = "abcdefghi"

len_needle = 3
len_haystack = 9

while len_haystack >= len_needle + i:
    if needle == haystack[i:i + len_needle]:
        return True
    i += 1
return False


=> 9 >= 3 + 0 => [0:3] = "abc"
=> 9 >= 3 + 1 => [1:4] = "bcd"
=> 9 >= 3 + 2 => [2:5] = "cde"
=> 9 >= 3 + 3 => [3:6] = "def" -> return True
"""
