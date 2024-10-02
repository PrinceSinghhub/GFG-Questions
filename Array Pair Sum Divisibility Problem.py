class Solution:

    def canPair(self, nums, k):

        # Code here

        if len(nums) % 2 != 0:
            return False

        rem = list(map(lambda i: i % k, nums))

        mp = {i: 0 for i in range(k)}

        print(rem)
        print(mp)
        for i in rem:
            mp[i] += 1

        for i in mp.keys():

            if i != 0 and mp[i] != mp[k - i]:
                return False

            if i == 0 and mp[i] % 2 != 0:
                return False

        return True

ans = Solution()
arr = [9,5,7,3]
print(ans.canPair(arr,6))