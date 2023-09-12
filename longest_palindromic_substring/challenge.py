"""
"baa" => "baa" False string full size
"baa" => "ba" False => "aa" True string full size - 1

"abaxyzzyxf" => "abaxyzzyxf" False string full size
"abaxyzzyxf" => "abaxyzzyx" False => "baxyzzyxf" False string full size - 1
"abaxyzzyxf" => "abaxyzzy" False => "baxyzzyx" False => "axyzzyxf" False string full size - 2
"abaxyzzyxf" => "abaxyzz" False => "baxyzzy" False => "axyzzyx" False => "xyzzyxf" False string full size - 3
"abaxyzzyxf" => "abaxyz" False => "baxyzz" False => "axyzzy" False => "xyzzyx" True => "yzzyxf" False string full size - 4

Found the longest Palindromic substring after 5 iterations starting with full size substring and reducing the size of the 
substrings by 1 char each time.
"""


def longestPalindromicSubstring(string):
    substring_len = len(string)
    while substring_len > 0:
        for i in range(len(string) - substring_len + 1):
            substring = string[i:i + substring_len]
            if is_palindrome(substring):
                return substring
        substring_len -= 1

def is_palindrome(string):
    return string == string[::-1]
