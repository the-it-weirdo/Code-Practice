# #### Question ####
# Given an array, find the sum of k elements such that it is maximum.
#
# E.g.: array = [80, -50, 90, 100] and k = 2
# 	answer = 190 (sum of 90 and 100).
#
# ########

#### Approach ####

# We take a Sliding window approach. At first, we find the sum of the first window i.e. the first k elements. 
# Then, we assign a variable 'max_sum' equal to window sum.
# Then for each remaining element, we add it to the window sum while simaltaneously subtracting the kth previous
# element to maintain the window length. We compare the new window sum with the 'max_sum' and update accordingly.

########

def max_k_sum(array, k):
	window_sum = 0
	max_sum = 0

	for i in array[:k]:
		window_sum+=i

	max_sum = window_sum

	for i in range(k, len(array)):
		# Add the next element in the window and subtract the previous kth element to maintain the window length.
		window_sum = window_sum + array[i] - array[i-k]
		max_sum = max(max_sum, window_sum)

	return max_sum


# #### Complexities ####

# Time Complexity: O(n)
# Space Complexity: O(1)

# ########



def test():
	test_cases = [[80, -50, 90, 100], [40, 50, 10, 90, 100], [-1, 1, -1, 1, -1, 1]]
	ks = [2, 3, 3]
	answers = [190, 200, 1]

	for case, k, expected in zip(test_cases, ks, answers):
		actual = max_k_sum(case, k)
		assert actual == expected, f"Wrong Answer. Expected: {expected}. Actual: {actual}."

	print("All test cases passed.")


test()