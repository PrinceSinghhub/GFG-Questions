# User function Template for python3
class Solution:

    def checkTriplet(self, arr, n):
        # code here
        for i in range(n):
            arr[i] = arr[i] * arr[i]
        arr.sort()
        for i in range(n - 1, 1, -1):
            b = 0
            c = i - 1
            while (b < c):
                if (arr[b] + arr[c] == arr[i]):
                    return 1
                    b += 1
                    c -= 1
                else:
                    if (arr[b] + arr[c] < arr[i]):
                        b += 1
                    else:
                        c -= 1
        return 0

ans = Solution()
arr = [1,2,3,4,5]
print(ans.checkTriplet(arr,5))