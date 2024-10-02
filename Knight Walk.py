class Solution:
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        moves = [[-2,-1], [-2,1], [-1,-2], [1,-2], [-1,2], [1,2], [2,-1], [2,1]]
        seen = set()
        seen.add((KnightPos[0]-1, KnightPos[1]-1))
        q = [(KnightPos[0]-1, KnightPos[1]-1, 0)]
        while q:
            i, j, min_steps = q.pop(0)
            if i == TargetPos[0]-1 and j == TargetPos[1]-1:
                return min_steps
            for move in moves:
                x = move[0] + i
                y = move[1] + j
                if 0 <= x < N and 0 <= y < N and (x, y) not in seen:
                    q.append((x, y, min_steps + 1))
                    seen.add((x, y))
        return -1