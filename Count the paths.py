from collections import defaultdict, deque


class Solution:
    def possible_paths(self, edges, n, s, d):
        adj=defaultdict(list)
        cnt=0
        for i,j in edges:
            adj[i].append(j)
        q=deque()
        q.append(s)
        while(q):
            node=q.popleft()
            if node == d :
                cnt+=1
            for neighbours in adj[node]:
                q.append(neighbours)
        return cnt