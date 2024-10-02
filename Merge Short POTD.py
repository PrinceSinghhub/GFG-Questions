# todo POTD: PROBLEM OF THE END
class Solution:
    def merge(self, arr, start, end):
        if len(arr)>1:
            mid = len(arr)//2
            R = arr[mid:]
            L = arr[:mid]

            Solution.merge(L,start,mid)
            Solution.merge(R,mid,end)

            i,j,k = 0

            while i<len(L) and j <len(R):
                if L[i]<R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while(i<len(L)):
                arr[k] = L[i]
                i+=1
                k+=1

            while (j < len(R)):
                arr[k] = R[j]
                j += 1
                k += 1



        # temp = []
        # a = start
        # b = m + 1
        # while a <= m or b <= end:
        #     if b > end or (a <= m and arr[a] <= arr[b]):
        #
        #         temp.append(arr[a])
        #         a += 1
        #
        #     else:
        #         temp.append(arr[b])
        #         b += 1
        #         for i in range(len(temp)):
        #             arr[start + i] = temp[i]

    def mergeSort(self, arr, l, r):
        # code here
        arr.sort()
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    n = 9
    arr = [10, 9, 8, 7, 6, 5, 4, 3,1]
    Solution().mergeSort(arr, 0, n - 1)

    for i in range(n):
        print(arr[i], end=" ")
    print()
    # t = int(input())
    # for i in range(t):
    #     n = int(input())
    #     # arr = list(map(int, input().split()))
    #     arr = [10,9,8,7,6,5,4,3,2,1]
    #     Solution().mergeSort(arr, 0, n - 1)
    #
    #     for i in range(n):
    #         print(arr[i], end=" ")
    #     print()