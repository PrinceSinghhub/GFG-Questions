class Solution:

    def longestString(self, arr, n):

        # Sort the array in lexicographic order

        arr.sort()

        # Initialize a candidate for the longest string

        candidate = ""

        # Iterate through the sorted array

        for s in arr:

            # Check if all prefixes of s are present in the array

            prefixes_present = True

            for i in range(1, len(s)):

                if s[:i] not in arr:
                    prefixes_present = False

                    break

            # If all prefixes are present, update the candidate if necessary

            if prefixes_present:

                if len(s) > len(candidate):
                    candidate = s

        # Return the candidate

        return candidate


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr, n))
# } Driver Code Ends