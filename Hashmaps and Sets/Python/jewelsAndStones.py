# Given a string representing your stones and another string representing a list of jewels, 
# return the number of stones that you have that are also jewels.

# Ex: Given the following jewels and stones...

# jewels = "abc", stones = "ac", return 2
# jewels = "Af", stones = "AaaddfFf", return 3
# jewels = "AYOPD", stones = "ayopd", return 0

def jewelsAndStones(jewels, stones):
    # jewelSet = set(list(jewels))
    # count = 0
    # for ch in stones:
    #     if ch in jewelSet:
    #         count+=1
    # return count
    jewelSet = set(list(jewels))
    return sum(1 for c in stones if c in jewelSet)


def test():
    testCases = [("abc", "ac"), ("Af", "AaaddfFf"), ("AYOPD", "ayopd")]
    expecteds = [2, 3, 0]
    for case, expected in zip(testCases, expecteds):
        actual = jewelsAndStones(*case) # same as jewelsAndStones(case[0], case[1])
        assert actual == expected, f"Wrong answer. Case: {case}. Expected: {expected}. Actual: {actual}."
    print("All test cases passed.")


test()