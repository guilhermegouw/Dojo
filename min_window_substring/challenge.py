"""
Min Window Substring

Have the function MinWindowSubstring(strArr) take the array of strings stored 
in strArr, which will contain only two strings, the first parameter being the 
string N and the second parameter being a string K of some characters, and 
your goal is to determine the smallest substring of N that contains all the 
characters in K. 

For example: 
- if strArr is ["aaabaaddae", "aed"] 
then the smallest substring of N that contains the characters a, e, and d is 
"dae" located at the end of the string. 
So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] 
then the smallest substring of N that contains all of the characters in K 
is "aabd" which is located at the beginning of the string. 
Both parameters will be strings ranging in length from 1 to 50 characters and 
all of K's characters will exist somewhere in the string N. 
Both strings will only contains lowercase alphabetic characters.

Examples

Input: ["ahffaksfajeeubsne", "jefaa"]
Output: aksfaje

Input: ["aaffhkksemckelloe", "fhea"]
Output: affhkkse
"""


def MinWindowSubstring(strArr):
    n, k = strArr
    n_len = len(n)
    k_len = len(k)
    if n_len < k_len:
        return ""
    if n_len == k_len:
        return n if sorted(n) == sorted(k) else ""
    
    k_dict = {}
    for c in k:
        if c not in k_dict:
            k_dict[c] = 1
        else:
            k_dict[c] += 1
    
    sub_str_last_char = k_len
    sub_str = compare_chars(k_dict, n_len, sub_str_last_char, n)
    while sub_str == "":
        sub_str_last_char += 1
        sub_str = compare_chars(k_dict, n_len, sub_str_last_char, n)
    return sub_str
    
def compare_chars(k_dict, n_len, sub_str_last_char, n):
    sub_str_first_char = 0
    while sub_str_last_char <= n_len + 1:
        sub_str = n[sub_str_first_char:sub_str_last_char]
        sub_str_dict = {}
        for c in sub_str:
            if c not in sub_str_dict:
                sub_str_dict[c] = 1
            else:
                sub_str_dict[c] += 1
        for key in k_dict.keys():
            if key not in sub_str_dict or sub_str_dict[key] < k_dict[key]:
                break
            else:
                if key == list(k_dict.keys())[-1]:
                    return sub_str
        sub_str_first_char += 1
        sub_str_last_char += 1
    return ""

if __name__ == "__main__":
    print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
    print(MinWindowSubstring(["aaffhkksemckelloe", "fhea"]))
    print(MinWindowSubstring(["aabdccdbcacd", "aad"]))
    print(MinWindowSubstring(["aaabaaddae", "aed"]))
