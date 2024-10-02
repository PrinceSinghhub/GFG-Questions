import bisect


# User function Template for python3
class Solution:
    def minSteps(self, A, N, K):
        # code here
        A.sort()
        pre = 0
        s = sum(A)
        pre_s = []
        for i in A:
            if len(pre_s) == 0:
                pre_s.append(i)
            else:
                pre_s.append(i + pre_s[-1])
        coins = float('inf')
        for i in range(len(A)):
            if i != 0 and A[i] == A[i - 1]:
                pre += A[i]
                continue
            index = bisect.bisect_right(A, A[i] + K)
            if index > N:
                index = N
            temp = s - (pre_s[index - 1])
            temp = (temp - ((A[i] + K) * (N - index)))
            coins = min(coins, pre + temp)
            pre += A[i]
        return coins
    # {


#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        ob = Solution()
        print(ob.minSteps(A, N, K))