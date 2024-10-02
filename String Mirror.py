class Solution:
    def stringMirror(self, str: str) -> str:
        # code here
        i, j = 0, 0
        temp = ""
        while j < len(str) - 1:
            if ord(str[j]) - ord('a') > ord(str[j + 1]) - ord('a') or (j != 0 and str[j] == str[j + 1]):
                j = j + 1
            else:
                break
        temp = str[:j + 1]
        return temp + temp[::-1]


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        str = (input())

        obj = Solution()
        res = obj.stringMirror(str)

        print(res)

# } Driver Code Ends