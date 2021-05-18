# Given two strings s and t return whether or not s is an anagram of t.
# Note: An anagram is a word formed by reordering the letters of another word.

# Ex: Given the following strings...

# s = "cat", t = "tac", return true
# s = "listen", t = "silent", return true
# s = "program", t = "function", return false

def validAnagram(s, t):
    # convert to dictionary with each character of s and t as keys and 
    # their count as values and check if both dictionaries are equal
    return dict((c, s.count(c)) for c in s) == dict((ch, t.count(ch)) for ch in t)


def test():
    testCases = [("cat", "tac"), ("listen", "silent"), ("program", "function")]
    expecteds = [True, True, False]
    for case, expected in zip(testCases, expecteds):
        actual = validAnagram(*case) # same as validAnagram(case[0], case[1])
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()
