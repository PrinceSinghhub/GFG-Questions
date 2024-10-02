class Solution:
    def findExtra(self,a,b,n):
        res = set(a) - set(b)
        for i in res:
            return a.index(i)
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        print(Solution().findExtra(a,b,n))
