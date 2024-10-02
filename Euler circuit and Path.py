class Solution:
    def isEulerCircuitExist(self, V, adj):
        deg=[0]*V
        for fm,nxt in enumerate(adj):
            for to in nxt:
                if fm>to:
                    continue
                deg[fm]+=1
                deg[to]+=1
        seen=set()
        nonzero=[x for x in range(V) if deg[x]>0]
        q=[nonzero[0]]
        while q:
            node=q.pop()
            seen.add(node)
            for to in adj[node]:
                if to not in seen:
                    q.append(to)
        if seen!=set(nonzero):
            return 0
        o=0
        for i in deg:
            if i==0:
                continue
            if i%2!=0:
                o+=1
        if o==0:
            return 2
        elif o==2:
            return 1
        else:
            return 0

#{
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends