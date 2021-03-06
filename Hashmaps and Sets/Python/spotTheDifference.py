# You are given two strings, s and t which only consist of lowercase letters. 
# t is generated by shuffling the letters in s as well as potentially adding an 
# additional random character. Return the letter that was randomly added to t 
# if it exists, otherwise, return ''.
# Note: You may assume that at most one additional character can be added to t.

# Ex: Given the following strings...

# s = "foobar", t = "barfoot", return 't'
# s = "ide", t = "idea", return 'a'
# s = "coding", t "ingcod", return ''

def spotTheDifference(s, t):
    sChars = dict([(char, s.count(char)) for char in s])
    tChars = dict([(char, t.count(char)) for char in t])
    for char in t:
        if char not in sChars or sChars[char] < tChars[char]:
            return char
    return ''


def test():
    testCases = [('foobar', 'barfoot'), ('ide', 'idea'), ('coding', 'ingcod'), ('eye', 'yeee')]
    expecteds = ['t', 'a', '', 'e']
    for case, expected in zip(testCases, expecteds):
        actual = spotTheDifference(*case) # same as spotTheDifference(case[0], case[1])
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()
