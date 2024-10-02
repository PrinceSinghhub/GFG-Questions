# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends
# User function Template for python3

class Solution:

    # Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):

        Bin = bin(n)[2::]
        count = 0
        for bi in Bin[::-1]:
            if bi == "1":
                count += 1
                return count
            else:
                count += 1
        return 0
        # Your code here


# {
# Driver Code Starts.


def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        ob = Solution()

        print(ob.getFirstSetBit(n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends