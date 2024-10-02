class Solution:
    # Back-end complete function Template for Python 3

    # Function to find the leaders in the array.
    def leaders(self, A, N):

        a = A[-1]
        arr = []
        for i in A[::-1]:
            if i >= a:
                a = i
                arr.append(a)
        return reversed(arr)