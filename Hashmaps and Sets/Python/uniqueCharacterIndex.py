# Given a string, return the index of its first unique character. 
# If a unique character does not exist, return -1.

# Ex: Given the following strings...

# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0

def uniqueCharIndex(inputstr):
    charMap = dict()
    for i in range(len(inputstr)):
        charMap[inputstr.count(inputstr[i])] = min(charMap.get(inputstr.count(inputstr[i]), i), i) #map[count] = min(map[count] if exists else index)
    return charMap.get(1, -1) # unique character will have count = 1



def test():
    testCases = ["abcabd", "thedailybyte", "developer", "aa"]
    expecteds = [2, 1, 0, -1]
    for case, expected in zip(testCases, expecteds):
        actual = uniqueCharIndex(case)
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()