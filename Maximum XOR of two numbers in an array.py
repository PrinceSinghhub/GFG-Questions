class Solution:
    def max_xor(self, arr, n):

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):

                if arr[i] ^ arr[j] > ans:
                    ans = arr[i] ^ arr[j]
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution();
        print(ob.max_xor(arr, n))