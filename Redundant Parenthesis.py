# User function Template for python3

class Solution:
    @staticmethod
    def removeBrackets(expression):
        expressionArr = list(expression)
        n = len(expression)

        ans = [1] * (n + 1)
        lastOperator = [-1] * (n + 1)
        nextOperator = [-1] * (n + 1)

        l = -1
        for i in range(n):
            lastOperator[i] = l
            if expressionArr[i] in ['*', '+', '-', '/']:
                l = expressionArr[i]
        l = -1
        for i in range(n - 1, -1, -1):
            nextOperator[i] = l
            if expressionArr[i] in ['*', '+', '-', '/']:
                l = expressionArr[i]

        stack = []
        sign = [-1] * 256
        mp = [0] * 256
        operators = ['*', '+', '-', '/']

        for p in range(n):
            for x in operators:
                mp[ord(x)] = 0
                if x == expressionArr[p]:
                    sign[ord(x)] = p
            if expressionArr[p] == '(':
                stack.append(p)
            elif expressionArr[p] == ')':
                i = stack.pop()
                j = p

                nxt = nextOperator[j]
                last = lastOperator[i]

                for x in operators:
                    if sign[ord(x)] >= i:
                        mp[ord(x)] = 1
                ok = 0

                if i > 0 and j + 1 < n and expressionArr[i - 1] == '(' and expressionArr[j + 1] == ')':
                    ok = 1
                if mp[ord('+')] == 0 and mp[ord('*')] == 0 and mp[ord('-')] == 0 and mp[ord('/')] == 0:
                    ok = 1

                if last == -1 and nxt == -1:
                    ok = 1
                if last == '/':
                    # Handle division
                    pass
                elif last == '-' and (mp[ord('+')] == 1 or mp[ord('-')] == 1):
                    # Handle subtraction
                    pass
                elif mp[ord('-')] == 0 and mp[ord('+')] == 0:
                    ok = 1
                else:
                    if (last == -1 or last == '+' or last == '-') and (nxt == -1 or nxt == '+' or nxt == '-'):
                        ok = 1
                if ok == 1:
                    ans[i] = 0
                    ans[j] = 0
        result = []
        for i in range(n):
            if ans[i] > 0:
                result.append(expressionArr[i])
        return ''.join(result)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        Exp = input()

        ob = Solution()
        print(ob.removeBrackets(Exp))

# } Driver Code Ends