# Given a string, return whether or not it uses capitalization correctly. 
# A string correctly uses capitalization if all letters are capitalized, 
# no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

def capitaliseString(inputstr):
    allCaps = False
    firstCap = True
    noneCap = False
    for i in range(len(inputstr)):
        if i == 0 and not inputstr[i].isupper():
            firstCap = False
            noneCap = True
        if i == 1 and inputstr[i].isupper():
            allCaps = True

        if allCaps and inputstr[i].islower():
            return False
        if noneCap and inputstr[i].isupper():
            return False
        if not i == 0 and not allCaps and inputstr[i].isupper():
            return False
    return True


def test():
    testCases = ["USA", "Calvin", "compUter", "coding", "CCd", "CdC", "CCdE", "eeC", "eCe", "eeCe"]
    expecteds = [True, True, False, True, False, False, False, False, False, False]
    for case, expected in zip(testCases, expecteds):
        actual = capitaliseString(case)
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()
