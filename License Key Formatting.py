class Solution:

    def ReFormatString(self,S, K):

        l="".join(list(S.split("-")))

        s=""

        c=0

        for i in range(len(l)-1,-1,-1):

            if c==K-1:

                s+=l[i].upper()+"-"

                c=0

            else:

                s+=l[i].upper()

                c+=1

        if s.endswith("-")==True:

            return s[len(s)-2::-1]

        else:

            return s[::-1]


#{
 # Driver Code Starts
#Initial Template for Python 3


import atexit
import io
import sys
from collections import defaultdict
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        k=int(input())
        obj = Solution()
        print(obj.ReFormatString(s, k))
# } Driver Code Ends