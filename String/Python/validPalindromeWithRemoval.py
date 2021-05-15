# Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "abcba", return true
# "foobof", return true (remove the first 'o', the second 'o', or 'b')
# "abccab", return false

def isValidPalindrome(inputstr):
    print(inputstr)
    return inputstr == inputstr[::-1]


def isValidPalindromeWithRemoval(inputstr):
    for i in range(len(inputstr)):
        if isValidPalindrome(inputstr[:i]+inputstr[i+1:]):
            return True
    return False


def test():
    testCases = ["abcba", "foobof", "abccab", "poope", "teye", "oolaaaaloo", "abba", "aba"]
    expecteds = [True, True, False, True, True, True, True, True]
    for case, expected in zip(testCases, expecteds):
        actual = isValidPalindromeWithRemoval(case)
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()
