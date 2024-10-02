from typing import List


class Solution:

    def numOfIslands(self, n: int, m: int, op: List[List[int]]) -> List[int]:

        parent, dic = {}, {}

        visited = [[False] * m for _ in range(n)]

        for i in range(n):

            for j in range(m):
                parent[(i, j)] = (i, j)

        dx = [1, -1, 0, 0]

        dy = [0, 0, 1, -1]

        ans = []

        def find_par(a):

            if parent[a] == a:
                return a

            return find_par(parent[a])

        for x in op:

            for k in range(4):

                i, j = x[0] + dx[k], x[1] + dy[k]

                if i >= 0 and j >= 0 and i < n and j < m and visited[i][j]:

                    b = find_par((i, j))

                    a = find_par((x[0], x[1]))

                    parent[a] = b

                    if a != (x[0], x[1]):

                        if a in dic:
                            del dic[a]

                            dic[b] = 1

            visited[x[0]][x[1]] = True

            if find_par((x[0], x[1])) == (x[0], x[1]):
                dic[(x[0], x[1])] = 1

            ans.append(len(dic))

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    T = int(input())
    for t in range(T):

        n = int(input())
        m = int(input())
        k = int(input())
        operators = []
        for i in range(k):
            u, v = map(int, input().strip().split())
            operators.append([u, v])
        obj = Solution()
        ans = obj.numOfIslands(n, m, operators)
        for i in ans:
            print(i, end=' ')
        print()

# } Driver Code Ends