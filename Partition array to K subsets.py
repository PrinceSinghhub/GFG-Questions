class Solution:
    def isKPartitionPossible(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]


# {
# Driver Code Starts


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)
# } Driver Code Ends