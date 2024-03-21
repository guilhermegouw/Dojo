"""
abccba
    left = 0
    right = 5
    a(0) == a(5)
    b(1) == b(4)
    c(2) == c(3)

is_palindrome("abccba") => True

abcdedcba 9 // 2 = 4

compare left (0) and right (8)
        a = 0    a = 8
        b = 1    b = 7
        c = 2    c = 6
        d = 3    d = 5

is_palindrome("abcdedcba") => True
"""


def is_palindrome(string):
    left = 0
    right = len(string) - 1
    for i in range(len(string) // 2):
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    is_palindrome("a")
    is_palindrome("aa")
    is_palindrome("aba")
    is_palindrome("abcdcba")
