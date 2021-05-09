# Given a string, reverse all of its characters and return the resulting string.

# Ex: Given the following strings...

# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”
# “civic”, return “civic”

def reverseString(inputStr):
    stack = []
    for ch in inputStr:
        stack.append(ch)
    returnString = ""
    while len(stack) > 0:
        returnString+=stack.pop()
    return returnString



def test():
    testCases = ["Cat", "The Daily Byte", "civic"]
    expecteds = ["taC", "etyB yliaD ehT", "civic"]
    for case, expected in zip(testCases, expecteds):
        actual = reverseString(case)
        assert actual == expected, "Wrong answer"
    print("All test cases passed.")

test()