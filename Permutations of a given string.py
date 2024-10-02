# User function Template for python3

class Solution:

    def findAllPermutations(self, nums, ans, visiteMap, ds):

        if len(ds) == len(nums):
            if ds not in ans:
                ans.append(ds)
                return
            return

        for i in range(len(nums)):

            if visiteMap[i] == False:
                visiteMap[i] = True
                ds += nums[i]
                self.findAllPermutations(nums, ans, visiteMap, ds)
                ds = ds[0:len(ds) - 1]
                visiteMap[i] = False

        # print(visiteMap)

    def find_permutation(self, nums):

        ans = []
        visiteMap = [False] * len(nums)
        ds = ""

        self.findAllPermutations(nums, ans, visiteMap, ds)

        ans.sort()
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends