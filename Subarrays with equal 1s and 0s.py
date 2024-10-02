# User function Template for python3

class Solution:

    # Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self, arr, n):

        d = {0: 1}
        for i in range(n):
            arr[i] = arr[i] - 1 if arr[i] == 0 else arr[i]
            s = 0
        for i in range(n):
            s += arr[i]
            d[s] = d.get(s, 0) + 1
        ans = 0
        for k in d.keys():
            ans += d[k] * (d[k] - 1) // 2
        return ans
        # Your code here


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))

        T -= 1


if __name__ == "__main__":
    main()