class Solution:
    def solve(self,n,arr,b):
        for i in arr:
            if i == b:
                b+=b
        return b

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n , b = map(int, input().split())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.solve(n, arr, b))