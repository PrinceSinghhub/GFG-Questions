class Solution:
    # Function to arrange all letters of a string in lexicographical
    # order using Counting Sort.
    def countSort(self, arr):
        arr = sorted(arr)

        ans = ""
        for i in arr:
            ans += i

        return ans

ans = Solution()
S = "geeksforgeeks"
print(ans.countSort(S))