# User function Template for python3

class Solution:
    def solve(self, n, cows, arr):
        arr.sort()
        low, high, res = 1, arr[n - 1] - arr[0], 0

        while low <= high:
            mid = (low + high) // 2
            if self.canPlaceCows(arr, n, cows, mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res

    def canPlaceCows(self, arr, n, cows, dist):
        cowCount, coordinate = 1, arr[0]
        for i in range(1, n):
            if arr[i] - coordinate >= dist:
                cowCount += 1
                coordinate = arr[i]

            if cowCount == cows: return True



        return False



# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends