class Solution:
   def increment(self, arr, N):
       if arr[-1]!=9:
           arr[N-1]=arr[N-1]+1
           return(arr)
       else:
           a=""
           list2=[]
           for i in arr:
               a+=str(i)
           a=str(int(a)+1)
           for j in a:
               list2.append(int(j))
           return(list2)

   # ans = ""

   # for i in arr:
   #     ans+=str(i)

   # add = str(int(ans)+1)

   # ans = []

   # for i in add:
   #     ans.append(int(i))

   # return ans
ans = Solution()
arr = [9,9,9]
print(ans.increment(arr,3))