class Solution:
    def countX(self, L, R, X):
        x_count = 0
        str_x = str(X)

        for n in range(L + 1, R):
            str_n = str(n)
            if str_x in str_n:
                x_count += str_n.count(str_x)

        return x_count

ans = Solution()
print(ans.countX(10,19,1))