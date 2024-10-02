class Solution:
    def solve(self, n, d):

        mlist = []
        str_d = str(d)

        for num in range(n + 1):
            str_num = str(num)

            if str_d in str_num:
                mlist.append(int(str_num))

        return [-1] if len(mlist) == 0 else list(map(int, mlist))

ans = Solution()
print(ans.solve(20,1))