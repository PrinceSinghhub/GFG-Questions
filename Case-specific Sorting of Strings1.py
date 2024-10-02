import heapq
class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,S,n):
        p = []
        q = []
        for i in range(len(S)):
            if ord(S[i])<97:
                p.append(ord(S[i]))
            else:
                q.append(ord(S[i]))
        heapq.heapify(p)
        heapq.heapify(q)
        p1 = ""
        for j in range(len(S)):
            if ord(S[j])>=97:
                p1 += chr(heapq.heappop(q))
            else:
                p1 += chr(heapq.heappop(p))
        return p1


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends