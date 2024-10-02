class Solution:

    def appleSequences(self, n, m, arr):

        # code here

        i=0

        j=0

        m1=0

        d={}

        while j<len(arr):

            if arr[j] in d:

                d[arr[j]]+=1

            else:

                d[arr[j]]=1

            if arr[j]=="O":

                m-=1

            if m>=0:

                m1=max(m1,j-i+1)

                j+=1

            if m<0:

                while m<0:

                    d[arr[i]]-=1

                    if arr[i]=="O":

                        m+=1

                    if d[arr[i]]==0:

                        del d[arr[i]]

                    i+=1

                j+=1

        return m1

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends