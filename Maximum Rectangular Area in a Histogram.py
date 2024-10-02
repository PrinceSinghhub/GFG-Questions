# User function Template for python3


class Solution:

    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, heights):
        n = len(heights)
        leftSmallIndexArray = [-1] * n
        rightSmallIndexArray = [-1] * n

        stack = []

        for i in range(n):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if len(stack) == 0:
                leftSmallIndexArray[i] = 0
            else:
                leftSmallIndexArray[i] = stack[-1] + 1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if len(stack) == 0:
                rightSmallIndexArray[i] = n - 1
            else:
                rightSmallIndexArray[i] = stack[-1] - 1
            stack.append(i)

        MaxArea = 0

        for i in range(n):
            MaxArea = max((rightSmallIndexArray[i] - leftSmallIndexArray[i] + 1) * heights[i], MaxArea)

        return MaxArea


# {
# Driver Code Starts
# Initial Template for Python 3

# by Jinay Shah

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends