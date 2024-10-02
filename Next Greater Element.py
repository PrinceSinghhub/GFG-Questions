# User function Template for python3
# optimize code
class Solution:
    def nextLargerElement(self, arr, n):
        # code here
        stack = []
        stack.append(0)
        for i in range(1, n):
            while stack and arr[stack[-1]] < arr[i]:
                index = stack.pop()
                arr[index] = arr[i]
            stack.append(i)
        while stack:
            index = stack.pop()
            arr[index] = -1
        return arr


# bruteforce Approch
# class Solution:
#     def findgre(self,arr,target,start,end):

#         for i in range(start,end):

#             if arr[i] > target:
#                 return arr[i]
#         return -1

#     def nextLargerElement(self,arr,n):


#         ans = []

#         for i in range(len(arr)):

#             if i == len(arr)-1:
#                 ans.append(-1)
#                 break

#             ans1 = self.findgre(arr,arr[i],i+1,n)
#             ans.append(ans1)

#         return ans

# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())

        a = list(map(int, input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a, n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()