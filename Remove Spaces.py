class Solution:
    def modify(self, s):
        s.strip()
        String = ""
        for i in s:
            if i.isalpha():
                String+=i
        return String

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)