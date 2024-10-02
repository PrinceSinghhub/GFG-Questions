from collections import defaultdict


class Solution:
    def firingEmployees(self, arr, n):
        # code here
        child = defaultdict(list)

        for i in range(n):
            if arr[i] != 0:
                child[arr[i]].append(i + 1)
            else:
                root = i + 1

        cnt = 0
        depth = 1

        curr = child[root]
        next_level = []

        while curr:
            temp = curr.pop()
            next_level.extend(child[temp])

            cnt += 1 if self.checkPrime(temp + depth) else 0

            if not curr:
                depth += 1
                curr = next_level[:]
                next_level = []

        return cnt

    def checkPrime(self, val):
        isPrime = True
        for i in range(2, int(val ** 0.5) + 1):
            if val % i == 0:
                isPrime = False
                break

        return isPrime


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.firingEmployees(arr, n))
# } Driver Code Ends