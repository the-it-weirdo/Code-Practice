#### Question ####
# Implement a queue with 2 stacks. 
# Your queue should have an enqueue and a dequeue method 
# and it should be "first in first out" (FIFO).

# Optimize for the time cost of mm calls on your queue. 
# These can be any mix of enqueue and dequeue calls.

# Assume you already have a stack implementation and it gives O(1)
# time push and pop.

########

#### Approach ####

# Let's call our stacks in_stack and out_stack.

# For enqueue, we simply push the enqueued item onto in_stack.

# For dequeue on an empty out_stack, the oldest item is at the bottom of in_stack.
# So we dig to the bottom of in_stack by pushing each item one-by-one onto out_stack 
# until we reach the bottom item, which we return.

# After moving everything from in_stack to out_stack, 
# the item that was enqueued the 2nd longest ago (after the item we just returned) 
# is at the top of out_stack, the item enqueued 3rd longest ago is just below it, etc.
# So to dequeue on a non-empty out_stack, 
# we simply return the top item from out_stack.

########

import unittest


class QueueTwoStacks(object):
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def __out_is_empty__(self):
        return len(self.out_stack) == 0
    
    def __in_is_empty__(self):
        return len(self.in_stack) == 0

    def enqueue(self, item):
        self.in_stack.append(item)


    def dequeue(self):
        if self.__out_is_empty__():
            while not self.__in_is_empty__():
                self.out_stack.append(self.in_stack.pop())
            
            if self.__out_is_empty__():
                raise IndexError("Queue empty! Cannot dequeue.")
        
        return self.out_stack.pop()



#### Complexity ####

# Each enqueue is clearly O(1) time, 
# and so is each dequeue when out_stack has items. 
# Dequeue on an empty out_stack is order of the number of items 
# in in_stack at that moment, which can vary significantly.

# We can notice that the more expensive a dequeue on an empty out_stack 
# is (that is, the more items we have to move from in_stack to out_stack), 
# the more O(1)-time dequeues off of a non-empty out_stack it wins us in the future. 
# Once items are moved from in_stack to out_stack they just sit there, 
# ready to be dequeued in O(1) time. 
# An item never moves "backwards" in our data structure.

# We might guess that this "averages out",
# so that in a set of m enqueues and dequeues,
# the total cost of all dequeues is actually just O(m).
# To check this rigorously, we can use the accounting method, 
# counting the time cost per item instead of per enqueue or dequeue.

# So let's look at the worst case for a single item, 
# which is the case where it is enqueued and then later dequeued. 
# In this case, the item enters in_stack (costing 1 push), 
# then later moves to out_stack (costing 1 pop and 1 push), 
# then later comes off out_stack to get returned (costing 1 pop).

# Each of these 4 pushes and pops is O(1) time. 
# So our total cost per item is O(1). 
# Our m enqueue and dequeue operations put m or fewer items into the system, 
# giving a total runtime of O(m)O(m).

####














# Tests

class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)