# ### Question ####
# Given an array of integers(positive and negative), find the largest continuous sum.
# 
# e.g. : given [1, 2, -1, 3, 4, -1], largest continuous sum = (1 + 2 + (-1) + 3 + 4) = 9
#
# ########

# #### Approach ####
# We iterate over the array once storing and updating the maximum sum obtained.

# Let us initialize 1 variables 'max_sum' and 'current_sum' with the first element of the array.
#
# We iterate the array from index 1 (if available). For each element in the array from index 1, we add it to 'current_sum'
# and compare the 'current_sum' with the recently visited element to find maximum. 
# Then we campare the 'max_sum' and the 'current_sum' to find the maximum among these 2.
#
# Return 'max_sum' at the end of the loop
#
# ########

def largest_continuous_sum(array):
	# Initialize 2 variables 'max_sum' and 'curr_sum' with first element of the array.
	curr_sum, max_sum = array[0], array[0]

	for i in array[1:]: # Iterate over the array from index 1
		curr_sum = max(curr_sum + i, i) # For each element in the array from index 1,
		# add it to 'curr_sum' and comapre it with the sum to find the maximum and assign it to 'curr_sum'

		max_sum = max(curr_sum, max_sum) # Compare 'curr_sum' and 'max_sum' to find overall maximum.

	# Return 'max_sum' at loop end
	return max_sum


# #### Complexities ####
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# ########




def test():
	# Format: [[test_case 1], [test_case 2], .........]
	test_cases = [[1, 2, -1, 3, 4, -1], [1,2,-1, 3, 4, 10, 10, -10, -1], [-1, -1, 4, 3, -1, -1]]
	answers = [9, 29, 7]
	for case, expected in zip(test_cases, answers):
		actual = largest_continuous_sum(case)
		assert expected == actual, f"Wrong answer. Expected: {expected}. Actual: {actual}"
	print("All test cases passed")

test()