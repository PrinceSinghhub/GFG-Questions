class Solution:

    def search(self, pat, txt):
        m, n = len(pat), len(txt)
        if m > n: return 0
        arr = [0] * 26
        # --cnt is the no. of unique letters in "pat".
        cnt = 0
        # --create a required array pattern for "pat".
        for i in pat:
            if arr[ord(i) - 97] == 0:
                cnt += 1
            arr[ord(i) - 97] += 1
        # --sliding window starts.
        i = 0
        res = 0
        for j in range(n):
            index = ord(txt[j]) - 97
            arr[index] -= 1
            if arr[index] == 0: cnt -= 1

            if j >= m:
                if arr[ord(txt[i]) - 97] == 0: cnt += 1
                arr[ord(txt[i]) - 97] += 1
                i += 1
            # --if cnt==0 means required array pattern is formed.
            if cnt == 0:
                res += 1
        return res


# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        txt = input().strip()
        pat = input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc = tc - 1