class Solution:

    # Function to find all elements in array that appear more than n/k times.
    def countOccurence(self, arr, n, k):
        cut = n // k
        count = 0

        map = {}
        for i in arr:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        value = list(map.values())
        for val in value:
            if val > cut:
                count += 1

        return count