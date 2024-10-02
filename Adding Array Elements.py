
class Solution:
    def minOperations(self, arr, n, k):
       import heapq
       c=0
       heapq.heapify(arr)
       for i in range(n):
           a=heapq.heappop(arr)
           if(a<k):
               b=heapq.heappop(arr)
               d=a+b
               heapq.heappush(arr,d)
               c=c+1
           else:
               break
       # print(c)
       return c


#{
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = Solution().minOperations(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends