# Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical
# characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true

def palindromeString(inputStr):
    inputStr = inputStr.lower()
    i, j = 0, len(inputStr)-1
    while i < j:
        if not inputStr[i].isalpha():
            i += 1
        elif not inputStr[j].isalpha():
            j -= 1
        elif inputStr[i] != inputStr[j]:
            return False
        else:
            i += 1
            j -= 1
    return True


def test():
    testCases = ["level", "algorithm",
                 "A man, a plan, a canal: Panama.", "Race Car", "", "John Snow"]
    expecteds = [True, False, True, True, True, False]
    for case, expected in zip(testCases, expecteds):
        actual = palindromeString(case)
        assert actual == expected, "Wrong answer"
    print("All test cases passed.")


test()
