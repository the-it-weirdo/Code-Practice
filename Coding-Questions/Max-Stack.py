# #### Question ####

# # You've already implemented this Stack class:


class Stack(object):
    
    def __init__(self):
        # Initialize an empty stack
        self.items = []

    def push(self, item):
        # Adds an element to the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the last item
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        
        return self.items.pop()
    
    def peek(self):
        # Return the last item without removing it
        if not self.items:
            return None
        return self.items[-1]


# Use your Stack class to implement a new class MaxStack with a 
# method get_max() that returns the largest element in the stack. 
# get_max() should not remove the item.

# Your stacks will contain only integers.

# ########

# #### Approach ####

# We define two new stacks within our MaxStack class—stack holds all of our integers, and maxes_stack holds our "maxima." 
# We use maxes_stack to keep our max up to date in constant time as we push() and pop():
# 	Whenever we push() a new item, we check to see if it's greater than or equal to the current max, 
# 		which is at the top of maxes_stack. If it is, we also push() it onto maxes_stack.

# 	Whenever we pop(), we also pop() from the top of maxes_stack if the item equals the top item in maxes_stack.

# ########

class MaxStack(object):

    # Implement the push, pop, and get_max methods


    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        max_peek = self.max_stack.peek()
        if max_peek is None or item >= max_peek:
            self.max_stack.push(item)
        self.stack.push(item)

    def pop(self):
        popped = self.stack.pop()
        if popped is self.max_stack.peek():
            self.max_stack.pop()
        return popped

    def get_max(self):
        return self.max_stack.peek()

# Complexity:
# Time: O(1) time for push(), pop(), and get_max(). 
# Space: O(m) additional space, where m is the number of operations performed on the stack.


#### Test ####

stack = MaxStack()
elems = [8, 3, 5, 8, 6, 9, 7]

for i in elems:
	stack.push(i)

assert stack.get_max() == max(elems), "Wrong answer"

print("Success.")