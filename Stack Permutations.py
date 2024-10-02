
from typing import List
class Solution:
    def isStackPermutation(self, n : int, a : List[int], b : List[int]) -> int:
        # code here
        stack = []
        j = 0
        for i in range(n):
            if a[i] == b[j] :
                j += 1
            elif stack and stack[-1] == b[j] :
                while stack and stack[-1] == b[j]:
                    stack.pop()
                    j += 1
            else :
                stack.append(a[i])
            while stack and stack[-1] == b[j]:
                stack.pop()
                j += 1
        return 0 if j < n else 1


# } Driver Code Ends