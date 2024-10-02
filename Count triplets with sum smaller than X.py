class Solution:
    def countTriplets(self, arr, n, sumo):
       #code here
       count = 0
       arr.sort()
       for i in range(n-2):
           j = i+1
           k = n-1
           rem = sumo - arr[i]
           while j<k:
               if arr[j] + arr[k] < rem:
                   count += k-j
                   j+=1
               else:
                   k-=1
       return count


#{
 # Driver Code Starts
if __name__ == '__main__':
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a=list(map(int,input().split()))
        ob = Solution()
        ans=ob.countTriplets(a,n,k)
        print(ans)
# } Driver Code Ends