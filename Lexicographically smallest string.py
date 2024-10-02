from math import log2


class Solution:
    def lexicographicallySmallest(ob, S, k):
        # Check if it is a power of 2 or not and update the value of k

        if log2(len(S)) == int(log2(len(S))):
            k = k // 2
        else:
            k = k * 2

        # If the new k is greater than or equal to length of string return -1

        if len(S) <= k: return -1

        s = []  # stack to store the lexigrophical characters
        size = len(S) - k  # size of stack

        # Filling the stack in a lexigrophic order

        for i in range(len(S)):
            c = S[i]  # character at index i

            # Check if the character is smaller than characters appended in the stack previously
            # Remove those characters
            # And also keep track that the nof of characters remaing in string is sufficent to filll the stack

            while s and s[-1] > c and len(S) - i > size - len(s):
                s.pop()

            # If stack is not filled then append the character
            if size - len(s) > 0: s.append(c)

        # Return the resultant string formed from the stack
        return ''.join(c for c in s)


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, k = input().split()
        k = int(k)

        ob = Solution()
        print(ob.lexicographicallySmallest(S, k))
# } Driver Code Ends