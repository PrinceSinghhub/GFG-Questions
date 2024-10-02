# User function Template for python3
class Solution:
    def bracketNumbers(self, str):
        result = []

        stack = []
        count = 0
        for i in str:
            if i == '(':
                count += 1
                stack.append(count)
                result.append(count)
            elif i == ')':
                result.append(stack.pop())

        return result


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends