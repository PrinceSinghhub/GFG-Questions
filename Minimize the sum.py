class Solution:
    def minimizeSum(self, N, arr):
        import heapq

        pq = arr
        heapq.heapify(pq)

        sum = 0
        while len(pq) > 1:
            a = heapq.heappop(pq)
            b = heapq.heappop(pq)
            heapq.heappush(pq, a + b)
            sum = sum + a + b

        return sum


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends