def uneatenLeaves(arr,n,k):
   # Your code goes here
   res = [0]*(n+1)
   co = 0
   for i in range(k):
       f = arr[i]
       if f == 1:
           return 0
       c = f
       while c<=n:
           if res[c] != 1:
               res[c] = 1
               co += 1
           c += f
   return ((n+1)-co)-1


#{
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
   # n=int(input())
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    a = list(map(int,input().split()))
    ans=uneatenLeaves(a,n,k)
    print(ans)
# } Driver Code Ends