# User function Template for python3

class Solution:

    # Function to check if brackets are balanced or not.
    def ispar(self, s):
        arr = []
        for i in s:
            if i in ['(', '{', '[']:
                arr.append(i)

            elif i == ')' and len(arr) != 0 and arr[-1] == '(':
                arr.pop()

            elif i == '}' and len(arr) != 0 and arr[-1] == '{':
                arr.pop()

            elif i == ']' and len(arr) != 0 and arr[-1] == '[':
                arr.pop()

            else:
                return False

        if len(arr) == 0:
            return True
