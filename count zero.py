class Solution:
    def countZeroes(self, arr, n):
        n=0
        for i in arr:
            if i == 0:
                n+=1
        return n
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countZeroes(arr, n)
        print(ans)
        tc -= 1
