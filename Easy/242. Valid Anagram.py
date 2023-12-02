# Problem 242. Valid Anagram
from collections import Counter

def is_anagram(s, t):

    s_dict = {}
    t_dict = {}

    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1

    for char in t:
        if char in t_dict:
            t_dict[char] += 1
        else:
            t_dict[char] = 1

    s_dict = Counter(s)
    t_dict = Counter(t)
    return s_dict == t_dict

def test_is_anagram():
    assert is_anagram('anagram', 'nagaram') == True, "Test case 1 failed"
    assert is_anagram('rat', 'car') == False, "Test case 2 failed"
    assert is_anagram('', '') == True, "Test case 3 failed"
    assert is_anagram('a', 'a') == True, "Test case 4 failed"
    assert is_anagram('ab', 'ba') == True, "Test case 5 failed"
    assert is_anagram('abc', 'def') == False, "Test case 6 failed"

test_is_anagram()