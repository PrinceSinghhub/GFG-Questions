class Solution:
    def maxDistance(self, arr, n):
        """
        After modulus operation

        case 1: + + --> (arr[i] + i) - (arr[j] + j) --> max - min
        case 2: + - --> (arr[i] - i) - (arr[j] - j) --> max - min

        case 3: - + --> (arr[j] - j) - (arr[i] - i) --> max - min
        case 4: - - --> (arr[j] + j) - (arr[i] + i) --> max - min

        Cases 2 & 3 and cases 1 & 4 are same when we take '-' in common

        Need to calculate max and min of arr[i] + i and i - arr[i]

        """
        max_1 = float('-inf')  # arr[i] + i
        min_1 = float('inf')  # arr[j] + j from above cases

        max_2 = float('-inf')  # arr[i] - i
        min_2 = float('inf')  # arr[j] - j from above cases

        for idx, val in enumerate(arr):
            max_1 = max(max_1, val + idx)
            min_1 = min(min_1, val + idx)

            max_2 = max(max_2, val - idx)
            min_2 = min(min_2, val - idx)

        return max(max_1 - min_1, max_2 - min_2)