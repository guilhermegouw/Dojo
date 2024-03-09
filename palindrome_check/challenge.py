def isPalindrome(string):
    return string == string[::-1]


def is_palindrome(string):
    n = len(string)
    mid = len(string) // 2
    for i in range(mid):
        if string[i] != string[n - 1 - i]:
            return False

    return True


if __name__ == "__main__":
    is_palindrome("a")
    is_palindrome("aa")
    is_palindrome("aba")
    is_palindrome("abcdcba")
