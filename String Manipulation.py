class Solution:

    def removeAdj(self,v,n):

        # Your code goes here

        l=[]

        prev=[]

        while True:

            c=len(v)

            prev=v

            l=[]

            for i in range(c):

                if l==[]:

                    l.append(v[i])

                elif l[-1]!=v[i]:

                    l.append(v[i])

                else:

                    l.pop()

 

            v=l.copy() 

            if l==[]:

                return 0

            elif prev==l:

                return len(l)
    


#{ 
 # Driver Code Starts

if __name__=='__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        v=[x for x in input().split()]
        ob = Solution()
        print(ob.removeAdj(v,n))
# } Driver Code Ends