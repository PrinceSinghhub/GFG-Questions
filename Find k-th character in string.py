class Solution:
    def kthCharacter(self, m, n, k):

        Bin = bin(m)[2::]

        arr = []
        arr.append(Bin)

        for i in range(n):

            temp = ""

            for j in Bin:
                if j == '0':
                    temp += '01'

                elif j == '1':
                    temp += '10'

            arr.append(temp)
            Bin = temp

        ans = arr[-1]
        # print(arr)


        return ans[k - 1]

ans = Solution()
m = 1
n = 0
k = 1
print(ans.kthCharacter(m,n,k))

