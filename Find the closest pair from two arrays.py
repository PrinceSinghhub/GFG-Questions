class Solution:
   def printClosest (self,arr, brr, n, m, x) :
       #code here
       diff=float('inf')
       l=0
       r=m-1
       ans=[]
       while l<n and r>=0 :
           if abs(arr[l]+brr[r]-x)<diff:
               diff=abs(arr[l]+brr[r]-x)
               if len(ans)!=0:
                   ans.pop()
                   ans.pop()
               ans.append(arr[l])
               ans.append(brr[r])
           if arr[l]+brr[r]<x:
               l+=1
           else:
               r-=1
       return ans