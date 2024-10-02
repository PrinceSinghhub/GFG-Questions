class Solution:
    def LCP(self, arr, n):
        # code here
        smallest = arr[0]
        for word in arr:

            while word.startswith(smallest) != True and len(smallest) > 0:
                smallest = smallest[:-1]
            if len(smallest) == 0:
                return -1

        return smallest

ans = Solution()
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(ans.LCP(arr))