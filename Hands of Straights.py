# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3
class Solution:
    def isStraightHand(self, N, groupSize, hand):
        # Code here
        if N % groupSize:
            return False

        count = {}
        for n in hand:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand);
        print(res)
# } Driver Code Ends