# User function Template for python3

class Solution:
    def uniquePerms(self, nums, n):

        results = []

        def backtrack(pointer):
            if pointer == len(nums):
                results.append(nums[:])
                return

            seen = set()  # generate an empty set eveytime the backtrack function is called
            for i in range(pointer, len(nums)):

                if nums[i] not in seen:  # do below > if nums[i] is not already in the seen

                    seen.add(nums[i])  # add nums[i] to the seen so if there is a duplicate, if condition can catch it

                    nums[i], nums[pointer] = nums[pointer], nums[i]

                    backtrack(pointer + 1)

                    nums[i], nums[pointer] = nums[pointer], nums[i]

        backtrack(0)
        results.sort()
        return results


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        res = ob.uniquePerms(arr, n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j], end=" ")
            print()
# } Driver Code Ends