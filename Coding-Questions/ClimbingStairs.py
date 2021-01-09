# #### Question ####
# A child is running up a staircase with n steps and can hop either 1 step
# or 2 steps at a time. Implement a method to count how many
# possible ways the child cn run up the stairs.
#
#  #### Approach ####
#
# Memoization
# We can get upto nth step by any of the following:
# 1. Going to the (n-1)st step and hopping 1 step.
# 2. Going to the (n-2)nd step and hopping 2 steps.
# So, we just need to add these to find out our required result.
#
# Recursively, it is count_ways(n-1) + count_ways(n-2). 
# Solving it recursively, however will give a time complexity of rougly O(2^n).
#
# ########


def count_ways(n):
	memory = [-1 for i in range(n+1)]
	return count_ways_memo(n, memory)


def count_ways_memo(n, cache):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	elif cache[n] != -1:
		return cache[n]
	else:
		cache[n] = count_ways_memo(n-1, cache) + count_ways_memo(n-2, cache)
		return cache[n]



def test():

	testCases = [2, 3, 4, 5, 6, 23, 34, 45]
	answers = [2, 3, 5, 8, 13, 46368, 9227465, 1836311903]

	for test, expected in zip(testCases, answers):
		actual = count_ways(test)

		assert expected == actual, f"Wrong answer.\nExected: {expected}\nActual: {actual}."

	print("All test cases passed.")


test()