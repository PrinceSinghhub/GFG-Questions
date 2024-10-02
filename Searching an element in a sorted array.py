class Solution:

    def searchInSorted(self,arr, N, K):
        start = 0
        end = len(arr)-1

        while start<=end:
            mid = start+(end-start)//2

            if K>arr[mid]:
                start = mid+1
            if K<arr[mid]:
                end = mid-1;

            if K==arr[mid]:
                return 1
        return -1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        A = [ int(x) for x in input().strip().split() ]
        ob=Solution()
        print(ob.searchInSorted(A,N,K))