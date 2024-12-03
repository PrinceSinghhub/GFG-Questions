#{
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    def findTriplets(self, arr):
        ans=[]
        for i in range(0,len(arr)):
            d={}
            for j in range(i+1,len(arr)):
                if -(arr[i]+arr[j]) in d:
                    for num in d[-(arr[i]+arr[j])]:
                        ans.append([i,num,j])
                if arr[j] in d:
                    d[arr[j]].append(j)
                else:
                    d[arr[j]]=[j]
        return ans

#{
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends