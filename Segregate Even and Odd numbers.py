class Solution:

    def segregateEvenOdd(self, arr):
        old = [i for i in arr if i%2!=0]
        even = [i for i in arr if i%2==0]

        even.sort()
        old.sort()

        return even + old

ans = Solution()
arr = [12, 34, 45, 9, 8, 90, 3]
print(ans.segregateEvenOdd(arr))