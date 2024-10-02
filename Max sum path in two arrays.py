# Your task is to complete this function
# Function should return an integer denoting the required answer
class Solution:
    def maxSumPath(self, arr1, arr2, m, n):
        i, j = 0, 0
        result, sum1, sum2 = 0, 0, 0

        while i < m and j < n:
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1

            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1

            else:
                result += max(sum1, sum2)
                sum1, sum2 = 0, 0
                while i < m and j < n and arr1[i] == arr2[j]:
                    result += arr1[i]
                    i += 1
                    j += 1

        while i < m:
            sum1 += arr1[i]
            i += 1

        while j < n:
            sum2 += arr2[j]
            j += 1

        result += max(sum1, sum2)

        return result