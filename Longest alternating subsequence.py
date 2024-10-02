from sortedcontainers import SortedList


# User function Template for python3
class Solution:
    def constructLowerArray(self, arr):
        # Initialize an empty SortedList to maintain elements in sorted order
        lst = SortedList()

        # Initialize the answer list with zeros, with the same length as arr
        ans = [0 for i in range(len(arr))]

        # Iterate through the array in reverse order
        for i in reversed(range(len(arr))):
            # Add the current element to the SortedList
            lst.add(arr[i])

            # Find the index of the current element in the SortedList
            # This index represents the count of elements smaller than arr[i]
            ans[i] = lst.index(arr[i])

        # Return the answer list
        return ans