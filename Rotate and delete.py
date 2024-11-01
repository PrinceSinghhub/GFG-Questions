# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:

    def rotateDelete(self, arr):
        n = len(arr)
        size = n // 2
        i = 0
        j = n - 2
        while size:
            i = (i - 1) % n
            while arr[i] == 0:
                i = (i - 1) % n
            arr[j] = 0
            t = 3
            while t:
                j = (j - 1) % n
                if arr[j] != 0:
                    t -= 1
            while arr[i] == 0:
                i = (i + 1) % n
            size -= 1
        return arr[i]


# {
# Driver Code Starts.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1

# } Driver Code Ends