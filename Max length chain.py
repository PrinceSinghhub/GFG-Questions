#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        #code here
        count = 1
        def func(x):
            return x.b
        arr = sorted(Parr,key=func)
        curr = arr[0]
        j=0
        for i in range(len(arr)-1):
            # print(arr[i].a,arr[i].b)
            if curr.b<arr[i+1].a:
                count+=1
                curr = arr[i+1]
            else:
                j+=1
                # curr = arr[j]
        return count


#{
 # Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))
        obj=Solution()
        print(obj.maxChainLen(Parr, n))
# } Driver Code Ends