from collections import Counter


class Solution:
    def maxInstance(self, s: str) -> int:
        s = list(s)
        s = Counter(s)
        x = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        ans = 100000000000000000
        for i in x:
            if i in s:
                ans = min(ans, s[i] // x[i])
        return ans


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = (input())

        obj = Solution()
        res = obj.maxInstance(s)

        print(res)

# } Driver Code Ends