# Given a string representing the sequence of moves a robot vacuum makes, return whether 
# or not it will return to its original position. 
# The string will only contain L, R, U, and D characters, representing left, right, up, 
# and down respectively.

# Ex: Given the following strings...

# "LR", return true
# "URURD", return false
# "RUULLDRD", return true


def vaccumCleanerPath(inputPath):
    position = 0
    for ch in inputPath:
        if ch == 'L' or ch == 'l':
            position+=2
        elif ch == 'R' or ch == 'r':
            position-=2
        elif ch == 'U' or ch == 'u':
            position+=1
        elif ch == 'D' or ch == 'd':
            position-=1
        else:
            raise NameError("Invalid character")
    return True if position == 0 else False


def vaccumCleanerPathUsingStack(inputPath):
    horizontalStack, verticalStack = [], []
    for ch in inputPath:
        if ch == 'L' or ch == 'l':
            if len(horizontalStack) == 0:
                horizontalStack.append(ch)
            else:
                horizontalStack.pop()
        elif ch == 'R' or ch == 'r':
            if len(horizontalStack) == 0:
                horizontalStack.append(ch)
            else:
                horizontalStack.pop()
        elif ch == 'U' or ch == 'u':
            if len(verticalStack) == 0:
                verticalStack.append(ch)
            else:
                verticalStack.pop()
        elif ch == 'D' or ch == 'd':
            if len(verticalStack) == 0:
                verticalStack.append(ch)
            else:
                verticalStack.pop()
        else:
            raise NameError("Invalid character")
    return True if len(horizontalStack) == 0 and len(verticalStack) == 0 else False


def test():
    testCases = ["LR", "URURD", "RUULLDRD"]
    expecteds = [True, False, True]
    for case, expected in zip(testCases, expecteds):
        actual = vaccumCleanerPath(case)
        assert actual == expected, "Wrong answer"
    print("All test cases passed for vaccumCleanerPath().")

    for case, expected in zip(testCases, expecteds):
        actual = vaccumCleanerPathUsingStack(case)
        assert actual == expected, "Wrong answer"
    print("All test cases passed for vaccumCleanerPathUsingStack().")

test()