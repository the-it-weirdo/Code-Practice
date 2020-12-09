# #### Question ####

# Let's say:

# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."
# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

# Examples:

# "{ [ ] ( ) }" should return True
# "{ [ ( ] ) }" should return False
# "{ [ }" should return False

# ########

# #### Approach ####

# At first, let us make a set of all the valid pairs.

# We will use a stack to keep track of the brackets. When we encounter 
# an 'opener', we will push it in the stack. And when we encounter a 'closer',
# we will pop from the stack and check if the popped bracket and the 'closer' 
# makes a valid pair.

# If the pair is valid, continue untill we reach the end of the input string.
# If the pair is invalid, return False

# ########

def bracket_validator(input_string):
	valid_pairs = {('(', ')'), ('{', '}'), ('[', ']')}
	openers = {'(', '[', '{'}
	closers = {')', ']', '}'}
	stack = []
	for char in input_string:
		if char in openers:
			stack.append(char)
		elif char in closers:
			if len(stack) == 0:
				return False # Encounter a closer without an opener. Not valid.
			else:
				pair = (stack.pop(), char)
				if pair not in valid_pairs:
					return False # Pair not valid
		else:
			pass # Ignoring non-bracket characters
	return True # Reached end of string.


# #### Complexity ####

# Time Complexity: O(n) (one iteration through the string), 
# Space complexity: O(n) space (in the worst case, all of our characters are openers, so we push them all onto the stack).

# ########



def test():
	test_inputs = ["{ [ ] ( ) }", "{ [ ( ] ) }", "{ [ }"]
	test_outputs = [True, False, False]
	for inp, expected in zip(test_inputs, test_outputs):
		actual = bracket_validator(inp)
		assert actual == expected, f"Failed. Input: {inp}"
	print('Success')


test()