class Solution:
    def multiplyStrings(self,s1,s2):
        res = int(s1)*int(s2)
        return res
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        a,b=input().split()
        print(Solution().multiplyStrings( a.strip() , b.strip() ))