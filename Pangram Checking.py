class Solution:
    def checkPangram(self, s):

        alpha = "abcdefghijklmnopqrstuvwxyz"
        # org = ""
        count = 0
        # for i in s:
        #     if i ==" ":
        #         continue
        #     else:
        #         org+=i
        # s=org
        # s=s.lower()
        s = set(s)


        for i in s:
            i = str(i).lower()
            if i in alpha:
                count += 1
        print(count)

        if count == 26:
            return True
        else:
            return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        if (obj.checkPangram(s)):
            print(1)
        else:
            print(0)

