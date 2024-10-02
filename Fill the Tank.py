from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def minimum_amount(self, Edges, N, S, Cap):
        g = defaultdict(set)
        for frm, to in Edges:
            g[frm].add(to)
            g[to].add(frm)

        def dfs(node, amount, parent=None):
            nonlocal g, Cap
            amount -= Cap[node - 1]

            if amount < 0:
                return False

            n = len(g[node])
            if parent:
                n -= 1

            if n == 0:
                return True

            dist = amount // n

            for nxt in g[node]:
                if nxt == parent:
                    continue
                if not dfs(nxt, dist, node):
                    return False
            return True

        lo, hi = sum(Cap), 10 ** 18 + 1

        while lo < hi:
            mi = lo + (hi - lo) // 2
            if dfs(S, mi):
                hi = mi
            else:
                lo = mi + 1

        return -1 if lo > 10 ** 18 else lo