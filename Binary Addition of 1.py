class Solution:
    def binaryAdd(self, n, s):

        ans = bin(int(s, 2) + 1).replace("0b", "")
        return ("0" * (n - len(ans)) + str(ans))


Bi = "1111"
ans = bin(int(Bi,2) + 1)
ans = ans[2::]
print(ans)
