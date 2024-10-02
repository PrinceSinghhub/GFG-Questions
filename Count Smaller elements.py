class Solution:

    def constructLowerArray(self, arr, n):

        ans = []

        index = 0

        while index < n:

            temp = arr[index]
            count = 0

            for i in arr[index::]:
                if i < temp:
                    count += 1
            ans.append(count)
            index += 1
        return ans