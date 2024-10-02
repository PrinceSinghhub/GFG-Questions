class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        ans = []

        for i in range(1, P + 1):
            if i not in arr:
                ans.append(0)
            else:
                ans.append(arr.count(i))

        if len(ans) != len(arr):
            for i in range(len(ans),len(arr)):
                ans.append(0)
            return ans

        return ans

    # optimize code


class Solution:
    def frequencyCount(self, arr, N, P):
        for i in range(N):
            arr[i] -= 1

        for i in range(N):
            if arr[i] % P < N:
                arr[arr[i] % P] += P

        for i in range(N):
            arr[i] = arr[i] // P
        return arr
ans = Solution()
arr = [3,2,2,2,1]
print(ans.frequencyCount(arr,5,3))