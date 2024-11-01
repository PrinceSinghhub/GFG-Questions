class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):

        n = len(nums) // 3

        ans = []

        for i in set(nums):
            if nums.count(i) > n:
                ans.append(i)

        if len(ans) == 0:
            return [-1]
        ans.sort()
        return ans
        # Your Code goes here.


# {
# Driver Code Starts
# Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends