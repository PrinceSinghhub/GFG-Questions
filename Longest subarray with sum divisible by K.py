class Solution:
    def longSubarrWthSumDivByK(self, arr, n, k):
        # Complete the function
        dict_ = {}
        sumAll = 0
        max_ = 0
        for i in range(n):
            sumAll += arr[i]
            temp = ((sumAll % k) + k) % k

            if (temp == 0):
                max_ = i + 1
            elif (temp in dict_.keys()):
                if (max_ < (i - dict_[temp])):
                    max_ = i - dict_[temp]


            else:
                dict_[temp] = i
        return max_

ans = Solution()
arr = [2, 7, 6, 1, 4, 5]
k = 3
n = len(arr)
print(ans.longSubarrWthSumDivByK(arr,n,k))