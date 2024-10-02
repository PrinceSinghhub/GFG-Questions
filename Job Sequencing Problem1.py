# User function Template for python3

class Solution:

    def JobScheduling(self, Jobs, n):
        M = max(j.deadline for j in Jobs)
        avail = list(range(M + 1))
        cnt, ans = 0, 0
        Jobs.sort(key=lambda x: (-x.profit, x.deadline))
        for job in Jobs:
            dl, prof = job.deadline, job.profit
            par, i = avail[dl], dl
            while i > 0 and i != par:
                avail[i] = avail[par]
                i = par
                par = avail[par]
            if i > 0:
                avail[i] = i - 1
                cnt += 1
                ans += prof

        return cnt, ans


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''

    def __init__(self, profit=0, deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        info = list(map(int, input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3 * i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit = info[3 * i + 2]
        ob = Solution()
        res = ob.JobScheduling(Jobs, n)
        print(res[0], end=" ")
        print(res[1])
# } Driver Code Ends