# User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    adj: adjacency list for the graph
    S: Source
    '''

    def bellman_ford(self, V, adj, S):
        dist = [100000000] * V
        dist[S] = 0
        for i in range(V - 1):
            for j in range(len(adj)):
                if dist[adj[j][0]] + adj[j][2] < dist[adj[j][1]]:
                    dist[adj[j][1]] = dist[adj[j][0]] + adj[j][2]

        return dist