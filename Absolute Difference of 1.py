# User function Template for python3


class Solution:
    def getDigitDiff1AndLessK(self, arr, n, k):
        li = []
        for i in range(len(arr)):
            if arr[i] < k:
                n = arr[i]
                prev = n % 10
                n = n // 10
                while n > 0:
                    curr = n % 10
                    if abs(prev - curr) != 1:
                        flag = 1
                        break
                    n = n // 10
                    if n == 0:
                        li.append(arr[i])
                    prev = curr
        return li

    # {


#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        obj = Solution();
        ans = obj.getDigitDiff1AndLessK(arr, n, k)
        for x in ans:
            print(x, end=" ")
        if len(ans) == 0:
            print(-1, end=" ")
        print()
        tc -= 1

# } Driver Code Ends