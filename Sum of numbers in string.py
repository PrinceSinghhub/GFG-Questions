
class Solution:
    def findSum(self,s):
        o = "0"
        d = 0
        for i in s:
            if i.isdigit() == True:
                o += i
            else:
                d += int(o)
                o = "0"
        return d + int(o)



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.findSum(s))
