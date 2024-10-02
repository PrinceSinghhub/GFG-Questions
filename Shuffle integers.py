class Solution:
    def shuffleArray(self, arr, n):
        mid = (n - 1 )// 2


        first = arr[0:mid+1]
        second = arr[mid+1::]

        print(first)
        print(second)

        ans = []

        for i in range(len(first)):
            ans.append(first[i])
            ans.append(second[i])
        return ans


ans = Solution()
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(ans.shuffleArray(arr,n))