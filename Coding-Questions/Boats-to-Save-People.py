# #### Question ####
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

# Each boat carries at most 2 people at the same time, provided sum of their weights is at most limit.

# Given an array 'people' containing weights of each people, and a 'limit', find out the number 
# of boats required to carry all of them.

# It is gauranted that each person can be carried by a boat.

# ########

# #### Approach ####

# 2 pointer Approach

# Let, left and right be 2 pointers pointing at start and end of the array respectively.

# Now, while left<=right, 
# if left == right -> means there's only one person. So, we'll add 1 to boat count 
# 	and increase the left pointer or decrease the right pointer
# if arr[left] + arr[right] <= limit -> means the boat can carry these 2 people,
# 	we'll add 1 to boat count and decrease right pointer by 1 and increse left pointer by 1.
# else if people[left] < people[right] -> weight of person pointed by left pointer is less than the weight of person pointed by right pointer,
# 	then we'll increase boat count by 1 and decrease right by 1. That is, the right person is sent off in a new boat.
# else if people[left] > people[right] -> weight of person pointed by left pointer is greater than the weight of person pointed by right pointer,
# 	then we'll increase boat count by 1 and increase left by 1. That is, the left person is sent off in a new boat.

# ########

def count_boats(people, limit):
	boat = 0
	left = 0
	right = len(people) - 1
	while left <= right:
		boat+=1 # each time we loop, no matter the condition, boat count will increase
		if left == right: # Only 1 person left in the boat. Boat count increases by 1.
			left+=1
		elif people[left] + people[right] <= limit: # 2 people with weight less than limit. Boat count increases by 1.
			left+=1
			right-=1
		elif people[left] < people[right]: # person pointed by right has more weight than person pointed by left. 
		# Boat count increases by 1 and send right person is sent off the in that boat.
			right-=1
		else:
			# person pointed by left has more weight than person pointed by right. 
			# Boat count increases by 1 and send left person is sent off the in that boat.
			left+=1
	return boat


# ########

# Time complexity: O(nlogn)
# Space complexity: O(1)

# ########


def test():
	# format: [(test_case 1), (test_case 2).....]
	# test_case n: ([people], limit)
	testcases = [([1, 2], 3), ([3, 2, 2, 1], 3), ([2, 3, 1, 2], 3), ([1, 2, 2, 3], 3), ([3, 5, 3, 4], 5), ([3], 4)]
	answers = [1, 3, 3, 3, 4, 1]
	for case, expected in zip(testcases, answers):
		actual = count_boats(case[0], case[1]) # case[0]: [people] and case[1]: limit
		assert expected == actual, f"Wrong answer. \nExpected: {expected}\nActual: {actual}"
	print("All test cases passed.")



test()