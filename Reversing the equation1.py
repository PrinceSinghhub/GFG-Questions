class Solution:
    def reverseEqn(self, s):

        stack = ["inf"]

        for i in s:
            stack.append(i)

        ans = ""
        print(stack)

        digit = ""
        while stack:
            data = stack.pop()
            if data.isdigit():
                digit += data

            if data in "+-*/":
                ans += digit[::-1]
                digit = ""
                ans += data
                print(ans)


        return ans+digit[::-1]

S = "500+2*56-2/4"
ans = Solution()
print(ans.reverseEqn(S))