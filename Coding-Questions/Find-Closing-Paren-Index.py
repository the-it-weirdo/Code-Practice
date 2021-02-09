import unittest
# #### Question ####
# "Sometimes (when I nest them (my parentheticals) too much 
# (like this (and this))) they get confusing."

# Write a function that, given a sentence like the one above, 
# along with the position of an opening parenthesis, 
# finds the corresponding closing parenthesis.

# Example: if the example string above is input with the 
# number 10 (position of the first parenthesis), 
# the output should be 79 (position of the last parenthesis).

# #### Approach ####
# We simply walk through the string,
# starting at our input opening parenthesis position.
# As we iterate, we keep a track of nested
# parenthesis opening and closing.

########

def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    stack = [opening_paren_index]
    for i in range(opening_paren_index+1, len(sentence)):
        if sentence[i] == '(':
            stack.append(i+opening_paren_index+1)
        if sentence[i] == ')':
            popped = stack.pop()
            if popped == opening_paren_index:
                return i
    raise Exception('No closing parenthesis')


# #### Complexities ####
# Time: O(n)
# Space: O(n). Can be improved to O(1).



# Tests

class Test(unittest.TestCase):

    def test_open_close_string(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_string(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_close(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)