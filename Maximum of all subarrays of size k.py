# User function Template for python3

class Solution:

    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):

        # code here

        j = k - 1

        ans = 0

        max = -1

        l = []

        while j <= n - 1:

            i = j - (k - 1)

            if max <= i - 1:

                ans = 0

                while i <= j:

                    if arr[i] > ans:
                        max = i

                        ans = arr[i]

                    i += 1

                l.append(ans)

            elif ans < arr[j]:

                l.append(arr[j])

                max = j

                ans = arr[j]

            else:

                l.append(ans)

            j += 1

        return l


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

# Contributed by : Nagendra Jha

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
        n, k = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(arr, n, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends