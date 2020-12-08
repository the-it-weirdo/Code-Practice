# #### Question ####
# A singly-linked list is built with nodes, where each node has:
# 	node.next - the next node in the list.
# 	node.value - the data held in the node.

# A cycle occurs when a node's next points back to a previous node in the list.
# The linked list is no longer linear with a begining and end - instead, 
# it cycles through a loop of nodes.

# Write a function contains_cycle() that takes the first node in a singly-linked list
# and returns a boolean indicating whether the list contains a cycle.

# E.g. 
# class LinkedListNode():

# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None


# [head]->[an object]->[another object]--
# 		    ^                           |
# 		    |___________________________|

# ########


# #### Approach 1 ####

# Traverse each node while storing it in a set. If we encounter a node which is
# already present in the set, we know we are in a cycle.

# Time Complexity: O(n)
# Space Complexity: O(n)

# ########

def contains_cycle_set(first_node):
	traverse_node = first_node
	visited = set()
	while traverse_node != None:
		if traverse_node not in visited:
			visited.add(traverse_node)
			traverse_node = traverse_node.next
		else:
			return True
	return False


# #### Approach 2 ####

# Let us consider a scenario where two runners are running on the same circular track but in different speed.
# The faster runner will eventually complete a lap and cross the slower runner. Let us apply the same concept here.

# We will keep 2 variables viz. faster and slower. Both will start at the first_node.
# We will increment faster as: faster = faster.next.next (i.e. advancing two nodes at a time)
# and slower as: slower = slower.next (i.e. advancing one node at a time)

# If our faster catches up with slower, we have a cycle. If not, our faster variable will eventually hit the end of the list.

# Time Complexity: O(n)
# Space Complexity: O(1)

# ########

def contains_cycle(first_node):
	faster = first_node
	slower = first_node
	while faster is not None and faster.next is not None:
		slower = slower.next
		faster = faster.next.next

		# faster crossing slower, we have a cycle
		if faster is slower:
			return True

	# No cycle
	return False



#### Test Code ####

class LinkedListNode():

	def __init__(self, value):
		self.value = value
		self.next = None


first_node = LinkedListNode(1)
second_node = LinkedListNode(2)
third_node = LinkedListNode(3)
fourth_node = LinkedListNode(4)

first_node.next = second_node # 1->2
second_node.next = third_node # 1->2->3
third_node.next = fourth_node # 1->2->3->4
fourth_node.next = third_node # creating a cycle here. 1->2->3->4->3...

print(f"Test using set approach (Should be True): {contains_cycle_set(first_node)}")
print(f"Test using two runner approach (Should be True): {contains_cycle(first_node)}")

fourth_node.next = None # Removing cycle. 1->2->3->4->None
print(f"Test using set approach (Should be False): {contains_cycle_set(first_node)}")
print(f"Test using two runner approach (Should be False): {contains_cycle(first_node)}")