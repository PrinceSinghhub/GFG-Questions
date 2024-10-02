def rev(q):
   #add code here
   Stack = []
   while (not q.empty()):
       Stack.append(q.queue[0])
       q.get()
   while (len(Stack) != 0):
       q.put(Stack[-1])
       Stack.pop()
   return q

#{
#  Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n+1)
        for j in a:
            q.put(j)
        q=rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()