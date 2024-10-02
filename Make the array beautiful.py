from typing import List


class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        # code here
        stack = [arr[0]]
        for i in arr[1:]:
            if stack and (stack[-1] >= 0 and i >= 0):
                stack.append(i)
            elif stack and (stack[-1] < 0 and i < 0):
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    stack.append(i)
        return stack


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        arr = list(map(int, input().split()))

        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends