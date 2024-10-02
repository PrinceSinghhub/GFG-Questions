class Solution:

    # Function to find root of a node.
    def findRoot(self, x, par):

        # finding the node whose par[i] is equal to i.
        if x == par[x]:
            return x
        return self.findRoot(par[x], par)

    # Function to merge two nodes a and b.
    def union_(self, a, b, par, rank1):

        # find root of nodes a and b.
        root_a = self.findRoot(a, par)
        root_b = self.findRoot(b, par)

        rank_root_a = rank1[root_a]
        rank_root_b = rank1[root_b]

        # checking for rank and putting in set with higher rank.
        if rank_root_a > rank_root_b:

            par[root_b] = root_a
            rank1[root_a] += rank1[root_b]
        else:

            par[root_a] = root_b
            rank1[root_b] += rank1[root_a]

        return

    # Function to check whether 2 nodes are connected or not.
    def isConnected(self, x, y, par, rank1):

        root_x = self.findRoot(x, par)
        root_y = self.findRoot(y, par)

        # if root of both nodes is same then they are connected.
        if root_x == root_y:
            return True
        else:
            return False


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        q = int(input())

        par = [i for i in range(n + 1)]  # parent of ith node is initialized as i.
        rank1 = [1 for i in range(n + 1)]  # rank is initialized as 1 fo every node
        obj = Solution()
        for i in range(q):
            task, u, v = map(str, input().strip().split())
            u = int(u)
            v = int(v)

            if task == 'U':
                obj.union_(u, v, par, rank1)
            else:
                if obj.isConnected(u, v, par, rank1):
                    print(1)
                else:
                    print(0)

# } Driver Code Ends