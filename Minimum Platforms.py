class Solution:
   def minimumPlatform(self,n,arr,dep):
       arr.sort()
       dep.sort()
       platform =1
       i=1
       j=0
       while i<n:
           if arr[i]>dep[j]:
               i+=1
               j+=1
           else:
               platform+=1
               i+=1
       return platform
#{
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))