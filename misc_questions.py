### Started at 09:52

"""
1. Write a function to check whether a given string is a palindrome without using any built-in functions. (A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.) (4 points) *
"""
### Python 3.8 or higher (for walrus operator ":=")
def is_palindrome(word: str) -> bool:
    if not isinstance(word, str) or (word_len := len(word)) == 0:
        return 'Invalid input'
    i, j = 0, word_len - 1
    while word[i] == word[j]:
        i += 1
        j -= 1
        if i >= j:
            return True
    return False

# print(is_palindrome('abba'))
# print(is_palindrome('racecar'))
# print(is_palindrome('dog'))
# print(is_palindrome('frankenstein'))
# print(is_palindrome('a'))

# # ### Erroneous input
# print(is_palindrome(''))
# print(is_palindrome(2))
# print(is_palindrome(None))

"""
2. Given a sorted array of integers, write a recursive function to perform binary search. (Binary search algorithm compares the search value with the middle element of the array. If they match, then return its index. Otherwise, if the search value is less than the middle element, then repeat the algorithm on the sub-array to the left of the middle element or, if the search value is greater, on the sub-array to the right. If the remaining array to be searched is empty, then the search value cannot be found and return -1.) (6 points) *
"""

from typing import List

def binary_search(arr: List[int], search_elem: int, start: int = None, end: int = None) -> int:
    start = start if start is not None else 0
    end = end if end is not None else len(arr) - 1
    if start > end:
        return -1
    midpoint = (start + end) // 2
    middle_elem = arr[midpoint]
    if search_elem == middle_elem:
        return midpoint
    elif search_elem < middle_elem:
        return binary_search(arr, search_elem, start, midpoint - 1)
    else:
        return binary_search(arr, search_elem, midpoint + 1, end)

print(binary_search([1, 2, 3, 4], 5))

"""
3. Your friend has been kidnapped and you have received a ransom note. The note has been constructed by cutting out letters from a printed magazine. Due to the unusual font used, the police think they can find your friend if only they are sure which magazine the letters are from. Your job is to determine if the ransom note could have been constructed from the set of letters given by the police. Write a function that takes in two Strings (‘note’ and ‘magazine’). Return true if the note could have been cut out from the magazine. Example 1) note = “ceba”; magazine = “abcde” returns true (the magazine has ≥ 1 ‘e’, ≥ 1 ‘c’, ≥ 1 ‘b’, ≥ 1 ‘a’ so the note could have been made by cutting characters out of the magazine); example 2) note = “deaa”, magazine = “abcde” returns false (the note has more ‘a’ characters than can be cut out of the magazine); example 3) note = “aacc”, magazine = “bbccaa” returns true. (5 points) *
"""

from collections import Counter

def note_from_magazine(note: str, magazine: str) -> bool:
    magazine_dict = dict(Counter(list(magazine)))
    for char in note:
        if char not in magazine_dict:
            return False
        magazine_dict[char] -= 1
        if magazine_dict[char] == 0:
            del magazine_dict[char]
    return True

### Alternative solution
def note_from_magazine(note: str, magazine: str) -> bool:
    magazine_dict = dict(Counter(list(magazine)))
    for char in note:
        magazine_dict[char] = magazine_dict.get(char, 0) - 1
        if magazine_dict[char] < 0:
            return False
    return True

# print(note_from_magazine('ceba', 'abcde')) ### True
# print(note_from_magazine('deaa', 'abcde')) ### False
# print(note_from_magazine('aacc', 'bbccaa')) ### True

"""
4. Write a function that converts a Roman numeral to an integer. (ex: “I” = 1, “III” = 3, “IV” = 4, “V” = 5, “VI” = 6, “X” = 10, “L” = 50, “LX” = 60, “XLIX” = 49, “C”= 100, “CIX” = 109, “CLX” = 160, “D” = 500, “M” = 1000, “CDXLIV” = 444, “MCMIV” = 1904, …). The input to the function is a String and the output is an int. (5 points). Assume that the given Roman numeral is valid. Assume that the value will be in the range [1, 3999].Assume that you have a function rCharToInt that converts a single character to an integer. In java it would be:public static int rCharToInt(char c) { switch (c) { case ‘I’: return 1; case ‘V’: return 5; case ‘X’ return 10; case ‘L’: return 50; case ‘C’ return 100; case ‘D’ return 500; case ‘M’ return 1000; return 0;}}
"""

def rn_char_to_int(char: str) -> int:
    char_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return char_int_dict.get(char, 0)

def convert_rn_to_int(rn: str) -> int:
    reversed_rn = rn[::-1]
    res = 0
    for i, char in enumerate(reversed_rn):
        char_val = rn_char_to_int(char)
        addition = True
        if i > 0:
            last_char = reversed_rn[i - 1]
            if char_val < rn_char_to_int(last_char):
                addition = False
        res = res + char_val if addition else res - char_val
    return res

# print(convert_rn_to_int('I')) # 1
# print(convert_rn_to_int('III')) # 3
# print(convert_rn_to_int('IV')) # 4
# print(convert_rn_to_int('V')) # 5
# print(convert_rn_to_int('VI')) # 6
# print(convert_rn_to_int('X')) # 10
# print(convert_rn_to_int('L')) # 50
# print(convert_rn_to_int('LX')) # 60
# print(convert_rn_to_int('XLIX')) # 49
# print(convert_rn_to_int('C')) # 100
# print(convert_rn_to_int('CIX')) # 109
# print(convert_rn_to_int('CLX')) # 160
# print(convert_rn_to_int('D')) # 500
# print(convert_rn_to_int('M')) # 1000
# print(convert_rn_to_int('CDXLIV')) # 444
# print(convert_rn_to_int('MCMIV')) # 1904