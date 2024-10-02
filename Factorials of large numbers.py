class Solution:
    def factorial(self, N):
        res=1
        for i in range(1,N+1):
            res*=i
        return str(res)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()