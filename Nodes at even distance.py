class Solution:
    def countOfNodes(self, graph, n):
        q = []
        q.append([1, 0])
        vis = [False for i in range(n + 1)]
        evenc = 0
        oddc = 0
        while q:
            temp = q.pop(0)
            next_node = temp[0]
            vis[next_node] = True
            curr_dist = temp[1]
            if curr_dist % 2 == 0:
                evenc += 1
            else:
                oddc += 1
            for i in range(len(graph[next_node])):
                if not vis[graph[next_node][i]]:
                    q.append([graph[next_node][i], curr_dist + 1])
                    vis[graph[next_node][i]] = True

        evenc = evenc * (evenc - 1)
        oddc = oddc * (oddc - 1)
        return (evenc + oddc) // 2


# {
#  Driver Code Starts
# Initial Template for Python 3

from collections import defaultdict

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().split()
        graph = defaultdict(list)
        for i in range(0, 2 * n - 2, 2):
            graph[int(arr[i])].append(int(arr[i + 1]))
            graph[int(arr[i + 1])].append(int(arr[i]))

        ob = Solution()
        print(ob.countOfNodes(graph, n))