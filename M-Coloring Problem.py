def graphColoring(graph, k, V):
    d = [0] * (V)

    def possible(node, i):
        for j in range(V):
            if graph[node][j] == 1 and d[j] == i:
                return False

        return True

    def color(node, V):
        if node == V:
            return True
        for i in range(1, k + 1):
            if possible(node, i):  # possible
                d[node] = i
                if color(node + 1, V) == True:
                    return True
                else:
                    d[node] = 0
        return False

    if color(0, V) == True:
        return True
    return False


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt] - 1][list[cnt + 1] - 1] = 1
            graph[list[cnt + 1] - 1][list[cnt] - 1] = 1
            cnt += 2
        if (graphColoring(graph, k, V) == True):
            print(1)
        else:
            print(0)

        t = t - 1

# } Driver Code Ends