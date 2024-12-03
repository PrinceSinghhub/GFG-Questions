class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        map = {}
        for i, value in enumerate(arr):
            if value in map and i - map[value] <= k:
                return True
            map[value] = i
        return False

# Example usage
solution = Solution()
print(solution.checkDuplicatesWithinK([1, 2, 3, 4, 1, 2, 3, 4], 3))  # Output: False
print(solution.checkDuplicatesWithinK([1, 2, 3, 1, 4, 5], 3))       # Output: True
print(solution.checkDuplicatesWithinK([6, 8, 4, 1, 8, 5, 7], 3))    # Output: True
